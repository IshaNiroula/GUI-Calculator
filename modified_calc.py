from tkinter import *
from tkinter import ttk

operator = ""
def no(numbers):
    global operator
    operator = operator + str(numbers)
    a.set(operator)

def equals_to():
    global operator
    w = str(eval(operator))
    a.set(w)
    operator = " "

def clear():
    global operator
    operator=""
    a.set(" ")

root = Tk()
root.title("Calculator")
root.config(background="black")


a = StringVar()

root.geometry("528x445")
root.resizable(0,0)
display = Entry(root,font=("",20),textvariable=a,background="White",bd=30).grid(rowspan=2,columnspan=4)
btn1 = Button(root,text="1",fg="blue",font=("",10),bd=8,width=10,padx=16,pady=16,command=lambda: no(1)).grid(row=3,column=0)
btn2 = Button(root,text="2",fg="blue",font=("",10),bd=8,width=10,padx=16,pady=16,command=lambda: no(2)).grid(row=3,column=1)
btn3 = Button(root,text="3",fg="blue",font=("",10),bd=8,width=10,padx=16,pady=16,command=lambda: no(3)).grid(row=3,column=2)
clr = Button(root,text="C",font=("",10),width=10,bd=8,background="red",fg="black",padx=16,pady=16,command = lambda: clear(),).grid(row=2,column=3)

btn4 = Button(root,text="4",fg="blue",font=("",10),bd=8,width=10,padx=16,pady=16,command = lambda: no(4)).grid(row=4,column=0)
btn5 = Button(root,text="5",fg="blue",font=("",10),bd=8,width=10,padx=16,pady=16,command = lambda: no(5)).grid(row=4,column=1)
btn6 = Button(root,text="6",fg="blue",font=("",10),bd=8,width=10,padx=16,pady=16,command= lambda: no(6)).grid(row=4,column=2)
add = Button(root,text="+",font=("",10),background="white",fg="black",width=10,bd=8,padx=16,pady=16,command = lambda: no("+")).grid(row=3,column=3)

btn7 = Button(root,text="7",fg="blue",font=("",10),width=10,bd=8,padx=16,pady=16,command = lambda: no(7)).grid(row=5,column=0)
btn8 = Button(root,text="8",fg="blue",font=("",10),width=10,bd=8,padx=16,pady=16,command = lambda: no(8)).grid(row=5,column=1)
btn9 = Button(root,text="9",fg="blue",font=("",10),width=10,bd=8,padx=16,pady=16,command= lambda : no(9)).grid(row=5,column=2)
sub = Button(root,text="-",font=("",10),bd=8,background="white",fg="black",width=10,padx=16,pady=16,command = lambda: no("-")).grid(row=4,column=3)

btna = Button(root,text="0",fg="blue",bd=8,font=("",10),width=10,padx=16,pady=16,command = lambda: no(0)).grid(row=6,column=0)
pro = Button(root,text="*",font=("",10),bd=8,background="white",fg="black",width=10,padx=16,pady=16,command = lambda: no("*")).grid(row=5,column=3)
div = Button(root,text="/",font=("",10),bd=8,background="white",fg="black",width=10,padx=16,pady=16,command = lambda: no("/")).grid(row=6,column=2)
pt = Button(root,text=".",font=("",10),bd=8,background="white",fg="black",width=10,padx=16,pady=16,command = lambda: no(".")).grid(row=6,column=1)
eq = Button(root,text="=",font=("",10),bd=8,background="white",fg="black",width=10,padx=16,pady=16,command = lambda: equals_to(),).grid(row=6,column=3)

root.mainloop()