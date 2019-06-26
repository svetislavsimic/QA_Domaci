import tkinter as tk
from tkinter import messagebox


def pozdrav():
    ime = nameVar.get()
    textPozdrava = "Zdravo " + ime
    messagebox.showinfo("Pozdrav ",textPozdrava)
    nameVar.set("")



root=tk.Tk()
nameVar = tk.StringVar()
entryIme = tk.Entry(root, textvariable=nameVar)
ok = tk.Button(root,text="OK", command = pozdrav)

entryIme.pack()
ok.pack()
root.mainloop()