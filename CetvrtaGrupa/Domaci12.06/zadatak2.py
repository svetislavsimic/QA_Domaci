class Osoba:
	def __init__(self, ime, prezime, jmbg):
		self.ime=ime
		self.prezime=prezime
		self.jmbg=jmbg
		
	def __repr__(self):
		return "{} {}".format(self.ime,self.prezime)
		
	def ispravanJmbg(self):
		if len(self.jmbg)==13:
			return ("Uneli ste ispravan JMBG")
		else:
			return ("Niste uneli ispravan JMBG")
			
	def godine(self):
		if self.jmbg[4] == "9" and len(self.jmbg) == 13  :
			return god - int("1" + self.jmbg[4:7])
		elif self.jmbg[4] == "0" and len(self.jmbg) == 13:
			return god - int("2" + self.jmbg[4:7])
		else:
			pass
		
		

ime=input("Unesite ime osobe: ")
prezime=input("Unesite prezime osobe: ")
jmbg=input("Unesite jmbg :")
osoba=Osoba(ime,prezime,jmbg)
god=int(input("Unesite godinu za izracunavanje: "))	

# Napisati metodu koja proverava da li je ispravan matični broj osobe
print(osoba.ispravanJmbg())

# Napisati metodu koja vraća godine starosti osobe u odnosu na korisničku zadatu godinu
print("Prema godini koju ste uneli {}, imate {} godina".format(god,osoba.godine()))
