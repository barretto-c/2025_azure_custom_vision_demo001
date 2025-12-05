from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry, ImageFileCreateBatch
from msrest.authentication import ApiKeyCredentials
import os
from dotenv import load_dotenv


load_dotenv()

# ...existing code...
training_key = os.getenv("TRAINING_KEY")
endpoint = os.getenv("ENDPOINT")
project_id = os.getenv("PROJECT_ID")
images_folder = os.getenv("IMAGES_FOLDER", "images")
# Authenticate the client
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(endpoint, credentials)

# Delete all existing images in the project before upload
print("Deleting all existing images in the project...")
existing_images = trainer.get_images(project_id)
if existing_images:
    image_ids = [img.id for img in existing_images]
    # Custom Vision API allows deleting up to 256 images per call
    for i in range(0, len(image_ids), 256):
        trainer.delete_images(project_id, image_ids[i:i+256])
    print(f"Deleted {len(image_ids)} images.")
else:
    print("No images to delete.")

training_key = os.getenv("TRAINING_KEY")
endpoint = os.getenv("ENDPOINT")
project_id = os.getenv("PROJECT_ID")
images_folder = os.getenv("IMAGES_FOLDER", "images")
# Authenticate the client
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(endpoint, credentials)
# Get the project
project = trainer.get_project(project_id)
# Prepare images for upload
image_entries = []
for image_name in os.listdir(images_folder):
    if image_name.endswith(('.jpg', '.jpeg', '.png')):
        # Extract tag from filename (e.g., apple-01.jpg -> apple)
        tag_name = image_name.split('-')[0]
        # Ensure tag exists in project, create if not
        tags = trainer.get_tags(project.id)
        tag_obj = next((t for t in tags if t.name == tag_name), None)
        if not tag_obj:
            tag_obj = trainer.create_tag(project.id, tag_name)
        tag_id = tag_obj.id
        with open(os.path.join(images_folder, image_name), "rb") as image_file:
            image_data = image_file.read()
            image_entry = ImageFileCreateEntry(name=image_name, contents=image_data, tag_ids=[tag_id])
            image_entries.append(image_entry)
# Upload images in batches
batch_size = 64  # Custom Vision allows a maximum of 64 images per batch
for i in range(0, len(image_entries), batch_size):
    batch = ImageFileCreateBatch(images=image_entries[i:i + batch_size])
    upload_result = trainer.create_images_from_files(project.id, batch)
    if not upload_result.is_batch_successful:
        print("Image batch upload failed.")
        for image in upload_result.images:
            print(f"Image {image.source_url} upload status: {image.status}")
    else:
        print(f"Uploaded batch of {len(batch.images)} images successfully.")        
        

print("All images uploaded.")

# Print number of images per tag in the project
print("Image count per tag:")
tags = trainer.get_tags(project.id)
for tag in tags:
    images = trainer.get_tagged_images(project.id, tag_ids=[tag.id])
    print(f"Tag '{tag.name}': {len(images)} images")

