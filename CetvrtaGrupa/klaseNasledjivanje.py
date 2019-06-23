from enum import Enum
import datetime
import math

class Ocena(Enum):
    NEOCENJEN:1
    NEDOVOLJAN:2
    DOBAR:3
    VRLODOBAR:4
    ODLICAN:5

class Pol(Enum):
    MUSKI=1
    ZENSKI=2
    
class Predmet(Enum):
    MATEMATIKA=1
    SRPSKI=2
    HEMIJA=3
    FIZICKO=4
    LIKOVNO=5
    MUZICKO=6
    ISTORIJA=7
    GEOGRAFIJA=8
    BIOLOGIJA=9
    ENGLESKI=10
    RUSKI=11
    FRANCUSKI=12
    
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

    def __init__ (self, ime, prezime, jmbg, pol, odeljenje,prosek):
        self.odeljenje=odeljenje
        self.ocene={}
        self.predmet={}
        super().__init__(ime, prezime, jmbg, pol)

    def ispravanJmbg(self):
        return len(self.jmbg) == 13
        
    def dodajOcenu(self, predmet, ocena):
        if predmet in self.ocene.keys():
            self.ocene[predmet].append(ocena)
        else:
            self.ocene[predmet]=[ocena]
    def zakljuciOcenu(self,predmet):
        return sum(self.ocena[predmet])/len(self.ocena[predmet])
    def prosek(self):
        return sum (self.predmet.values)/len (self.predmet.values)

    ucenici = []
    nastavi = "y"
    while nastavi == "y":
        ime = input("Unesite ime ucenika: ")
        prezime = input("Unesite prezime ucenika: ")
        jmbg=False
        while jmbg==False:
            jmbg = input("Unesite jmbg ucenika: ")
            if len(jmbg) ==13 :
                True
            else:
                print("Uneliste pogresan Jmbg: ")

        uspesnoUnetPol = False
        while uspesnoUnetPol == False:
            pol = input("Unesite pol ucenika: m-z ")
            if pol.lower() == "m":
                pol = Pol.MUSKI
                uspesnoUnetPol = True
            elif pol.lower() == "z":
                pol = Pol.ZENSKI
                uspesnoUnetPol = True
            else:
                print("Uneli ste nepostojeci pol")
        odeljenje = input("Unesite odeljenje: ")
        ocene={}
        matematika = input("Unesite listu ocena iz matematike odvojene razmakom: ")
        listaMat = matematika.split()
        print("Lista ocena iz matematike je: ",listaMat)
        sum=0
        for ocena in listaMat:
            sum+=(int(ocena))
        zakljucnaMat = math.ceil(sum/len(listaMat))
        print("Zakljucena ocena iz matematike je: ", zakljucnaMat)

        srpski = input("Unesite listu ocena iz srpskog odvojene razmakom: ")
        listaSrp = srpski.split()
        print("Lista ocena iz srpskog je: ", listaSrp)
        sum = 0
        for ocena in listaSrp:
            sum += (int(ocena))
        zakljucnaSrp = math.ceil(sum / len(listaSrp))
        print("Zakljucena ocena iz srpskog je: ", zakljucnaSrp)

        hemija = input("Unesite listu ocena iz hemije odvojene razmakom: ")
        listaHem = hemija.split()
        print("Lista ocena iz hemije je: ", listaHem)
        sum = 0
        for ocena in listaHem:
            sum += (int(ocena))
        zakljucnaHem = math.ceil(sum / len(listaHem))
        print("Zakljucena ocena iz hemije je: ", zakljucnaHem)

        fizicko = input("Unesite listu ocena iz fizickog odvojene razmakom: ")
        listaFiz = fizicko.split()
        print("Lista ocena iz fizickog je: ", listaFiz)
        sum = 0
        for ocena in listaFiz:
            sum += (int(ocena))
        zakljucnaFiz = math.ceil(sum / len(listaFiz))
        print("Zakljucena ocena iz fizickog je: ", zakljucnaFiz)

        likovno = input("Unesite listu ocena iz likovnog odvojene razmakom: ")
        listaLik = likovno.split()
        print("Lista ocena iz likovnog je: ", listaLik)
        sum = 0
        for ocena in listaLik:
            sum += (int(ocena))
        zakljucnaLik = math.ceil(sum / len(listaLik))
        print("Zakljucena ocena iz likovnog je: ",zakljucnaLik)

        muzicko = input("Unesite listu ocena iz muzickog odvojene razmakom: ")
        listaMuz = muzicko.split()
        print("Lista ocena iz muzickog je: ", listaMuz)
        sum = 0
        for ocena in listaMuz:
            sum += (int(ocena))
        zakljucnaMuz = math.ceil(sum / len(listaMuz))
        print("Zakljucena ocena iz muzickog je: ",zakljucnaMuz)

        istorija = input("Unesite listu ocena iz istorije odvojene razmakom: ")
        listaIst = istorija.split()
        print("Lista ocena iz istorije je: ", listaIst)
        sum = 0
        for ocena in listaIst:
            sum += (int(ocena))
        zakljucnaIst = math.ceil(sum / len(listaIst))
        print("Zakljucena ocena iz istorije je: ",zakljucnaIst)

        geografija = input("Unesite listu ocena iz geografije odvojene razmakom: ")
        listaGeo = geografija.split()
        print("Lista ocena iz geografije je: ", listaGeo)
        sum = 0
        for ocena in listaGeo:
            sum += (int(ocena))
        zakljucnaGeo = math.ceil(sum / len(listaGeo))
        print("Zakljucena ocena iz geografije je: ",zakljucnaGeo)

        biologija = input("Unesite listu ocena iz biologije odvojene razmakom: ")
        listaBio = biologija.split()
        print("Lista ocena iz biologije je: ", listaBio)
        sum = 0
        for ocena in listaBio:
            sum += (int(ocena))
        zakljucnaBio = math.ceil(sum / len(listaBio))
        print("Zakljucena ocena iz biologije je: ",zakljucnaBio)

        jezik = input("Unesite jezik koji pohadjate: ")
        if jezik=="engleski":
            engleski=(input("Unesite listu ocena iz engleskog jezika odvojene razmakom: "))
            listaJez=engleski.split()
        elif jezik=="ruski":
            ruski=(input("Unesite listu ocena iz ruskog jezika odvojene razmakom: "))
            listaJez = ruski.split()
        elif jezik=="francuski":
            francuski=(input("Unesite listu ocena iz francuskog jezika odvojene razmakom:"))
            listaJez = francuski.split()
        else:
            "Uneli ste pogresan jezik"

        print("Lista ocena iz jezika je: ", listaJez)
        sum = 0
        for ocena in listaJez:
            sum += (int(ocena))
        zakljucnaJez = math.ceil(sum / len(listaJez))
        print("Zakljucena ocena iz jezika je: ", zakljucnaJez)

        ocene.update(matematika=zakljucnaMat, srpski=zakljucnaSrp,geografija=zakljucnaGeo, istorija=zakljucnaIst, muzicko=zakljucnaMuz, likovno=zakljucnaLik, fizicko=zakljucnaFiz, hemija=zakljucnaHem, biologija=zakljucnaBio, jezici=zakljucnaJez)
        print("Zakljucne ocene ucenika su : ", ocene)
        prosek = []
        sum = 0
        for prosek in ocene:
            sum += (int(ocena))
        ukupanProsek = math.ceil(sum / len(ocene))
        if ukupanProsek == 1:
            print("Uspeh ucenika je nedovoljan")
        elif ukupanProsek == 2:
            print("Uspeh ucenika je dovoljan")
        elif ukupanProsek == 3:
            print("Uspeh ucenika je dobar")
        elif ukupanProsek == 4:
            print("Uspeh ucenika je vrlo dobar")
        elif ukupanProsek == 5:
            print("Uspeh ucenika je odlican")
        else:
            print("Nekorektan unos podataka")
        nastavi = input("Za dalji unos ucenika pritisnite 'y' ")

    print(ucenici)







    
        