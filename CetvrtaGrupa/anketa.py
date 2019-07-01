from tkinter import *
import tkinter.ttk as ttk

class Checkbar2(ttk.Frame):
   def __init__(self, parent=None,categoryName="", picks=[], side=LEFT, anchor=CENTER):
      Frame.__init__(self, parent)
      self.vars = []
      self.imeKategorije = ttk.Label(self, text="Kategorija:      {0}".format(categoryName))
      self.imeKategorije.pack()
      for pick in picks:
         var = IntVar()
         chk = ttk.Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)

   def state(self):
        return [var.get() for var in self.vars]


if __name__ == '__main__':
   root = Tk()
   root.minsize(500,500)
   root.maxsize(700,800)
   firstFrame=ttk.Frame(root)
   secondFrame=ttk.Frame(root)
   natpisNazivAnkete=ttk.Label(firstFrame,text="Naziv ankete :")
   entyNazivAnkete=ttk.Entry(firstFrame)
   firstFrame.pack(side=TOP)
   secondFrame.pack(pady=50,fill=BOTH)
   natpisNazivAnkete.pack(side=LEFT)
   entyNazivAnkete.pack(side=LEFT)
   kanali = Checkbar2(secondFrame,"TV Kanali", ['RTS', 'PINK', 'Studio B', 'N1'])
   kanali.pack(fill=X)
   operateri=Checkbar2(secondFrame,"TV Operater", ["Kopernikus","SBB", "MTS" ,"OpenTV"])
   operateri.pack(pady=30,fill=X)



   # *******
   s = ttk.Style()

   s.map("ButtonStyle.TButton", foreground=[('pressed', 'red'), ('active', 'blue')],
         background=[('pressed', '!disabled', 'black'), ('active', 'white')])
   s.configure("ButtonStyle.TButton", padding=6)
   # *****
   komandeFrame=ttk.Frame(root)
   komandeFrame.pack(side=BOTTOM,pady=10)
   ttk.Button(komandeFrame, text='Quit', style="ButtonStyle.TButton", command=root.quit).pack(side=RIGHT)
   ttk.Button(komandeFrame, text='Submit', style="ButtonStyle.TButton", command="").pack(side=RIGHT)
   root.mainloop()


