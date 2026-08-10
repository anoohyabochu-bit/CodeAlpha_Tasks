# AI Language Translation Tool

## Project Description

The AI Language Translation Tool is a Python-based desktop application that translates text from one language to another using Google Translate. It provides a simple graphical user interface (GUI) where users can enter text, choose source and target languages, and get instant translations.

The application also includes:
- Copy translated text to clipboard
- Text-to-Speech (TTS) for translated text
- Support for 100+ languages
- Easy-to-use Tkinter interface

---

## Features

- Translate text between 100+ languages
- User-friendly GUI using Tkinter
- Source and Target language selection
- Copy translated text
- Text-to-Speech using Google Text-to-Speech (gTTS)
- Beginner-friendly project

---

## Technologies Used

- Python 3
- Tkinter
- deep-translator (Google Translate)
- gTTS
- pyperclip
- playsound

---

## Project Structure

```
LanguageTranslator/
│
├── app.py
├── gui.py
├── requirements.txt
└── README.md
```

---

## Installation

### Step 1: Clone or Download the Project

Download the project and open it in Visual Studio Code.

### Step 2: Install Required Packages

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install deep-translator pyperclip gtts playsound==1.2.2
```

---

## Run the Project

Open the terminal and run:

```bash
python gui.py
```

---

## How to Use

1. Enter text in the input box.
2. Select the source language.
3. Select the target language.
4. Click the **Translate** button.
5. The translated text will appear in the output box.
6. Click **Copy** to copy the translated text.
7. Click **Speak** to hear the translated text.

---

## Sample Translation

Input:

```
Hello, how are you?
```

Source Language:

```
English
```

Target Language:

```
Hindi
```

Output:

```
नमस्ते, आप कैसे हैं?
```

---

## Future Improvements

- Voice Input
- Speech-to-Text
- Dark Mode
- Translation History
- Save Translation to File
- Offline Translation
- OCR Image Translation

---

## Author

Name: Bochu Anoohya

Course: Artificial Intelligence

Project: AI Language Translation Tool

Year: 2026

---

## License

This project is developed for educational purposes only.