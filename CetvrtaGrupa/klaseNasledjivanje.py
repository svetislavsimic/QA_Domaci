from enum import Enum

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
        