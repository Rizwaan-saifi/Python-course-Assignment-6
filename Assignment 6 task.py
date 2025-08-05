from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("350x600")



entry = Entry(window, width=45, borderwidth=9, bg="black",fg="white")
entry.place(x=0, y=0)

def button_clicked(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))


b=Button(window,text="1", width=11, height='4', bg="#2d2d30", fg="white",command=lambda: button_clicked(1))
b.place(x=10, y=60)

b=Button(window,text="2", width=11, height='4', bg="#2d2d30", fg ='white', command=lambda: button_clicked(2))
b.place(x=107, y=60)

b=Button(window,text="3", width=11, height='4',bg="#2d2d30", fg ='white', command=lambda: button_clicked(3))
b.place(x=204, y=60)

b=Button(window,text="4", width=11, height='4',bg="#2d2d30", fg ='white', command=lambda: button_clicked(4))
b.place(x=10, y=149)

b=Button(window,text="5", width=11, height='4',bg="#2d2d30", fg ='white', command=lambda: button_clicked(5))
b.place(x=107, y=149)

b=Button(window,text="6", width=11, height='4',bg="#2d2d30", fg ='white', command=lambda: button_clicked(6))
b.place(x=204, y=149)

b=Button(window,text="7", width=11,height='4',bg="#2d2d30", fg ='white', command=lambda: button_clicked(7))
b.place(x=10, y=238)

b=Button(window,text="8", width=11, height='4',bg="#2d2d30", fg ='white', command=lambda: button_clicked(8))
b.place(x=107, y=238)

b=Button(window,text="9", width=11, height='4',bg="#2d2d30", fg ='white', command=lambda: button_clicked(9))
b.place(x=204, y=238)

b=Button(window,text="0", width=11, height='4',bg="#2d2d30", fg ='white', command=lambda: button_clicked(0))
b.place(x=10, y=329)

# oprators

def add():
    n1=entry.get()
    global math
    math="addition"
    global i
    i=int(n1)
    entry.delete(0, END)

b=Button(window,text="+", width=11, height='4',bg="#2d2d30", fg ='white', command=add)
b.place(x=107, y=329)

def sub():
    n1=entry.get()
    global math
    math="subtraction"
    global i
    i=int(n1)
    entry.delete(0, END)

b=Button(window,text="-", width=11, height='4',bg="#2d2d30", fg ='white', command=sub)
b.place(x=204, y=329)

def mult():
    n1=entry.get()
    global math
    math="multiplication"
    global i
    i=int(n1)
    entry.delete(0, END)

b=Button(window,text="*", width=11, height='4',bg="#2d2d30", fg ='white', command=mult)
b.place(x=10, y=415)

def div():
    n1=entry.get()
    global math
    math="division"
    global i
    i=int(n1)
    entry.delete(0, END)

b=Button(window,text="/", width=11, height='4',bg="#2d2d30", fg ='white', command=div)
b.place(x=107, y=415)

def equal():
    n2=entry.get()
    entry.delete(0, END)
    if math=="addition":
        entry.insert(0,i+int(n2) )
    elif math=="subtraction":
        entry.insert(0,i-int(n2))
    elif math=="multiplication":
            entry.insert(0,i*int(n2))
    elif math=="division":
        entry.insert(0,i/int(n2))

b=Button(window,text="=", width=11, height='4',bg="#2d2d30", fg ='white', command=equal)
b.place(x=204, y=415)
# b.place(x=170, y=300)

def clear():
    entry.delete(0, END)

b=Button(window,text="clear", width=39, height='4',bg="#2d2d30", fg ='white', command=clear)
b.place(x=10, y=490)

mainloop()