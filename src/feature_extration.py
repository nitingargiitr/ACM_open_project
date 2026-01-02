import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

DATA_PATH = r"C:\Users\sonia\Desktop\acm_open_project\data\processed_data.csv"
VEC_PATH = r"C:\Users\sonia\Desktop\acm_open_project\models\tfidf.pkl"
df = pd.read_csv(DATA_PATH)

vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),
    stop_words="english"
)

X = vectorizer.fit_transform(df["text"])

pickle.dump(vectorizer, open(VEC_PATH, "wb"))

print("✅ TF-IDF vectorizer saved")
print("Shape:", X.shape)
