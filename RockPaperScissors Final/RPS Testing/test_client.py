import requests

# Replace with the actual path to your image (can be 'rock.jpg' or similar)
image_path = "/home/b554s757/582/RPS/rock.jpg"

# Replace with your lab PC's IP address, if not running on same machine
url = "http://10.117.33.109:5000/classify"

# Open the image and send it as a POST request to the server
with open(image_path, "rb") as img:
    response = requests.post(url, files={'image': img})
    print("Server Response:", response.json())
