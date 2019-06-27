import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

root.title("Lista brojeva")

style = ttk.Style()
style.configure("BW.TButton", foreground="black", background="white",
                padding=10, relief="flat", activebackground="yellow")

style.map('BW.TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'red')])
for x in range(10):
    b=ttk.Button(text=x, style="BW.TButton", ).pack()


root.mainloop()