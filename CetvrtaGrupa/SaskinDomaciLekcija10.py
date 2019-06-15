class Osoba:
    def __init__(self,ime,prezime,jmbg):
        self.ime=ime
        self.prezime=prezime
        self.jmbg=jmbg
    def inicijali(self):
        return self.ime[0]+ self.prezime[0]
    def istiInicijali(self):
        return self.ime[0]==self.prezime[0]
    def prettify(self):
        return self.ime.capitalize() + ' ' + self.prezime.capitalize()
    def __repr__(self):
        return self.ime+" "+self.prezime
    def IstravanJMBG (self):
        return len(self.jmbg)==13
    def sortiranjePoPrezimenu (self):
        return sorted(self.ime.capitalize() + ' ' + self.prezime.capitalize())
    def startswith(self):
        return self.ime+" "+self.prezime
    def zadataGodina(self):
        godina=2019
        if jmbg[5]=="9":
            return (2019-int("1"+jmbg[4:7]))
        else:
            return (2019-int("2"+jmbg[4:7]))

   
    
              
osobe=[]
nastavi="y"
while nastavi=="y":
    ime=input("Unesite ime: ")
    prezime=input("Unesite prezime: ")
    jmbg=input("Unesite jmbg: ")
    if len(jmbg) == 13:
        print("Uneli ste ispravan jmbg")
    elif jmbg == ['a-z','A-Z']:
        print("Uneli ste pogresan jmbg")
    else:
        print("Uneli ste pogresan jmbg")
    osobe.append(Osoba(ime,prezime,jmbg))
    nastavi=input("Za novi unos unesite: y ")

    
        
najduzePrezime=osobe[1]
for osoba in osobe:
    if len(osoba.prezime)>len(najduzePrezime.prezime):
        najduzePrezime=osoba
print("Najduze prezime je: {}".format(najduzePrezime.prezime))

ImenaSaIstimInicijalima=[x for x in osobe if x.istiInicijali()]
print("Lista osoba sa istim inicijalima je : " ,ImenaSaIstimInicijalima)

from operator import attrgetter
sortiranje=sorted(osobe, key=attrgetter('prezime','ime'))
print("Lista osoba sortirana po prezimenu je: {}".format(sortiranje))

slovo=input("Unesite prvo slovo za pretragu osobe po imenu: ")
pretragaOsobe=[x for x in osobe if x.ime.startswith(slovo)]
print("Imena koja pocinju na zadato slovo su: ", pretragaOsobe)

godineStarosti=[]
for godine in osobe:
    if jmbg[5]=="9":
        print("Godine starosti osoba su: ", 2019-int("1"+jmbg[4:7]))
    else:
        print ("Godine starosti osoba su: ", 2019-int("2"+jmbg[4:7]))
