from tkinter import *
import tkinter.ttk as ttk

class Anketa(ttk.Frame):
   def __init__(self,labela, labela2, entry, button, side=LEFT, anchor=E):
      Frame.__init__(self, bd=20)
      self.labela = labela
      self.labela2=labela2
      self.entry = entry
      self.button = button
      lb = ttk.Label(self,text=labela,font=('times',30,"italic"))
      lb2 = ttk.Label(self, text=labela2, font=('times', 10, "italic"))
      lb.pack(padx=20,side=side)
      lb2.pack(padx=30,anchor=anchor)
      self.en = StringVar()
      ent = ttk.Entry(self,textvariable=self.en)
      ent.pack(side=RIGHT,padx=10,pady=5)

   def name(self):
      return(self.en.get())

class Checkbar(ttk.Frame):
   def __init__(self,parent=None, picks=[],category="", side=LEFT, anchor=W):
      Frame.__init__(self,parent, relief=GROOVE, bd=5,)
      self.vars = []
      self.picks = picks
      self.category = category
      kat= ttk.Label(self, text=category)
      kat.pack(side=TOP,pady=30)
      for i in enumerate(picks,1):
         var = IntVar()
         chk = ttk.Checkbutton(self, text=i, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
        return [var.get() for var in self.vars]
   def stateRepresent(self):
      picked = [p[0] for p in list(zip(self.picks,self.vars)) if p[1].get()==1]
      return picked

if __name__ == '__main__':
   root = Tk()
   naslov = Anketa("Anketa","Ime i Prezime:","Unos","Submit",)
   tv = Checkbar(root, ['Pink', 'StudioB', 'RTS1', 'Prva','O2'],"Izaberite Tv Kanal:")
   op = Checkbar(root, ['Mts','SBB','Vector','Kopernikus','Orion'],"Izaberite TV Operatera:")
   dani = Checkbar(root, ['Ponedeljak', 'Utorak', 'Sreda','Cetvrtak','Petak','Subota','Nedelja'],"Izaberite dan:")
   naslov.grid(row=0,column=0,sticky=W+N+E+S)
   tv.grid(row=1,column=0,sticky=W+N+E+S)
   op.grid(row=3,column=0,sticky=W+N+E+S)
   dani.grid(row=5,column=0,sticky=W+N+E+S)

   def allstates():
      print(naslov.name())
      print(list(tv.state()), list(op.state()),list(dani.state()))
      lb1 = Label(root, text="Izabrali ste: " + str(Checkbar.stateRepresent(tv)))
      lb2 = Label(root, text="Izabrali ste: " + str(Checkbar.stateRepresent(op)))
      lb3 = Label(root, text="Izabrali ste: " + str(Checkbar.stateRepresent(dani)))
      lb1.grid(row=2,column=0)
      lb2.grid(row=4,column=0)
      lb3.grid(row=6,column=0)


   s = ttk.Style()
   s.map("ButtonStyle.TButton", foreground=[('pressed', 'red'), ('active', 'blue')],
         background=[('pressed', '!disabled', 'black'), ('active', 'white')])
   s.configure("ButtonStyle.TButton", padding=6)

   ttk.Button(root, text='Submit', style="ButtonStyle.TButton", command=allstates).grid(sticky=E+S)

   root.mainloop()