import tkinter as tk
import tkinter.ttk as ttk

def shoping():
    global vars
    articals = articalsVar.get().split(",")
    for widget in articalsListFrame.winfo_children():
        widget.destroy()
    for artical in articals:
        var = tk.IntVar()
        vars.append(var)
        x = ttk.Checkbutton(articalsListFrame, text=artical, variable=var)
        x.pack(side=tk.LEFT)
vars=[]
root = tk.Tk()
articalsEntryFrame = ttk.Frame(root, padding="0 0 0 0")
articalsListFrame = ttk.Frame(root, padding="0 0 0 0")
articalsVar = tk.StringVar()
articalsInfo = ttk.Label(articalsEntryFrame,text="Unesite artikle razmaknute zarezom")
articalsEntry = ttk.Entry(articalsEntryFrame,textvariable=articalsVar)
shop = ttk.Button(articalsEntryFrame, text="Shop", command=shoping)


articalsEntryFrame.pack()
articalsListFrame.pack()
articalsInfo.pack(side=tk.LEFT)
articalsEntry.pack(side=tk.LEFT)
shop.pack(side=tk.LEFT)

articalsEntry.focus_set()
root.mainloop()