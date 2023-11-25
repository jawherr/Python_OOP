from tkinter import  *
from tkinter import messagebox

master = Tk()
master.geometry('400x400')

def myName():
    messagebox.showinfo('this is title','Hello Muhammed Essa')

btn = Button(master,text='click me',command=myName)
btn.place(x=30,y=70)

lst1 = Listbox(master)
lst1.insert(1,'python')
lst1.insert(2,'java')
lst1.insert(3,'C')
lst1.insert(4,'C++')
lst1.insert(5,'html')
lst1.insert(6,'javascript')
lst1.pack()
master.mainloop()