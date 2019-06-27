import tkinter as tk
import tkinter.ttk as ttk


def ukupno():
    u = varPon.get() + varUt.get() + varSr.get() + varCet.get() + varPet.get()
    text = str(u*8) + " sati"
    ukupnoSati.set(text)

def obrisi():
    varPon.set(0)
    varUt.set(0)
    varSr.set(0)
    varCet.set(0)
    varPet.set(0)
    ukupnoSati.set("Ukupno sati")

root = tk.Tk()
workingDaysFrame = ttk.Frame(root, padding="0 0 0 0")
totalFrame = ttk.Frame(root, padding="0 0 0 0")
varPon = tk.IntVar()
varUt = tk.IntVar()
varSr = tk.IntVar()
varCet = tk.IntVar()
varPet = tk.IntVar()
ukupnoSati = tk.StringVar()

pon = ttk.Checkbutton(workingDaysFrame, text="Ponedeljak", variable=varPon)
uto = ttk.Checkbutton(workingDaysFrame, text="Utorak", variable=varUt)
sre = ttk.Checkbutton(workingDaysFrame, text="Sreda", variable=varSr)
cet = ttk.Checkbutton(workingDaysFrame, text="Cetvrtak", variable=varCet)
pet = ttk.Checkbutton(workingDaysFrame, text="Petak", variable=varPet)

ukupnoBtn = ttk.Button(totalFrame, text="Ukupno", command = ukupno)
obrisiBtn= ttk.Button(totalFrame, text="Obrisi", command = obrisi)
prikazUkupno = ttk.Label(totalFrame, text="ukupno dana", textvariable = ukupnoSati)
ukupnoSati.set("Ukupno sati")

workingDaysFrame.pack(side = tk.LEFT, fill=tk.BOTH, expand=True)
totalFrame.pack(side = tk.LEFT, fill=tk.BOTH)
pon.pack(fill=tk.BOTH, expand=True)
uto.pack(fill=tk.BOTH, expand=True)
sre.pack(fill=tk.BOTH, expand=True)
cet.pack(fill=tk.BOTH, expand=True)
pet.pack(fill=tk.BOTH, expand=True)
ukupnoBtn.grid(row=0,column=0)
obrisiBtn.grid(row=1,column=0)
prikazUkupno.grid(row=0,column=1)

root.minsize(100,200)
root.maxsize(300,600)
root.mainloop()