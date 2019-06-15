# Napisati program za unos sa tastature liste osoba a zatim sortirati tu listu po prezimenu u leksikografskom poretku
# Napisati program za unos sa tastature liste osoba a zatim izdvojiti one osobe čije ime počinje na korisnički zadato slovo


class Osoba:
	def __init__(self, ime, prezime):
		self.ime=ime
		self.prezime=prezime
	def __repr__(self):
		return self.ime.capitalize()+" "+self.prezime.capitalize()
	

osobe=[]
nastavi="y"
i=0
while nastavi=="y":
	for i in range(i+1):
		i=i+1
	ime=input("Unesite ime osobe "+str(i)+": ")
	prezime=input("Unesite prezime osobe "+str(i)+": ")
	osobe.append(Osoba(ime,prezime))
	nastavi=input("Zelite li da nastavite unos: y/n ")

from operator import attrgetter
osobeSort=sorted(osobe, key=attrgetter('prezime', 'ime'))


karakter=input("Unesite karakter za filtriranje liste: ")
osobeSaKarakterom=[x for x in osobe if (x.ime.lower()).startswith(karakter.lower())]


print("Sortirana lista osoba po prezimenu u leksikografskom poretku je: {}\nOsobe cije ime pocinje na zadati karakter su: {}".format(osobeSort,osobeSaKarakterom))


