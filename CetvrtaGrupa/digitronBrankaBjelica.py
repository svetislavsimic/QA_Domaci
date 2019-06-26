import tkinter as tk
import tkinter.ttk as ttk

expression = ""

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)


def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set("error")
		expression = ""


def clear():
	global expression
	expression = ""
	equation.set("")


if __name__ == "__main__":
	root = tk.Tk()
	root.configure(background="pale green")
	root.title("Calculator")
	equation = tk.StringVar()

	style=ttk.Style()
	style.configure("B.TButton", font=("Cambria", 12, "bold"), foreground="dark green", background="pale green", padding=6, relief="flat", width=10)
	style.configure("B.TLabel", font=("Cambria", 22, "bold"), foreground="dark green", background="pale green", padding=20, width=60, relief="flat")

	tk.Grid.rowconfigure(root, 0, weight=1)
	tk.Grid.rowconfigure(root, 1, weight=1)
	tk.Grid.rowconfigure(root, 2, weight=1)
	tk.Grid.rowconfigure(root, 3, weight=1)
	tk.Grid.rowconfigure(root, 4, weight=1)
	tk.Grid.columnconfigure(root, 0, weight=1)
	tk.Grid.columnconfigure(root, 1, weight=1)
	tk.Grid.columnconfigure(root, 2, weight=1)
	tk.Grid.columnconfigure(root, 3, weight=1)

	entry=ttk.Entry(root, style="B.TLabel", textvariable=equation)
	entry.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
	equation.set("")

	c=ttk.Button(root, text="Clear",style="B.TButton", command=clear)
	c.grid(column=3, row=0, sticky=tk.NSEW)

	frame=tk.Frame(root)
	frame.grid(row=5, column=4, sticky=tk.NSEW)


	btnList = ['7','8','9','*','4','5','6','+','1','2','3','-','0','.','/',"=",]
	r=1
	c=0
	for b in btnList:
		cmd = lambda x=b: press(x)
		if b=="=":
			x=ttk.Button(root, text=b, style="B.TButton", command=equalpress).grid(row=r, column=c, sticky=tk.NSEW)
		else:
			x=ttk.Button(root, text=b, style="B.TButton", command=cmd).grid(row=r, column=c, sticky=tk.NSEW)
		c += 1
		if c > 3:
			c = 0
			r += 1

	root.mainloop()