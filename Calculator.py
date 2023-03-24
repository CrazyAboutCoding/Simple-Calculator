from tkinter import*
import tkinter.messagebox
top=Tk()
def message():
    tkinter.messagebox.showinfo("Hello", "You are going to rock this world!")
button=Button(text="Hello", command=message)
button.pack()
