from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials
import os
from dotenv import load_dotenv
import time

load_dotenv()

training_key = os.getenv("TRAINING_KEY")
endpoint = os.getenv("ENDPOINT")
project_id = os.getenv("PROJECT_ID")

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(endpoint, credentials)

# Start training
print("Starting training run...")
iteration = trainer.train_project(project_id)
print(f"Training started: Iteration ID {iteration.id}")

# Wait for training to complete
while iteration.status != "Completed":
    print(f"Training status: {iteration.status}. Waiting...")
    time.sleep(10)
    iteration = trainer.get_iteration(project_id, iteration.id)
print("Training completed.")

# Evaluate the model
metrics = trainer.get_iteration(project_id, iteration.id)
print("Evaluation Results:")
print(f"Name: {metrics.name}")
print(f"Status: {metrics.status}")
if hasattr(metrics, 'metrics') and metrics.metrics:
    print(f"Precision: {metrics.metrics.precision}")
    print(f"Recall: {metrics.metrics.recall}")
    print(f"Training accuracy: {metrics.metrics.training_accuracy}")
else:
    print("No detailed metrics available for this iteration.")
