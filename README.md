
# Azure Custom Vision Demo: Step-by-Step Guide

## 1. Create a Custom Vision Project
- Go to the [Azure Custom Vision portal](https://customvision.ai/).
- Create a new project and select the **Food** domain.

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
	- **Prediction Key** - Only after prediction
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


## 4. Upload, Train, Publish, and Test (Steps 01–04)
- Place your training images in the `images/` folder.
- Then run the following commands in order:
	```
	python 01_upload_files_for_training.py
	python 02_train_and_evaluate.py
	python 03_publish_model.py
	python 04_test_predictionl.py
	```
- For prediction, place a test image in the `test/` folder (e.g., `fruit_apple_test.jpg`).


## Troubleshooting
- Make sure your keys and endpoints are correct in `.env`.
- Use `/image` endpoint for local file prediction and `/url` for image URLs.
- If you see permission errors, double-check you are using the **Prediction Key** and **Prediction Endpoint**.

---
For more details, see Azure Custom Vision [documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/overview). 
