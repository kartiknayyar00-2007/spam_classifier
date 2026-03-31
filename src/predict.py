from utils import load_file

model = load_file("../models/model.pkl")
vectorizer = load_file("../models/vectorizer.pkl")

print("📩 Spam Classifier CLI")
print("Type 'exit' to quit\n")

while True:
    text = input("Enter message: ")

    if text.lower() == "exit":
        print("Exiting...")
        break

    text_vec = vectorizer.transform([text])
    result = model.predict(text_vec)

    print("Prediction:", result[0])
