# 🤖 FAQ Chatbot

## 📌 Project Overview

This project is an **AI-based FAQ Chatbot** developed using Python.

The chatbot allows users to ask questions about Artificial Intelligence and provides the most relevant answer from a predefined collection of Frequently Asked Questions (FAQs).

The project uses **Natural Language Processing (NLP)** concepts and **TF-IDF with Cosine Similarity** to find the most similar FAQ question.

A simple **Tkinter GUI** is also provided for easy interaction.

---

## 🎯 Objectives

- Collect frequently asked questions and their answers.
- Preprocess user questions.
- Convert text into numerical vectors using TF-IDF.
- Compare the user's question with existing FAQs.
- Find the most similar question using Cosine Similarity.
- Display the appropriate answer.
- Provide a simple graphical chatbot interface.

---

## 🛠️ Technologies Used

- Python
- Tkinter
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Regular Expressions
- JSON

---

## 📁 Project Structure

```text
CodeAlpha_Chatbot/
│
├── chatbot.py
├── faqs.json
└── README.md
```

### Files Description

**chatbot.py**

Contains the main chatbot program, NLP preprocessing, similarity matching, and GUI.

**faqs.json**

Contains the predefined FAQ questions and answers.

**README.md**

Contains the project documentation.

---

## ⚙️ Installation

### Step 1: Install Python

Download and install Python from the official Python website:

https://www.python.org/

Make sure to enable **Add Python to PATH** during installation.

---

### Step 2: Install Required Library

Open the VS Code terminal and run:

```bash
pip install scikit-learn
```

Tkinter is normally included with Python on Windows.

---

## ▶️ How to Run

Open the project folder in Visual Studio Code.

Make sure the terminal is inside the project folder:

```text
CodeAlpha_Chatbot
```

Run the following command:

```bash
python chatbot.py
```

The FAQ Chatbot GUI will open.

---

## 💬 Example Questions

You can ask questions such as:

```text
What is artificial intelligence?
```

```text
What is machine learning?
```

```text
What is NLP?
```

```text
What is Python?
```

```text
What is a chatbot?
```

```text
What is deep learning?
```

```text
What is a neural network?
```

---

## 🧠 How the Chatbot Works

The chatbot follows these steps:

```text
User enters a question
        ↓
Text preprocessing
        ↓
Remove punctuation and common words
        ↓
TF-IDF Vectorization
        ↓
Calculate Cosine Similarity
        ↓
Find the most similar FAQ
        ↓
Display the matching answer
```

---

## 🔍 NLP Preprocessing

The chatbot performs basic text preprocessing.

The user's question is:

1. Converted to lowercase.
2. Punctuation is removed.
3. The sentence is split into words.
4. Common words are removed.
5. The processed text is used for similarity matching.

For example:

```text
Original:
What is Artificial Intelligence?

Processed:
artificial intelligence
```

---

## 📊 TF-IDF

**TF-IDF** stands for **Term Frequency-Inverse Document Frequency**.

It converts text into numerical values so that the computer can compare different questions.

The chatbot uses TF-IDF to represent both the user's question and the stored FAQ questions.

---

## 📐 Cosine Similarity

Cosine Similarity is used to measure how similar two text vectors are.

The chatbot compares the user's question with all available FAQ questions.

The FAQ with the highest similarity score is selected.

If the similarity is too low, the chatbot responds:

```text
Sorry, I don't know the answer to that question.
```

---

## 🖥️ Graphical User Interface

The project uses **Tkinter** to provide a simple chat interface.

The interface contains:

- Chat display area
- Text input box
- Send button
- Clear button

Users can type a question and click **Send** to receive an answer.

---

## ✨ Features

- 🤖 AI-based FAQ chatbot
- 💬 Interactive GUI
- 🔍 Similarity-based question matching
- 📊 TF-IDF text representation
- 📐 Cosine Similarity
- 📚 JSON-based FAQ database
- 🧹 Text preprocessing
- 🗑️ Clear chat option
- ⌨️ Enter key support

---

## 🚀 Future Enhancements

The chatbot can be improved by adding:

- More FAQs
- Voice input
- Text-to-speech
- Multiple topics
- Database integration
- Better NLP techniques
- Chat history
- Dark mode
- Online AI API integration

---

## 📌 Conclusion

The FAQ Chatbot demonstrates how basic Natural Language Processing and machine learning techniques can be used to create an interactive question-answering system.

The project uses **TF-IDF and Cosine Similarity** to identify the FAQ that is most similar to the user's question and displays the corresponding answer through a simple graphical interface.

---

## 👨‍💻 Project

**Task:** Task 2 – Chatbot for FAQs

**Organization:** CodeAlpha

**Language:** Python

**Project Type:** Artificial Intelligence / Natural Language Processing