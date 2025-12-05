from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials
import os
from dotenv import load_dotenv

load_dotenv()

# Set values based on your provided info
training_key = os.getenv("TRAINING_KEY")
endpoint = os.getenv("ENDPOINT")
project_id = os.getenv("PROJECT_ID")
prediction_resource_id = os.getenv("PREDICTION_RESOURCE_ID")

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(endpoint, credentials)

# Get all iterations and select the first one
iterations = trainer.get_iterations(project_id)
if not iterations:
    raise Exception("No trained iterations found. Train your model first.")
first_iteration = sorted(iterations, key=lambda x: x.created)[0]
iteration_id = first_iteration.id
published_name = first_iteration.name

# Publish the first iteration
if not first_iteration.publish_name:
    trainer.publish_iteration(project_id, iteration_id, published_name, prediction_resource_id)
    print(f"Published iteration '{first_iteration.name}' (ID: {iteration_id}) as '{published_name}'.")
else:
    print(f"Iteration '{first_iteration.name}' (ID: {iteration_id}) is already published as '{first_iteration.publish_name}'.")
