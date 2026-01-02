import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(
    r"C:\Users\sonia\Desktop\acm_open_project\data\processed_data.csv"
)

vectorizer = pickle.load(
    open(r"C:\Users\sonia\Desktop\acm_open_project\models\tfidf.pkl", "rb")
)

X = vectorizer.transform(df["text"])
y = df["score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

pickle.dump(
    model,
    open(r"C:\Users\sonia\Desktop\acm_open_project\models\regressor.pkl", "wb")
)

print("✅ Linear Regression model trained & saved")
