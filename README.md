# AutoJudge – Problem Difficulty Predictor

## Project Overview
AutoJudge is a machine learning–based system that predicts the difficulty of competitive programming problems. Given a problem’s textual content (problem description, input format, and output format), the system predicts:

- A **difficulty class** (classification)
- A **numeric difficulty score** on a scale of 0 to 10 (regression)

The project is developed as an **ACM Open Project** and aims to explore automated difficulty estimation using classical NLP and machine learning techniques. A Streamlit-based web interface is provided for interactive usage.

---

## Dataset Used
The dataset consists of competitive programming problems stored in a **JSON Lines** format.

### Raw Dataset
- File: `data/problems_data.jsonl`
- Each problem includes:
  - Title
  - Problem description
  - Input description
  - Output description
  - Difficulty class label
  - Numeric difficulty score

### Preprocessed Dataset
- File: `data/processed_data.csv`
- Created using `src/preprocess.py`
- Text fields are cleaned, lowercased, and merged into a single text feature
- Used directly for feature extraction and model training

---

## Approach and Models Used

### Text Processing and Feature Extraction
- Text from title, description, input, and output sections is merged
- Preprocessing includes:
  - Lowercasing
  - Removal of special characters
  - Whitespace normalization
- Features are extracted using **TF-IDF Vectorization**
  - Unigrams and bigrams
  - Stop words removed
- Vectorizer stored as: `models/tfidf.pkl`

### Machine Learning Models
Two separate models are trained:

1. **Difficulty Classification**
   - Model: Logistic Regression
   - File: `models/classifier.pkl`
   - Script: `src/train_classifier.py`

2. **Difficulty Score Prediction**
   - Model: Linear Regression
   - File: `models/regressor.pkl`
   - Script: `src/train_regressor.py`

All trained models are included in the repository and loaded directly by the web application.

---

## Evaluation Metrics
Model evaluation is performed using `src/evaluate.py`.

### Classification Metrics
- **Accuracy**
- **Confusion Matrix**

Current classification accuracy is approximately **50 percent**.

### Regression Metrics
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**

These metrics provide insight into how close the predicted difficulty scores are to the ground truth values.

---

## Steps to Run the Project Locally
1. Clone the Repository
git clone https://github.com/nitingargiitr/ACM_open_project.git
cd ACM_open_project
2. Install Dependencies
pip install -r requirements.txt
3. Run the Web Application
streamlit run app/app.py
The application will open automatically in your default web browser.

Explanation of the Web Interface
The web interface is built using Streamlit and provides a simple, interactive way to use the model.

Input Fields
Problem Description – Full problem statement

Input Description – Input format and constraints

Output Description – Output format

Output
After clicking Predict Difficulty, the app displays:

Predicted difficulty class

Predicted difficulty score (out of 10)

All input fields must be filled for prediction to work.

Project Structure
```
ACM_open_project/
├── app/
│   ├── app.py                # Streamlit web application
├── data/
│   ├── problems_data.jsonl   # Raw dataset
│   └── processed_data.csv    # Preprocessed dataset
├── models/
│   ├── tfidf.pkl             # TF-IDF vectorizer
│   ├── classifier.pkl        # Logistic Regression model
│   └── regressor.pkl         # Linear Regression model
├── src/
│   ├── preprocess.py         # Data preprocessing
│   ├── feature_extration.py  # Feature extraction
│   ├── train_classifier.py   # Classification training
│   ├── train_regressor.py    # Regression training
│   └── evaluate.py           # Model evaluation
├── requirements.txt
├── .gitattributes
└── README.md
```

Demo Video
A short demo video (2–3 minutes) demonstrating the working of the web application is available here:

Demo Video Link:


Author Details
Name: Nitin Garg

Email: nitin_g@ece.iitr.ac.in

GitHub: https://github.com/nitingargiitr

Project Type: ACM Open Project

AutoJudge is developed as an open project to explore automated difficulty estimation for competitive programming problems using machine learning.
