
# Azure Custom Vision Demo: Step-by-Step Guide

## 1. Create a Custom Vision Project
- Go to the [Azure Custom Vision portal](https://customvision.ai/).
- Create a new project and select the **Food** domain.
- Upload and tag your images (minimum 5 images per tag).
- Train your model and publish an iteration (e.g., `Iteration1`).

## 2. Set Up Your Local Environment
- Clone this repository.
- Open a terminal in the project folder.
- Create a Python virtual environment:
	- **Windows:**
		```
		python -m venv venv
		.\venv\Scripts\Activate.ps1
		```
	- **Linux/macOS:**
		```
		python3 -m venv venv
		source venv/bin/activate
		```
- Install dependencies:
	```
	pip install -r requirements.txt
	```

## 3. Configure Environment Variables
- Copy your keys and IDs from the Azure portal:
	- **Training Key**
	- **Prediction Key**
	- **Endpoint URL** (use the Prediction endpoint for prediction)
	- **Project ID**
	- **Published Iteration Name**
- Edit the `.env` file and fill in these values:
	```
	TRAINING_KEY=your-training-key
	PREDICTION_KEY=your-prediction-key
	ENDPOINT=https://<your-resource>.cognitiveservices.azure.com/
	PROJECT_ID=your-project-id
	PUBLISHED_NAME=Iteration1
	PREDICTION_URL=https://<your-resource>-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/<project-id>/classify/iterations/<iteration-name>/image
	```

## 4. Upload and Tag Images
- Place your training images in the `images/` folder.
- Run `01_upload_files_for_training.py` to upload and tag images.

## 5. Train and Evaluate the Model
- Run `02_train_and_evaluate.py` to start training and print evaluation metrics.

## 6. Publish the Model
- Run `03_publish_model.py` to publish the latest trained iteration for prediction.

## 7. Test Prediction
- Place a test image in the `test/` folder (e.g., `fruit_apple_test.jpg`).
- Run `04_test_predictionl.py` to send the image to the prediction endpoint and print results.

## Troubleshooting
- Make sure your keys and endpoints are correct in `.env`.
- Use `/image` endpoint for local file prediction and `/url` for image URLs.
- If you see permission errors, double-check you are using the **Prediction Key** and **Prediction Endpoint**.

---
For more details, see Azure Custom Vision [documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/overview). 
