from tkinter import *
from tkinter import ttk

def Sum(numbers):
    global operator
    operator = operator+str(numbers)
    y.set(operator)


root = Tk()
root.title("CALCULATOR")
root.geometry("500x500")
root.config(background="grey")
root.resizable(0,0)
title=Label(root,text = "CALCULATOR")
title.config(font=("",32),background="blue",fg="white")
title.place(relx=0.2,rely=0)

ask = Label(root,text = "Enter the first value: ")
ask.config(font=("",15),background="black",fg="white")
ask.place(relx = 0.0,rely = 0.2)

x = StringVar()
ent1 = Entry(root,textvariable=x)
ent1.config(font=("",15))
ent1.place(relx=0.36,rely=0.2)

tak = Label(root,text = "Enter the second value: ")
tak.config(font=("",15),background="black",fg="white")
tak.place(relx=0.0,rely=0.3)

y= StringVar()
ent2 = Entry(root,textvariable=y)
ent2.config(font=("",15))
ent2.place(relx=0.42,rely=0.3)

ad = Label(root,text = "Choose the operation you want to perform:")
ad.config(font=("",15),background="black",fg="white")
ad.place(relx=0.0,rely=0.4)

rad1 = Button(root,text = "Add",width=15,command=lambda: res.config(font=("",15),text="Output:"+str(int(x.get())+int(y.get()))))
rad1.config(font=("",15))
rad1.place(relx=0.14,rely=0.47)

rad2 = Button(root,text = "Subtract",width=15,command=lambda: res.config(font=("",15),text="Output:"+str(int(x.get())-int(y.get()))))
rad2.config(font=("",15))
rad2.place(relx=0.14,rely=0.55)

rad3 = Button(root,text = "Multiply",width=15,command=lambda: res.config(font=("",15),text="Output:"+str(int(x.get())*int(y.get()))))
rad3.config(font=("",15))
rad3.place(relx=0.14,rely=0.63)

rad4 = Button(root,text = "Division",width=15,command=lambda: res.config(font=("",15),text="Output:"+str(int(x.get())/int(y.get()))))
rad4.config(font=("",15))
rad4.place(relx=0.14,rely=0.71)

res = Label(root,text="Output:")
res.config(font=("",15))
res.place(relx=0.0,rely=0.8)

root.mainloop()