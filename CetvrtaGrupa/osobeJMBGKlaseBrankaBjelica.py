# Napisati novu definiciju klase Osoba tako što će svaka osoba imati svoj JMBG. Zatim:
# Napisati metodu koja proverava da li je ispravan matični broj osobe
# Napisati metodu koja vraća godine starosti osobe u odnosu na korisničku zadatu godinu

# Sad za novokreiranu klasu Osoba potrebno je uraditi:
# Napisati program za unos sa tastature liste osoba a zatim pronaći najmlađu osobu.
# Napisati program za unos sa tastature liste osoba a zatim izdvojiti sve osobe mlađe od korisnički zadatog kriterijuma.




class Osoba:
	def __init__(self, ime, prezime, jmbg):
		self.ime=ime
		self.prezime=prezime
		self.jmbg=jmbg
	
	def ispravanJmbg(self):
		provera=11-((7*(int(self.jmbg[0])+int(self.jmbg[6]))+6*(int(self.jmbg[1])+int(self.jmbg[7]))+5*(int(self.jmbg[2])+int(self.jmbg[8]))+4*(int(self.jmbg[3])+int(self.jmbg[9]))+3*(int(self.jmbg[4])+int(self.jmbg[10]))+2*(int(self.jmbg[5])+int(self.jmbg[11])))%11)
		if (int(self.jmbg[12])==provera)!=0 and self.jmbg.isnumeric() and len(self.jmbg)==13:		
			return self.jmbg
		elif int(self.jmbg[12])==0 and provera>9 and self.jmbg.isnumeric() and len(self.jmbg)==13:
			return self.jmbg
		else:
			pass	

	def __repr__(self):
		return self.ime.capitalize()+" "+self.prezime.capitalize()+" "+self.jmbg
		
	def godine(self):
		g=self.jmbg[4:7]
		lista1=["1",g]
		lista2=["2",g]
		gSa1="".join(lista1)
		gSa2="".join(lista2)
		brGodina1=2019-(int(gSa1))
		brGodina2=2019-(int(gSa2))
		if int(self.jmbg[4])==9:
			brGodina=brGodina1
		else:
			brGodina=brGodina2
		
		return brGodina

osobe=[]
nastavi="y"
i=0
while nastavi=="y":
	try:
		for i in range(i+1):
			i=i+1
		ime=input("Unesite ime osobe "+str(i)+": ")
		prezime=input("Unesite prezime osobe "+str(i)+": ")
		jmbg=input("Unesite jmbg osobe "+str(i)+": ")
		o=Osoba(ime,prezime,jmbg)
		if o.ispravanJmbg():
			osobe.append(o)
		else:
			pass
		nastavi=input("Zelite li da nastavite unos: y/n ")

	except ValueError:
		print("Uneli ste neispravan JMBG.")
		
	except IOError:
		print("Uneli ste neispravan JMBG.")

	except IndexError:
		print("Uneli ste neispravan JMBG.")

	except NameError:
		print("Uneli ste neispravan JMBG.")

najmladjaOsoba=osobe[0]
for osoba in osobe:
	if osoba.godine()<najmladjaOsoba.godine():
		najmladjaOsoba=osoba

l=[]
for god in osobe:
	if god.godine()==najmladjaOsoba.godine():
		god=god.ime.capitalize()+" "+god.prezime.capitalize()
		l.append(god)

l1=[]
krit=int(input("Unesi neki broj godina: "))

for osoba1 in osobe:
	if osoba1.godine()<krit:
		osoba1=osoba1.ime.capitalize()+" "+osoba1.prezime.capitalize()
		l1.append(osoba1)


print("Lista osoba je: {}\nNajmanje godina ima osoba: {}\nOsobe koje su mladje od {} godina su: {}".format(osobe,l,krit,l1))



