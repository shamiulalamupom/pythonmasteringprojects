import time
from tkinter import *
from tkinter import messagebox

def gui():
    root = Tk()
    root.title('Alarm Clock')
    root.geometry('{}x{}'.format(450, 350))

    hour = StringVar()
    minute = StringVar()
    second = StringVar()

    hour.set('00')
    minute.set('00')
    second.set('00')

    hourEntry= Entry(root, width=3, font=("Poppins", 18, ""), textvariable=hour)
    hourEntry.place(x=150,y=40)
    minuteEntry= Entry(root, width=3, font=("Poppins", 18, ""), textvariable=minute)
    minuteEntry.place(x=200,y=40)
    secondEntry= Entry(root, width=3, font=("Poppins", 18, ""), textvariable=second)
    secondEntry.place(x=250,y=40)

    def submit():
        try:
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print('Please input valid time.')
        
        while temp > -1:
            mins, secs = divmod(temp, 60)
            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)

            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            root.update()
            time.sleep(1)

            if temp == 0:
                messagebox.showinfo("", "Time's up!")

            temp -= 1
    btn = Button(root, text='Set Time', bd='5', command=submit)
    btn.place(x=200, y=120)

    root.mainloop()

# To start the clock:(copy and paste it in the main.py)
# from count_timer import gui
#
# gui.gui()