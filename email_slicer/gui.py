from tkinter import Tk, Label

def gui():
    root = Tk()
    root.title('Email Slicer')
    root.geometry('{}x{}'.format(500, 350))
    root.config(bg="#828282")
    root.resizable(width=False, height=False)

    label = Label(root, text="Enter your e-mail id below.\n The application will extract your username and domain name.", font=("Poppins", 10), justify='center', foreground='white', background='#828282')
    emt_label = Label(root, background="#828282")


    label.pack()

    root.mainloop()