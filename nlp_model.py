from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Sample training data
texts = [
    "Food was fresh and tasty",
    "Delivery was late and food was cold",
    "Very bad packaging",
    "Excellent quality",
    "Food smells bad",
    "Amazing taste and fast delivery"
]

labels = [1, 0, 0, 1, 0, 1]  # 1=Good, 0=Bad

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

def predict_complaint(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return "Good" if prediction[0] == 1 else "Bad"