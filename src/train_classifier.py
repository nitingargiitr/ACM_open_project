import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv(r"C:\Users\sonia\Desktop\acm_open_project\data\processed_data.csv")

vectorizer = pickle.load(open(r"C:\Users\sonia\Desktop\acm_open_project\models\tfidf.pkl", "rb"))
X = vectorizer.transform(df["text"])
y = df["class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

pickle.dump(model, open(r"C:\Users\sonia\Desktop\acm_open_project\models\classifier.pkl", "wb"))

print("✅ Classification model trained & saved")
