import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from utils import save_file

# Load dataset
df = pd.read_csv("../data/dataset.csv")

X = df["text"]
y = df["label"]

# Vectorization
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save
save_file(model, "../models/model.pkl")
save_file(vectorizer, "../models/vectorizer.pkl")

print("✅ Training complete!")
