import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

style = ttk.Style()
style.configure("BW.TButton", foreground="black", background="white",
                padding=20, relief="flat")
for x in range(10):
    b=ttk.Button(text=x, style="BW.TButton").pack()

root.mainloop()