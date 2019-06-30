from tkinter import *
import tkinter.ttk as ttk

class Checkbar(ttk.Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      self.picks=picks
      for pick in picks:
         var = IntVar()
         chk = ttk.Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
        return [var.get() for var in self.vars]
   def stateRepresent(self):
      picked = [p[0] for p in list(zip(self.picks,self.vars)) if p[1].get()==1]
      return picked
if __name__ == '__main__':
   root = Tk()
   lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
   tgl = Checkbar(root, ['English','German','Spain'])
   hobi = Checkbar(root, ['Sport', 'Muzika', 'Pecanje'])
   lng.pack(side=TOP,  fill=X)
   tgl.pack(side=TOP,fill=X)
   hobi.pack(side=TOP,fill=X)
   lng.config(relief=GROOVE, bd=2)
   tgl.config(relief=GROOVE, bd=2)
   hobi.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()), list(tgl.state()))
      print(Checkbar.stateRepresent(lng),Checkbar.stateRepresent(tgl),Checkbar.stateRepresent(hobi))
      lb1= Label(root,text="Izabrali ste: " + str(Checkbar.stateRepresent(lng)))
      lb2 = Label(root, text="Izabrali ste: " + str(Checkbar.stateRepresent(tgl)))
      lb3 = Label(root, text="Izabrali ste: " + str(Checkbar.stateRepresent(hobi)))
      lb1.pack(side=RIGHT)
      lb2.pack(side=RIGHT)
      lb3.pack(side=RIGHT)
   #*******
   s = ttk.Style()
   
   s.map("ButtonStyle.TButton",foreground=[('pressed', 'red'), ('active', 'blue')],background=[('pressed', '!disabled', 'black'), ('active', 'white')])
   s.configure("ButtonStyle.TButton",padding=6)
   #*****
   ttk.Button(root, text='Quit', style = "ButtonStyle.TButton", command=root.quit).pack(side=RIGHT)
   ttk.Button(root, text='Peek',style = "ButtonStyle.TButton",  command=allstates).pack(side=RIGHT)
   root.mainloop()