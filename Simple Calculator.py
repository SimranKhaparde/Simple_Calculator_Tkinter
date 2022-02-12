# Building a Simple Calculator using Tkinter in Python

from tkinter import *

# Setting the GUI Window

root = Tk()
root.title("Simple Calculator")
root.geometry("570x600")
root.resizable(False, False)
root.configure(bg="black")

# Core Logic of the Calculator expression evaluation and working
equation = ""

def clear():
    global equation
    equation = ""
    label_one.config(text=equation)

def show(value):
    global equation
    equation+=value
    label_one.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result=eval(equation)
        except:
            result = "error"
            equation = ""
    label_one.config(text=result)


# Making the result display screen

label_one = Label(root, width=25, height=2, font="arial 30")
label_one.pack()

# Buttons for the Calculator

Button(root, text="C", width=5, height=1, font="arial 30 bold", bg="blue", fg="white",
       command= lambda: clear(), relief=SUNKEN).place(x=10, y=100)
Button(root, text="/", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command= lambda: show("/"), relief=SUNKEN).place(x=150, y=100)
Button(root, text="%", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command= lambda: show("%"), relief=SUNKEN).place(x=290, y=100)
Button(root, text="*", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command=lambda: show("*"), relief=SUNKEN).place(x=430, y=100)



Button(root, text="7", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command= lambda: show("7"), relief=SUNKEN).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command= lambda: show("8"), relief=SUNKEN).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command= lambda: show("9"), relief=SUNKEN).place(x=290, y=200)
Button(root, text="-", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command= lambda: show("-"), relief=SUNKEN).place(x=430, y=200)



Button(root, text="4", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command=lambda: show("4"), relief=SUNKEN).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command= lambda: show("5"), relief=SUNKEN).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command= lambda: show("6"), relief=SUNKEN).place(x=290, y=300)
Button(root, text="+", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command= lambda: show("+"), relief=SUNKEN).place(x=430, y=300)



Button(root, text="1", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command=lambda: show("1"),  relief=SUNKEN).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command=lambda: show("2"), relief=SUNKEN).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command=lambda: show("3"), relief=SUNKEN).place(x=290, y=400)
Button(root, text="0", width=11, height=1, font="arial 30 bold", bg="grey", fg="white",
       command=lambda: show("0"), relief=SUNKEN).place(x=10, y=500)



Button(root, text=".", width=5, height=1, font="arial 30 bold", bg="grey", fg="white",
       command=lambda: show("."), relief=SUNKEN).place(x=290, y=500)
Button(root, text="=", width=5, height=3, font="arial 30 bold", bg="orange", fg="white",
       command=lambda: calculate(), relief=SUNKEN).place(x=430, y=400)

root.mainloop()

