# Import required libraries
import paramiko              # For SSH and SFTP connections
import time                  # For sleep/delay between image checks
import os                    # For basic file operations
import cv2                   # OpenCV for image processing
import mediapipe as mp       # MediaPipe for hand landmark detection
import numpy as np           # NumPy for image data processing

# Configuration: NAO robot connection details and file paths
NAO_IP = "10.117.35.186"                                # NAO robot's IP address
NAO_USER = "nao"                                        # SSH username
NAO_PASS = "nao"                                        # SSH password
REMOTE_PATH = "/home/nao/recordings/cameras/gesture.jpg"  # Path to image on NAO
LOCAL_PATH = "gesture.jpg"                              # Local filename to store fetched image

# Initialize MediaPipe hand model (static image mode for snapshots)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.7
)

# Function to classify gesture from detected landmarks
def classify_gesture(landmarks):
    # Indices of fingertip landmarks (thumb to pinky)
    tip_ids = [4, 8, 12, 16, 20]
    finger_states = []  # List of True/False for each finger's extended state

    for tip_id in tip_ids:
        tip = landmarks[tip_id]       # Fingertip
        pip = landmarks[tip_id - 1]   # Joint below the tip (PIP or IP joint)

        # Thumb logic (compare x-coordinates, different axis for horizontal movement)
        if tip_id == 4:
            # Right-hand thumb: if tip.x < base.x, it's extended (leftward)
            is_extended = tip.x < pip.x
        else:
            # Other fingers: if tip is significantly above joint in y-axis
            is_extended = tip.y < pip.y - 0.015

        finger_states.append(is_extended)

    # Count how many fingers are extended
    extended_count = finger_states.count(True)

    # Print debug info
    print("🖐 Extended states:", finger_states, "| Count:", extended_count)

    # Gesture classification based on number of extended fingers
    if extended_count >= 4:
        return "paper"
    elif extended_count == 2 or extended_count == 3:
        return "scissors"
    else:
        return "rock"

# Function to fetch latest image from NAO and classify it
def fetch_and_classify():
    # Setup SSH connection to NAO
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Accept unknown hosts automatically

    try:
        # Establish SSH connection
        ssh.connect(NAO_IP, username=NAO_USER, password=NAO_PASS)

        # Open SFTP session for file transfers
        sftp = ssh.open_sftp()

        # Get timestamp of the image file on the NAO robot
        stat = sftp.stat(REMOTE_PATH)
        mod_time = stat.st_mtime

        global last_mod_time
        # Only proceed if the file has changed (new image taken)
        if mod_time != last_mod_time:
            print("🟢 New image detected! Fetching...")

            # Download the updated image
            sftp.get(REMOTE_PATH, LOCAL_PATH)
            last_mod_time = mod_time  # Update the last known modification time

            # Read image using OpenCV
            img = cv2.imread(LOCAL_PATH)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB for MediaPipe

            # Use MediaPipe to find hand landmarks
            result = hands.process(img_rgb)

            if result.multi_hand_landmarks:
                # If hand detected, classify it
                gesture = classify_gesture(result.multi_hand_landmarks[0].landmark)
            else:
                gesture = "none"  # No hand found

            print("🤖 Detected gesture:", gesture)

            # Write result to local text file
            with open("gesture_result.txt", "w") as f:
                f.write(gesture)

            # Send the result file back to the NAO robot
            result_remote_path = "/home/nao/gesture_result.txt"
            sftp.put("gesture_result.txt", result_remote_path)
            print("✅ Gesture written back to NAO at:", result_remote_path)

        else:
            # No update — same image as last time
            print("🔄 No new image yet...")

        # Close SFTP and SSH connections
        sftp.close()
        ssh.close()

    except Exception as e:
        # Print any errors that occur during SSH/SFTP/processing
        print("❌ Error:", e)

# Initialize timestamp tracker
last_mod_time = 0

# Infinite loop: periodically check for new images and classify them
while True:
    fetch_and_classify()
    time.sleep(2)  # Wait for 2 seconds before checking again
