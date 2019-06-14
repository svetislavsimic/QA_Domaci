class Osoba:
	def __init__(self, ime, prezime):
		self.ime=ime
		self.prezime=prezime
		
	def __repr__(self):
		return "{} {}".format(self.ime,self.prezime)
		
		
nastavi="y"
osobe=[]
while nastavi=="y":
	ime=input("Unesite ime osobe: ").capitalize()
	prezime=input("Unesite prezime osobe: ").capitalize()
	osoba=Osoba(ime,prezime)
	osobe.append(osoba)
	nastavi=input("y/n :")
		
# Napisati program za unos sa tastature liste osoba a zatim sortirati tu listu po prezimenu u leksikografskom poretku

lista= sorted(osobe, key=lambda p:p.prezime)
print("Sortirana lista osoba po prezimenu u leksikografskom poretku: {}".format(lista))	

# Napisati program za unos sa tastature liste osoba a zatim izdvojiti one osobe čije ime počinje na korisnički zadato slovo

char=input("Unesite pocetno slovo imena za pretragu: ").capitalize()
pocSlovo=[ x for x in osobe if x.ime.startswith(char)]
print("Lista osoba cije ime pocinje na {} slovo: {}".format (char,pocSlovo))


