# Import Flask for web server functionality
from flask import Flask, request, jsonify

# Import OpenCV for image decoding and processing
import cv2

# Import NumPy for image array conversion
import numpy as np

# Import MediaPipe for hand tracking and landmark detection
import mediapipe as mp

# Initialize Flask app
app = Flask(__name__)

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands

# Set up hand tracking: static images, max 1 hand, confidence threshold
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.7
)

# Initialize drawing utilities (optional for visualization/debugging)
mp_draw = mp.solutions.drawing_utils

# Custom function to classify hand gesture based on hand landmarks
def classify_gesture(landmarks):
    # Indices of the tips of index, middle, ring, and pinky fingers
    finger_tips = [8, 12, 16, 20]

    # Indices of the base joints (MCP) of the same fingers
    finger_mcp = [5, 9, 13, 17]

    # Count how many fingers are extended
    extended = 0
    for tip, base in zip(finger_tips, finger_mcp):
        # A finger is considered "extended" if the tip is above the base in the image (y decreases upward)
        if landmarks[tip].y < landmarks[base].y - 0.04:    #buffer
            extended += 1
            print("Extended fingers:", extended)

    # Check thumb extension by comparing horizontal (x) position of thumb tip and joint
    # This is a simplification and may need tuning based on camera angle
    thumb_extended = landmarks[4].x > landmarks[3].x

    # Classify gesture based on number of extended fingers
    if extended <= 1:
        return "rock"
    elif extended >= 3:
        return "paper"
    elif extended == 2:
        return "scissors"
    else:
        return "unknown"

# Define a route on the Flask server that listens for POST requests at /classify
@app.route('/classify', methods=['POST'])
def classify():
    # Ensure that an image file is included in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    # Read the image from the HTTP request
    file = request.files['image']

    # Convert the uploaded file to a NumPy array (byte format)
    npimg = np.frombuffer(file.read(), np.uint8)

    # Decode the image using OpenCV
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Convert image to RGB (MediaPipe expects RGB format)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe to find hand landmarks
    result = hands.process(img_rgb)

    # If a hand is detected, classify the gesture
    if result.multi_hand_landmarks:
        # Get landmarks for the first detected hand
        landmarks = result.multi_hand_landmarks[0].landmark

        # Run gesture classification
        gesture = classify_gesture(landmarks)
    else:
        # No hand detected
        gesture = "none"

    # Return the classified gesture in JSON format
    return jsonify({'gesture': gesture})


# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    # Listen on all interfaces (0.0.0.0) so other devices can access it
    app.run(host='0.0.0.0', port=5000)
