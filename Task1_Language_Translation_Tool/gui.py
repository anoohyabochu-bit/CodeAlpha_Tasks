import tkinter as tk
from tkinter import ttk, messagebox

from deep_translator import GoogleTranslator
from app import translate_text

import pyperclip
from gtts import gTTS
from playsound import playsound
import os

# Automatically loads all languages supported by Google Translate
languages = GoogleTranslator().get_supported_languages(as_dict=True)

language_names = sorted(languages.keys())

root = tk.Tk()

root.title("Google Language Translator")

root.geometry("850x650")

root.config(bg="white")

title = tk.Label(
    root,
    text="Google Language Translator",
    font=("Arial",22,"bold"),
    bg="white",
    fg="blue"
)

title.pack(pady=10)

tk.Label(root,text="Enter Text",bg="white").pack()

input_box = tk.Text(root,height=8,width=90)
input_box.pack()

frame = tk.Frame(root,bg="white")
frame.pack(pady=10)

tk.Label(frame,text="Source").grid(row=0,column=0)

source = ttk.Combobox(
    frame,
    values=language_names,
    width=30,
    state="readonly"
)

source.set("english")

source.grid(row=0,column=1,padx=10)

tk.Label(frame,text="Target").grid(row=0,column=2)

target = ttk.Combobox(
    frame,
    values=language_names,
    width=30,
    state="readonly"
)

target.set("hindi")

target.grid(row=0,column=3,padx=10)

tk.Label(root,text="Translated Text",bg="white").pack()

output_box = tk.Text(root,height=8,width=90)
output_box.pack()


def translate():

    text = input_box.get("1.0","end").strip()

    src = languages[source.get()]

    tgt = languages[target.get()]

    result = translate_text(text,src,tgt)

    output_box.delete("1.0","end")

    output_box.insert("end",result)


def copy():

    pyperclip.copy(output_box.get("1.0","end"))

    messagebox.showinfo("Copied","Text copied successfully")


def speak():

    text = output_box.get("1.0","end").strip()

    if text=="":

        return

    lang = languages[target.get()]

    try:

        tts = gTTS(text=text,lang=lang)

        tts.save("voice.mp3")

        playsound("voice.mp3")

        os.remove("voice.mp3")

    except:

        messagebox.showerror(
            "Error",
            "Speech not supported for this language."
        )


button_frame = tk.Frame(root,bg="white")

button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Translate",
    bg="green",
    fg="white",
    width=18,
    command=translate
).grid(row=0,column=0,padx=10)

tk.Button(
    button_frame,
    text="Copy",
    bg="blue",
    fg="white",
    width=18,
    command=copy
).grid(row=0,column=1,padx=10)

tk.Button(
    button_frame,
    text="Speak",
    bg="orange",
    fg="white",
    width=18,
    command=speak
).grid(row=0,column=2,padx=10)

root.mainloop()