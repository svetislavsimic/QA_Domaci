class Osoba:
	def __init__(self,ime,prezime,godine):
		self.ime=ime
		self.prezime=prezime
		self.godine=godine
		
	def __repr__(self):
		return "{} {}".format(self.ime,self.prezime)
		
nastavi="y"
osobe=[]
while nastavi=="y":
    ime=input("Unesite ime osobe:")
    prezime=input("Unesite prezime osobe:")
    godine=int(input("Unesite godine:"))
    osoba=Osoba(ime,prezime,godine)
    osobe.append(osoba)
    nastavi=input("y/n :")

krit=int(input("Unesite kriterijum za godine: "))

# Napisati program za unos sa tastature liste osoba a zatim pronaći najmlađu osobu.
najMladja=osoba
for x in osobe:
	if x.godine>najMladja.godine:
		najMladja=x
print("Najmladja osoba iz liste {} je: {}".format(osobe,najMladja))


# Napisati program za unos sa tastature liste osoba a zatim izdvojiti sve osobe mlađe od korisnički zadatog kriterijuma.
lista=[x for x in osobe if x.godine<krit]
print("Lista osoba mljadjih od {} godina: {}".format(krit,lista))

