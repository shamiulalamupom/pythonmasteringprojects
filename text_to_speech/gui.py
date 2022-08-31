from tkinter import *
from tkinter.ttk import *
import pyttsx3

def gui():
    root = Tk()
    root.title("Text to Speech Application")
    root.geometry("{}x{}".format(395, 400))
    root.resizable(width=False, height=False)
    root.config(bg="#0e1c25")

    engine = pyttsx3.init()

    def text_to_speech():
        text = textbox.get(1.0, END)
        engine.setProperty('rate', 160)
        engine.say(text)
        engine.runAndWait()

    title = Label(root, text="Enter your text here:", font=('Poppins', 14), background="#0e1c25", foreground='white')
    title.place(x=20, y=10)
    textbox = Text(root, width=35, height=10, font=('Poppins', 12), relief=GROOVE, wrap=WORD)
    textbox.place(x=20, y=50)
    submit_btn = Button(root, text="Speak", command=text_to_speech)
    submit_btn.place(x=160, y=355)

    root.mainloop()

# To use Text to Speech copy and paste these lines in main.py:
# from text_to_speech.gui import gui

# gui()