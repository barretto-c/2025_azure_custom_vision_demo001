import requests
import os
from dotenv import load_dotenv

load_dotenv()

prediction_key = os.getenv("PREDICTION_KEY")
prediction_url = os.getenv("PREDICTION_URL")


# Set your local test image path here
image_path = os.path.join("test", "fruit_apple_test.jpg")  # Change to your actual image file

# Ensure your PREDICTION_URL ends with /image for local file prediction
if not prediction_url.strip().endswith("/image"):
    print("ERROR: PREDICTION_URL must end with /image for local file prediction.")
    print("Example: https://<your-endpoint>/customvision/v3.0/Prediction/<project-id>/classify/iterations/<iteration-name>/image")
    exit(1)

headers = {
    "Prediction-Key": prediction_key,
    "Content-Type": "application/octet-stream"
}

with open(image_path, "rb") as image_data:
    response = requests.post(prediction_url, headers=headers, data=image_data)

if response.status_code == 200:
    results = response.json()
    print(f"Results for local image '{image_path}':")
    for prediction in results.get("predictions", []):
        print(f"Tag: {prediction['tagName']}, Probability: {prediction['probability']:.2f}")
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
