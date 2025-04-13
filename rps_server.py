import paramiko
import time
import os
import cv2
import mediapipe as mp
import numpy as np

# Configuration
NAO_IP = "10.117.35.186"
NAO_USER = "nao"
NAO_PASS = "nao"
REMOTE_PATH = "/home/nao/recordings/cameras/gesture.jpg"
LOCAL_PATH = "gesture.jpg"

# Set up MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.7)

def classify_gesture(landmarks):
    # Indices for each fingertip and base joint
    finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
    finger_mcp = [5, 9, 13, 17]

    extended = 0
    finger_states = []

    for tip, base in zip(finger_tips, finger_mcp):
        is_extended = landmarks[tip].y < landmarks[base].y - 0.02  # Less strict threshold
        finger_states.append(is_extended)
        if is_extended:
            extended += 1

    # Optional: debug print for finger states
    print("🖐 Extended fingers:", finger_states, "| Count:", extended)

    # Detect thumb extension more carefully
    thumb_extended = abs(landmarks[4].x - landmarks[3].x) > 0.04
    print("👍 Thumb extended:", thumb_extended)

    # Classification logic
    if extended == 0 or extended == 1 or (extended == 1 and not thumb_extended):
        return "rock"
    elif extended >= 3:
        return "paper"
    elif extended == 2:
        return "scissors"
    else:
        return "unknown"


def fetch_and_classify():
    # Create an SSH client to connect to the NAO robot
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Avoid host key issues

    try:
        # Connect to NAO using SSH credentials
        ssh.connect(NAO_IP, username=NAO_USER, password=NAO_PASS)

        # Open an SFTP session for file operations
        sftp = ssh.open_sftp()

        # Get the last modification time of the image on NAO
        stat = sftp.stat(REMOTE_PATH)
        mod_time = stat.st_mtime

        global last_mod_time
        # Only proceed if the image has been updated since last check
        if mod_time != last_mod_time:
            print("🟢 New image detected! Fetching...")
            # Download the updated image to local PC
            sftp.get(REMOTE_PATH, LOCAL_PATH)
            last_mod_time = mod_time  # Update last known modification time

            # Load the image using OpenCV
            img = cv2.imread(LOCAL_PATH)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Process the image with MediaPipe to detect hand landmarks
            result = hands.process(img_rgb)

            # Run gesture classification logic
            if result.multi_hand_landmarks:
                gesture = classify_gesture(result.multi_hand_landmarks[0].landmark)
            else:
                gesture = "none"  # No hand detected

            print("🤖 Detected gesture:", gesture)

            # Write the classified gesture to a local text file
            with open("gesture_result.txt", "w") as f:
                f.write(gesture)

            # Define where the result will be stored on NAO
            result_remote_path = "/home/nao/gesture_result.txt"

            # Upload the local gesture_result.txt file back to NAO
            sftp.put("gesture_result.txt", result_remote_path)
            print("✅ Gesture written back to NAO at:", result_remote_path)

        else:
            # No new image since last check
            print("🔄 No new image yet...")

        # Close the SFTP and SSH sessions
        sftp.close()
        ssh.close()

    except Exception as e:
        # Handle and print any errors encountered during the process
        print("❌ Error:", e)


# Initialize with a dummy timestamp so first check always fetches
last_mod_time = 0

# Loop every few seconds
while True:
    fetch_and_classify()
    time.sleep(2)

