from tkinter import *
import tkinter.ttk as ttk

class Checkbar(ttk.Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []

      for pick in picks:
         var = IntVar()
         chk = ttk.Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)

   def state(self):
        return [var.get() for var in self.vars]


        
if __name__ == '__main__':
   root = Tk()
   lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
   tgl = Checkbar(root, ['English','German','Spain'])
   hoby=Checkbar(root,['Fishing','Football','Hunting','Swimming'])
   lng.pack(side=TOP,  fill=X)
   tgl.pack(side=LEFT)
   lng.config(relief=GROOVE, bd=2)
   hoby.pack(side=BOTTOM )
   def allstates(): 
      print(list(lng.state()), list(tgl.state()))







   
   #*******
   s = ttk.Style()
   
   s.map("ButtonStyle.TButton",foreground=[('pressed', 'red'), ('active', 'blue')],background=[('pressed', '!disabled', 'black'), ('active', 'white')])
   s.configure("ButtonStyle.TButton",padding=6)
   #*****
   ttk.Button(root, text='Quit', style = "ButtonStyle.TButton", command=root.quit).pack(side=RIGHT)
   ttk.Button(root, text='Peek',style = "ButtonStyle.TButton",  command=allstates).pack(side=RIGHT)
   root.mainloop()