from tkinter import  *
from tkinter import messagebox

master = Tk()
master.geometry('400x400')

def myName():
    messagebox.showinfo('this is title','Hello Muhammed Essa')

btn = Button(master,text='click me',command=myName)
btn.place(x=100,y=70)

master.mainloop()