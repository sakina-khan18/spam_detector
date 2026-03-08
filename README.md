# 📧 Email Spam Detection System (Taipy GUI + Machine Learning)

## 📌 Project Overview

This project is a **Machine Learning based Spam Detection System** with an interactive **Taipy GUI interface**.
The system analyzes a user-entered message and predicts whether it is **Spam** or **Not Spam**.

The goal of the project is to demonstrate **pattern identification in text data using machine learning** along with a **graphical user interface**.

---

## 🎯 Problem Statement

Spam messages are a major problem in digital communication systems such as emails, SMS, and social media platforms.
Manual filtering is inefficient and time-consuming.

This project aims to build a **machine learning-based system** that can automatically classify messages as:

* 🚨 **Spam**
* ✅ **Not Spam**

---

## 🧠 Solution Approach

The system uses **Natural Language Processing (NLP)** and **Machine Learning classification**.

### Workflow

1. User enters a message in the GUI
2. Message is converted into numerical features using **CountVectorizer**
3. The trained **Naive Bayes model** predicts the label
4. The result is displayed in the GUI

---

## 🛠 Tools & Technologies

| Tool            | Purpose                   |
| --------------- | ------------------------- |
| Python          | Programming language      |
| Taipy           | GUI framework             |
| Pandas          | Data processing           |
| Scikit-learn    | Machine learning          |
| CountVectorizer | Text feature extraction   |
| Naive Bayes     | Spam classification model |

---

## 📂 Project Structure

```
spam_detector
│
├── spam.csv            # Dataset
├── train_model.py      # Machine learning training script
├── app.py              # Taipy GUI application
├── model.pkl           # Saved trained model
├── vectorizer.pkl      # Saved text vectorizer
└── README.md           # Project documentation
```

---

## 📊 Dataset

The dataset contains two columns:

| Text                   | Label |
| ---------------------- | ----- |
| Win a free iPhone now  | spam  |
| Claim your free prize  | spam  |
| Let's meet tomorrow    | ham   |
| Please send the report | ham   |

* **spam** → unwanted messages
* **ham** → normal messages

---

## ⚙️ Installation

Install required libraries:

```
pip install taipy pandas scikit-learn
```

---

## 🤖 Train the Machine Learning Model

Run:

```
python train_model.py
```

This will generate:

* `model.pkl`
* `vectorizer.pkl`

---

## 🖥 Run the GUI Application

Start the Taipy interface:

```
python app.py
```

The application will open in your browser:

```
http://localhost:5000
```

---

## 💻 GUI Interface

User can:

1. Enter a message
2. Click **Detect Spam**
3. View the classification result

Example:

Input:

```
Congratulations you won a lottery
```

Output:

```
🚨 SPAM MESSAGE
```

---

## 🚀 Features

* Machine Learning based classification
* Pattern detection in text
* Interactive GUI using Taipy
* Fast predictions
* Simple and user-friendly interface

---

## 📚 Learning Outcomes

Through this project we learned:

* Text classification using Machine Learning
* Feature extraction using CountVectorizer
* Naive Bayes algorithm
* GUI development using Taipy
* Integrating ML models with applications

---

## 🔮 Future Improvements

* Larger dataset for better accuracy
* Deep learning models
* Email integration
* Multi-language spam detection
* Web deployment

---
