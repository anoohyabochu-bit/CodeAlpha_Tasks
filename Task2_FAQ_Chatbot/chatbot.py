import json
import re
import tkinter as tk
from tkinter import scrolledtext

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Load FAQs
# -----------------------------

with open("faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)

questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]


# -----------------------------
# Text preprocessing
# -----------------------------

stop_words = {
    "a", "an", "the", "is", "are", "was", "were",
    "what", "is", "are", "how", "can", "i", "you",
    "do", "does", "of", "to", "in", "on", "for",
    "and", "or", "it", "this", "that", "about"
}


def preprocess(text):
    text = text.lower()

    # Remove punctuation
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Split into words
    words = text.split()

    # Remove common words
    words = [
        word for word in words
        if word not in stop_words
    ]

    return " ".join(words)


# Process FAQ questions
processed_questions = [
    preprocess(question)
    for question in questions
]


# -----------------------------
# TF-IDF
# -----------------------------

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(
    processed_questions
)


# -----------------------------
# Get chatbot response
# -----------------------------

def get_response(user_question):

    processed_input = preprocess(user_question)

    if not processed_input:
        return "Please enter a valid question."

    user_vector = vectorizer.transform(
        [processed_input]
    )

    similarities = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match_index = similarities.argmax()

    best_score = similarities[0][best_match_index]

    if best_score < 0.20:
        return "Sorry, I don't know the answer to that question."

    return answers[best_match_index]


# -----------------------------
# Send message
# -----------------------------

def send_message(event=None):

    user_question = entry_box.get().strip()

    if user_question == "":
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(
        tk.END,
        "You: " + user_question + "\n"
    )

    response = get_response(user_question)

    chat_area.insert(
        tk.END,
        "Bot: " + response + "\n\n"
    )

    chat_area.config(state=tk.DISABLED)

    entry_box.delete(0, tk.END)

    chat_area.see(tk.END)


# -----------------------------
# Clear chat
# -----------------------------

def clear_chat():

    chat_area.config(state=tk.NORMAL)

    chat_area.delete(
        "1.0",
        tk.END
    )

    chat_area.config(state=tk.DISABLED)


# -----------------------------
# GUI
# -----------------------------

window = tk.Tk()

window.title("FAQ Chatbot")

window.geometry("650x600")

window.resizable(False, False)


# Title

title_label = tk.Label(
    window,
    text="🤖 FAQ Chatbot",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=15)


# Chat area

chat_area = scrolledtext.ScrolledText(
    window,
    width=70,
    height=25,
    font=("Arial", 11),
    wrap=tk.WORD
)

chat_area.pack(
    padx=15,
    pady=10
)

chat_area.config(
    state=tk.DISABLED
)


# Input frame

input_frame = tk.Frame(window)

input_frame.pack(
    padx=15,
    pady=10,
    fill=tk.X
)


# Input box

entry_box = tk.Entry(
    input_frame,
    font=("Arial", 13)
)

entry_box.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    ipady=8
)


# Send button

send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 11, "bold"),
    command=send_message
)

send_button.pack(
    side=tk.LEFT,
    padx=5
)


# Clear button

clear_button = tk.Button(
    input_frame,
    text="Clear",
    font=("Arial", 11),
    command=clear_chat
)

clear_button.pack(
    side=tk.LEFT
)


# Enter key

entry_box.bind(
    "<Return>",
    send_message
)


# Welcome message

chat_area.config(
    state=tk.NORMAL
)

chat_area.insert(
    tk.END,
    "Bot: Hello! 👋 Ask me a question about Artificial Intelligence.\n\n"
)

chat_area.config(
    state=tk.DISABLED
)


# Start GUI

window.mainloop()