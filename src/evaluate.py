import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv(r"C:\Users\sonia\Desktop\acm_open_project\data\processed_data.csv")

vectorizer = pickle.load(open(r"C:\Users\sonia\Desktop\acm_open_project\models\tfidf.pkl", "rb"))
clf = pickle.load(open(r"C:\Users\sonia\Desktop\acm_open_project\models\classifier.pkl", "rb"))
reg = pickle.load(open(r"C:\Users\sonia\Desktop\acm_open_project\models\regressor.pkl", "rb"))

X = vectorizer.transform(df["text"])

# Classification
y_class = df["class"]
X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.2, random_state=42)
y_pred = clf.predict(X_test)

print("\n📊 Classification")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Regression
y_reg = df["score"]
X_train, X_test, y_train, y_test = train_test_split(X, y_reg, test_size=0.2, random_state=42)
y_pred = reg.predict(X_test)

print("\n📈 Regression")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
