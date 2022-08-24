from tkinter import *

def gui():
    root = Tk()
    root.geometry('{}x{}'.format(600, 400))
    root.resizable(width=False, height=False)
    root.config(bg="#828282")
    root.title("Website Blocker")

    h = Label(root, text="Simple Website Blocker", font=('Poppins', 18), background="#828282", foreground="white")
    h.pack()
    emt_label0 = Label(background="#828282")
    emt_label0.pack()

    host_path = "C:\Windows\System32\drivers\etc\hosts"
    ip_address = "192.168.0.104"

    def block():
        website_links = enter_web_address.get(1.0, END)
        website = list(website_links.split(","))
        with open(host_path, '+r') as host_file:
            file_content = host_file.readlines()
        for web in website:
            if web in file_content:
                display = Label(root, text=f"This site is already blocked --> {web}", font=("Poppins", 12), foreground="white", background="#828282")
                display.pack()
                pass
            else:
                host_file.write(ip_address + " " + web + "\n")
                Label(root, text=f"This site is blocked --> {web}", font=('Poppins', 18), foreground="white", background="#828282").pack()

    def unblock():
        website_links = enter_web_address.get(1.0, END)
        website = list(website_links.split(","))
        with open(host_path, '+r') as host_file:
            file_content = host_file.readlines()
        for web in website:
            with open (host_path , 'r+') as f:
                for line in file_content:
                    if line.strip(',') != website_links:
                        f.write(line)
                        Label(root, text="UnBlocked", font='Poppins', foreground="white", background="#828282").pack()
                        pass
                    else:
                        display=Label(root, text='Already UnBlocked' , font='Poppins', foreground="white", background="#828282")
                        display.pack()

    entry_label = Label(root, text='Enter Website Below', font=('Poppins', 12), background="#828282", foreground="white")
    entry_label.pack()
    enter_web_address = Text(root, font=('Poppins', 12), height='2', width='40', background="white", foreground="black")
    enter_web_address.pack()
    emt_label1 = Label(background="#828282")
    emt_label1.pack()

    block_button = Button(text="Block", font=('Poppins', 12), width=10, command=block, foreground="white", background="#828282")
    block_button.pack()
    emt_label2 = Label(background="#828282")
    emt_label2.pack()

    unblock_button = Button(text="Unblock", font=('Poppins', 12), width=10, command=unblock, foreground="white", background="#828282")
    unblock_button.pack()

    root.mainloop()