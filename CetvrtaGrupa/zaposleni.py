from enum import Enum
import datetime

class Pol(Enum):
    MUSKI=1
    ZENSKI=2
    
class Predmet(Enum):
    MATEMATIKA=1
    SRPSKI=2
    HEMIJA=3    
    
class Osoba:
    def __init__(self,ime, prezime, jmbg, pol):
        self.ime=ime
        self.prezime=prezime
        self.jmbg=jmbg
        self.pol=pol

def godinaRodjenja(self):
    god=self.jmbg[4:7]
    if god[0]=='9':
        god="1"+god
    else:
        god="2"+god
    return int(god)

def StarostGodine(self, godina):
    starost=godina-self.godinaRodjenja()
    if starost<0:
        return 0
    else:
        return starost

def __repr__(self):
    return self.ime + " " + self.prezime

class Ucenik(Osoba):

   def __init__(self, ime, prezime, jmbg, pol, odeljenje):
       #self.ime = ime
       #self.prezime = prezime
       #self.jmbg = jmbg
       #self.pol = pol
       # jer nasledjuje klasu Osoba, nema potrebe da se opet kucaju ove linije

       self.odeljenje = odeljenje
       self.ocene={}
       super().__init__(ime, prezime, jmbg, pol)

def dodajOcenu(self, predmet, ocena):
        if predmet in self.ocene.keys():
            self.ocene[predmet].append(ocena)
        else:
            self.ocene[predmet]=[ocena]

ucenici=[]
nastavi="y"

while nastavi=="y":
    ime=input("Unesite ime ucenika: ")
    prezime=input("Unesite prezime ucenika: ")
    jmbg=input("Unesite JMBG ucenika: ")

    uspesnoUnetPol=False
    while uspesnoUnetPol==False:
        pol=input("Unesite pol ucenika: m-z ")
        if pol.lower()=="m":
            pol=Pol.MUSKI
            uspesnoUnetPol=True
        elif pol.lower()=="z":
            pol=Pol.ZENSKI
            uspesnoUnetPol=True
        else:
            print("Uneli ste nepostojeci pol! ")

    odeljenje=input("Unesite odeljenje: ")
    ucenici.append(Ucenik(ime=ime, prezime=prezime, jmbg=jmbg, pol=pol, odeljenje=odeljenje))
    nastavi=input("Za dalji unos ucenika pritisnite 'y' ")

print(ucenici)

class Zaposleni:
    def __init__ (self, ime, prezime, jmbg, pol, plata, godineStaza, godinaPenzija):
        #self.ime=ime
        #self.prezime=prezime
        #self.jmbg=jmbg
        #self.pol=pol
        self.plata=plata
        self.godineStaza=godineStaza
        self.godina.Penzija=godinaPenzija
        super().__init__(ime, prezime, jmbg, pol)

    def godineDoPenzije(self, godina=datetime.datetime.now().year):
        starost=self.StarostGodine(godina)
        doPenzije = self.godinaPenzija-starost
        if doPenzije<0:
            return 0
        else:
            return doPenzije


zaposleni=[]
nastavi="y"

while nastavi=="y":
    ime=input("Unesite ime zaposlenog: ")
    prezime=input("Unesite prezime zaposlenog: ")
    jmbg=input("Unesite JMBG zaposlenog: ")

    uspesnoUnetPol=False
    while uspesnoUnetPol==False:
        pol=input("Unesite pol zaposlenog: m-z ")
        if pol.lower()=="m":
            pol=Pol.MUSKI
            uspesnoUnetPol=True
        elif pol.lower()=="z":
            pol=Pol.ZENSKI
            uspesnoUnetPol=True
        else:
            print("Uneli ste nepostojeci pol! ")

    plata=input("Unesite iznos plate: ")
