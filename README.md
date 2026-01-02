# AutoJudge - Problem Difficulty Predictor

## Overview
AutoJudge is an automated machine learning tool designed to predict the difficulty of competitive programming problems. Using problem text (description, input, and output sections), it estimates both a difficulty class and a numeric difficulty score. This helps contest setters and learners gauge how challenging a problem might be before attempting it or adding it to a contest. The system is built as an interactive web application with a Streamlit interface, making it easy to use from a browser.

## Features
- Streamlit-based web application for interactive usage
- Predicts a categorical difficulty class for competitive programming problems
- Predicts a numeric difficulty score on a scale of 0 to 10
- Uses pretrained machine learning models included in the repository
- Based on TF-IDF text features and classical ML models
- Current classification accuracy is approximately 50 percent

## Installation
To set up AutoJudge locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/nitingargiitr/ACM_open_project.git
   cd ACM_open_project
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit application:

bash
Copy code
streamlit run app.py
After running the command, the application will open automatically in your default web browser.

## Usage
Enter the Problem Description, Input Description, and Output Description in the provided text fields.

Click on the Predict Difficulty button.

The application will display:

The predicted difficulty class

The predicted difficulty score out of 10

All three input fields must be filled for the prediction to work correctly.

## Project Structure

ACM_open_project/
├── app/
│   ├── app.py                # Streamlit web application
│   └── requirements.txt      # App-specific dependencies
├── data/
│   ├── problems_data.jsonl   # Raw competitive programming dataset
│   └── processed_data.csv    # Preprocessed dataset used for training
├── models/
│   ├── tfidf.pkl             # Trained TF-IDF vectorizer
│   ├── classifier.pkl        # Logistic Regression classifier
│   └── regressor.pkl         # Linear Regression regressor
├── src/
│   ├── preprocess.py         # Data cleaning and preprocessing
│   ├── feature_extration.py  # TF-IDF feature extraction
│   ├── train_classifier.py   # Difficulty class model training
│   ├── train_regressor.py    # Difficulty score model training
│   └── evaluate.py           # Model evaluation script
├── .gitattributes
├── requirements.txt          # Global project dependencies
└── README.md

## Models
Feature Extraction: TF-IDF Vectorizer with unigrams and bigrams

Classification Model: Logistic Regression

Regression Model: Linear Regression

All trained models are already included in the models directory and are loaded directly by the application.

## Dataset
The dataset consists of competitive programming problems stored in a JSON Lines file (problems_data.jsonl).

Each problem includes:

Title

Problem description

Input description

Output description

Difficulty class label

Numeric difficulty score

The preprocess.py script cleans and merges text fields and converts the data into a CSV file used for training and evaluation.

## Evaluation
The evaluate.py script reports:

Classification accuracy and confusion matrix

Regression metrics including MAE and RMSE

The current difficulty classification accuracy is approximately 50 percent, leaving room for improvement through better models, more data, or advanced NLP techniques.

## Credits
Author: Nitin Garg

GitHub: https://github.com/nitingargiitr

Project Type: ACM Open Project

AutoJudge is developed as an open project to explore automated difficulty estimation for competitive programming problems using machine learning.








