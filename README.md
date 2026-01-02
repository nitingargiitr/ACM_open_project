AutoJudge - Problem Difficulty Predictor
Overview
AutoJudge is an automated machine learning tool designed to predict the difficulty of competitive programming problems. Using problem text (description, input, and output sections), it estimates both a difficulty class (e.g., category of difficulty) and a numeric difficulty score. This helps contest setters and learners gauge how challenging a problem might be before attempting it or adding it to a contest. The system is built as an interactive web application with a Streamlit interface, making it easy to use from a browser.
Features
•	Streamlit Web App: User-friendly interface to input problem details and see predictions.
•	Dual Predictions: Outputs both a categorical difficulty class and a numeric difficulty score.
•	Pretrained Models: Includes ready-to-use models (TF-IDF vectorizer, Logistic Regression classifier, and Linear Regression regressor) for quick predictions.
•	ML Models: Uses a TF-IDF transformer for text features, a Logistic Regression model for classification, and a Linear Regression model for scoring.
•	Performance: Achieves around 50% accuracy on difficulty classification with the provided dataset (improving with more data and tuning).
Installation
To set up AutoJudge locally, follow these steps:
1.	Clone the repository (replace <username> with the GitHub user, or use the project URL):

 	git clone https://github.com/nitingargiitr/AutoJudge.git
cd AutoJudge
2.	Install dependencies (requires Python 3.x):

 	pip install -r requirements.txt
3.	Run the app:

 	streamlit run app.py
This will launch the Streamlit app and open it in your default web browser.
Usage
•	Input Fields: The web app provides three text areas:
•	Problem Description: Enter the full problem statement or description.
•	Input Description: Enter the input specification/details.
•	Output Description: Enter the output specification/details.
•	After filling in all fields, click the Predict Difficulty button.
•	The app will display:
•	Difficulty Class: A categorical label (e.g., Easy/Medium/Hard or numeric class).
•	Difficulty Score: A numeric score (out of 10.0) indicating estimated difficulty.
•	Example steps:
•	Run streamlit run app.py to launch the app.
•	Enter the problem’s description, input, and output in the respective fields.
•	Click Predict Difficulty.
•	View the predicted class and score on the page.
Project Structure
The repository contains the following key scripts:
•	app.py — Streamlit Frontend: Web interface for inputting problem data and displaying predictions.
•	preprocess.py — Data Preprocessing: Reads raw JSONL data (problems_data.jsonl), cleans and combines text fields, and outputs a CSV (processed_data.csv) for training.
•	feature_extration.py — Feature Extraction: Builds and saves a TF-IDF vectorizer from the training text data (creates models/tfidf.pkl).
•	train_classifier.py — Classifier Training: Trains a Logistic Regression model on the text features to predict difficulty classes (saves models/classifier.pkl).
•	train_regressor.py — Regressor Training: Trains a Linear Regression model on the text features to predict difficulty scores (saves models/regressor.pkl).
•	evaluate.py — Model Evaluation: Evaluates the trained models on a test split, reporting classification accuracy and regression errors.
Models
The project uses the following machine learning models: - Logistic Regression (Classification): Predicts the categorical difficulty class of a problem. - Linear Regression (Regression): Predicts a numeric difficulty score (on a 0–10 scale). - TF-IDF Vectorizer: Converts problem text into numerical feature vectors for model input.
Pre-trained model files are stored in the models/ directory: - tfidf.pkl — Saved TF-IDF vectorizer. - classifier.pkl — Trained Logistic Regression classifier. - regressor.pkl — Trained Linear Regression regressor.
Dataset
•	Raw Data: The input dataset is a JSON Lines file (problems_data.jsonl) of competitive programming problems. Each entry includes fields like title, description, input_description, output_description, class (difficulty category), and score (numeric difficulty score).
•	Preprocessing: The preprocess.py script reads the JSONL file, concatenates the title, description, input, and output into one text field (after cleaning), and produces a CSV (processed_data.csv) with the combined text and corresponding class/score labels. This processed CSV is then used for training the models.

Credits
•	Author: Nitin Garg
•	GitHub: nitingargiitr
•	Project Type: ACM Open Project
AutoJudge is developed as an open project to advance research and applications in automated problem difficulty estimation for competitive programming.
