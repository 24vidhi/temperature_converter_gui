from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry("668x234")
root.title("Temperature Calculator")

myFont = font.Font(size=11)
myFont1 = font.Font(size=14)

# to change entered temperature from Celcius to Fahrenheit


def cel_fahren():
    if not e.get():
        print("Enter temperature")
    else:
        res = float(e.get()) * 9/5 + 32
        lbl_text.config(text="Temperature in Fahrenheit is %.2f F" % (res))
        e.set = ""

# to change entered temperature from Fahrenheit to Celcius


def fahren_cel():
    if not e.get():
        print("Please enter temperature")
    else:
        res = (float(e.get()) - 32) * 5/9
        lbl_text.config(text="Temperature in Celcius is %.2f C" % (res))
        e.set = ""

# to clear the entered temperature


def clear():
    e.delete(0, END)


l1 = Label(root, text="Enter the temperature in C or F:", font=("Ariel", 14))
e = Entry(root, width=40, borderwidth=5)

b1 = Button(root, text="Celcius --> Fahrenheit",
            fg='white', bg='blue', command=cel_fahren)
b2 = Button(root, text="Fahrenheit --> Celcius",
            fg='white', bg='blue', command=fahren_cel)
b3 = Button(root, text="Clear", fg='white', bg='blue', command=clear)

b1['font'] = myFont
b2['font'] = myFont
b3['font'] = myFont

lbl_text = Label()
lbl_text.place(x=250, y=150)
lbl_text['font'] = myFont1

l1.place(x=50, y=50)
e.place(x=350, y=50)
b1.place(x=100, y=100)
b2.place(x=300, y=100)
b3.place(x=500, y=100)

root.mainloop()
