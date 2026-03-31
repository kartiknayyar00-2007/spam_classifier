# Spam Classifier (CLI Based)

## Project Description

This project is a simple command-line based spam message classifier. It takes a text message as input and predicts whether the message is **spam** or **not spam (ham)**.

The project is built using basic machine learning concepts. It uses a dataset of sample messages and trains a model to recognize patterns commonly found in spam messages.

---

## Objective

The main objective of this project is to understand how machine learning can be used for text classification. It also demonstrates how a model can be trained and used in a simple CLI application.

---

## Technologies Used

* Python
* Pandas
* Scikit-learn

---

## Working of the Project

1. The dataset contains messages labeled as spam or ham.
2. The text data is converted into numerical form using a vectorizer.
3. A Naive Bayes model is trained on this data.
4. The trained model is saved and later used for prediction.
5. The user enters a message in the terminal, and the program predicts the result.

---

## Project Structure

```
spam_classifier/
│── data/
│── models/
│── src/
│── README.md
│── requirements.txt
```

---

## How to Run

1. Install the required libraries:

```
pip install -r requirements.txt
```

2. Train the model:

```
cd src
python train.py
```

3. Run the program:

```
python predict.py
```

---

## Sample Input / Output

Input:

```
Win money now
```

Output:

```
spam
```

Input:

```
Let's meet tomorrow
```

Output:

```
ham
```

---

## Note

The `models` folder initially contains only a placeholder file. The actual model files are generated after running the training script.

---

## Conclusion

This project shows a basic implementation of a spam classifier using machine learning. It helped in understanding text processing, model training, and prediction using Python.

---
