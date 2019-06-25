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

    def __init__ (self, ime, prezime, jmbg, pol, odeljenje):
        self.odeljenje=odeljenje
        self.ocene={}
        super().__init__(ime, prezime, jmbg, pol)
        
    def dodajOcenu(self, predmet, ocena):
        if predmet in self.ocene.keys():
            self.ocene[predmet].append(ocena)
        else:
            self.ocene[predmet]=[ocena]
            
    def zakljuciOcenu(self,predmet):
        ocena = sum(self.ocene[predmet])/len(self.ocene[predmet])
        if ocena<1.5:
            return 1
        elif 1.5<=ocena<2.5:
            return 2
        elif 2.5<=ocena<3.5:
            return 3
        elif 3.5<=ocena<4.5:
            return 4
        elif 4.5<=ocena:
            return 5

    def zakljuciOcene(self):
        zakljuceneOcene={}
        for k in self.ocene.keys():
            ocena=self.zakljuciOcenu(k)
            zakljuceneOcene[k]=ocena
        return zakljuceneOcene
        
    def opstiUspeh(self):
        ocene=self.zakljuciOcene()
        return sum(ocene.values())/len(ocene.values())
        
        
        
class Zaposleni(Osoba):
    def __init__(self, ime, prezime, jmbg, pol, plata, godineStaza, godinaPenzija):
        self.plata=plata
        self.godineStaza=godineStaza
        self.godinaPenzija=godinaPenzija
        super().__init__(ime, prezime, jmbg, pol)
        
    def godineDoPenzije(self, godina=datetime.datetime.now().year):
        starost=self.StarostGodine(godina)
        doPenzije = self.godinaPenzija-starost 
        if doPenzije<0:
            return 0
        else:
            return doPenzije
    
    
        