class Osoba:
    def __init__(self, ime, prezime, jmbg):
        self.ime=ime
        self.prezime=prezime
        self.jmbg=jmbg
        
    def inicijali(self):
        return self.ime[0]+ " " + self.prezime[0]
        
    def prettify(self):
        return self.ime.capitalize()+ " " + self.prezime.capitalize()
        
    def istiInicijali(self):
        return self.ime[0]==self.prezime[0]
        
    def ispravanJmbg(self):
        return len(self.jmbg)==13
        
    def __repr__(self):
        return "{}  {}".format(self.ime,self.prezime)

    
        
nastavi="y"
osobe=[]
while nastavi=="y":
    ime=input("Unesite ime osobe: ")
    prezime=input("Unesite prezime osobe: ")
    jmbg=input("Unesite jmbg :")
    osoba=Osoba(ime,prezime,jmbg)
    osobe.append(osoba)
    nastavi=input("y/n :")
    
istiInicijali=[ x for x in osobe if x.istiInicijali()]

osobe.sort(key=lambda x: x.prezime)
print("Osobe sotirane po prezimenima:{}".format(osobe))

