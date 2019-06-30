import tkinter as tk
import tkinter.ttk as ttk


def zero():
    broj.set(broj.get() + '0')

def one():
    broj.set(broj.get() + '1')

def two():
    broj.set(broj.get() + '2')

def three():
    broj.set(broj.get() + '3')

def four():
    broj.set(broj.get() + '4')

def five():
    broj.set(broj.get() + '5')

def six():
    broj.set(broj.get() + '6')

def seven():
    broj.set(broj.get() + '7')

def eight():
    broj.set(broj.get() + '8')

def nine():
    broj.set(broj.get() + '9')

def sum():
    entry2.focus_set()
    a.set(broj.get())
    broj.set("")
    c.set("+")

def sub():
    entry2.focus_set()
    a.set(broj.get())
    broj.set("")
    c.set("-")

def times():
    entry2.focus_set()
    a.set(broj.get())
    broj.set("")
    c.set("*")

def div():
    entry2.focus_set()
    a.set(broj.get())
    broj.set("")
    c.set("/")


def result():
    b.set(broj.get())
    if c.get() == "+":
        total.set(a.get() + b.get())
    elif c.get() == "-":
         total.set(a.get() - b.get())
    elif c.get() == "*":
         total.set(a.get() * b.get())
    elif c.get() == "/":
         total.set(round(a.get() / b.get(),2))

def clear():
    a.set("")
    b.set("")
    total.set("")
    broj.set("")


root = tk.Tk()
root.title("Kalkulator")
style= ttk.Style()
style.configure("I.TButton", foreground="red", background="black", font=("times", 10, "bold"), padding=10)
style.configure("I.TEntry", foreground="green", background="red",padding=5)
style.configure("I.TLabel", foreground="black", font=("times", 12, "bold"))

labelFrame=ttk.Label(root)
entryFrame= ttk.Frame(root, padding=10)
buttonFrame= ttk.Frame(root)

broj=tk.StringVar()
a=tk.IntVar()
a.set("")
b=tk.IntVar()
b.set("")
c=tk.StringVar()
total=tk.StringVar()

label1 = ttk.Label(labelFrame,style="I.TLabel", text="Broj 1:").grid(row=0, column=0, padx=40)
label2 = ttk.Label(labelFrame,style="I.TLabel", text="Broj 2:").grid(row=0, column=1, padx=40)
label3 = ttk.Label(labelFrame,style="I.TLabel", text="Rezultat:").grid(row=0, column=2, padx=40)

entry1 = ttk.Entry(entryFrame, style="I.TEntry",font=("times", 10, "bold"),width=15, textvariable=a)
entry2 = ttk.Entry(entryFrame, style="I.TEntry",font=("times", 10, "bold"),width=15, textvariable=b)
entry3 = ttk.Entry(entryFrame, style="I.TEntry",font=("times", 10, "bold"),width=15, textvariable=total)

button1=ttk.Button(buttonFrame,text="1",style="I.TButton",command=one).grid(row=2,column=0)
button2=ttk.Button(buttonFrame,text="2",style="I.TButton",command=two).grid(row=2,column=1)
button3=ttk.Button(buttonFrame,text="3",style="I.TButton",command=three).grid(row=2,column=2)
button4=ttk.Button(buttonFrame,text="4",style="I.TButton",command=four).grid(row=2,column=3)
button5=ttk.Button(buttonFrame,text="5",style="I.TButton",command=five).grid(row=3,column=0)
button6=ttk.Button(buttonFrame,text="6",style="I.TButton",command=six).grid(row=3,column=1)
button7=ttk.Button(buttonFrame,text="7",style="I.TButton",command=seven).grid(row=3,column=2)
button8=ttk.Button(buttonFrame,text="8",style="I.TButton",command=eight).grid(row=3,column=3)
button9=ttk.Button(buttonFrame,text="9",style="I.TButton",command=nine).grid(row=4,column=0)
button0=ttk.Button(buttonFrame,text="0",style="I.TButton",command=zero).grid(row=4,column=1)
buttonAdd=ttk.Button(buttonFrame,text="+",style="I.TButton",command=sum).grid(row=4,column=2)
buttonSub=ttk.Button(buttonFrame,text="-",style="I.TButton",command=sub).grid(row=4,column=3)
buttonTimes=ttk.Button(buttonFrame,text="x",style="I.TButton",command=times).grid(row=5,column=0)
buttonDiv=ttk.Button(buttonFrame,text="/",style="I.TButton",command=div).grid(row=5,column=1)
buttonClear=ttk.Button(buttonFrame,text="C",style="I.TButton",command=clear).grid(row=5,column=2)
buttonTotal=ttk.Button(buttonFrame,text="=",style="I.TButton",command=result).grid(row=5,column=3)

entry1.grid(row=1, column=0)
entry2.grid(row=1, column=1, padx=10)
entry3.grid(row=1, column=2, padx=20)
labelFrame.pack()
entryFrame.pack()
buttonFrame.pack()

root.mainloop()


