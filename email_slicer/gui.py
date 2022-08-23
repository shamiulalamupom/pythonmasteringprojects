from tkinter import *

def gui():
    root = Tk()
    root.title('Email Slicer')
    root.geometry('{}x{}'.format(500, 380))
    root.config(bg="#828282")
    root.resizable(width=False, height=False)

    def result():
        try:
            email = entry.get()
            full_email = email.strip()
            username = full_email[0:full_email.index('@')]
            domain = full_email[full_email.index('@') + 1:]
            result_box.delete("1.0", END)
            msg = f'E-mail entered was: {email}\nYour e-mail username is {username}\nYour e-mail domain us {domain}'
            result_box.insert(END, msg)
            entry.delete(0, END)

        except:
            result_box.delete("1.0", END)
            result_box.insert(END, 'ERROR!!!')

    def reset():
        result_box.delete("1.0", END)
        entry.delete(0, END)

    label = Label(root, text="Enter your e-mail id below\n The application will extract your username and domain name", font=("Poppins", 10), justify='center', foreground='white', background='#828282')
    entry_label = Label(root, text="Enter your e-mail ID", foreground="white", background="#828282", font=("Poppins", 10), justify="center")
    result_label = Label(root, text="Result", foreground="white", background="#828282", font=("Poppins", 10), justify="center")
    emt_label0 = Label(root, background="#828282")
    emt_label1 = Label(root, background="#828282")
    emt_label2 = Label(root, background="#828282")
    emt_label3 = Label(root, background="#828282")
    emt_label4 = Label(root, background="#828282")

    entry_var = StringVar()
    entry = Entry(font=(11), width=50, justify='center', textvariable=entry_var)

    result_box = Text(height=5, width=50)

    submit_btn = Button(text="Submit", command=result, font=(11), bd=0, bg="green")
    reset_btn = Button(text="Reset", command=reset, font=(11), bd=0, bg="red")

    emt_label0.pack()
    label.pack()
    emt_label1.pack()
    entry_label.pack()
    entry.pack()
    emt_label3.pack()
    submit_btn.pack()
    emt_label2.pack()
    reset_btn.pack()
    emt_label4.pack()
    result_label.pack()
    result_box.pack()

    root.mainloop()

# To start the program:(copy and paste it in the main.py)
# from email_slicer.gui import gui

# gui()