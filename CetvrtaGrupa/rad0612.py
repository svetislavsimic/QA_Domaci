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
		provera=11-((7*(int(self.jmbg[0])+int(self.jmbg[6]))+6*(int(self.jmbg[1])+int(self.jmbg[7]))+5*(int(self.jmbg[2])+int(self.jmbg[8]))+4*(int(self.jmbg[3])+int(self.jmbg[9]))+3*(int(self.jmbg[4])+int(self.jmbg[10]))+2*(int(self.jmbg[5])+int(self.jmbg[11])))%11)
		if (int(self.jmbg[12])==provera)!=0 and self.jmbg.isnumeric() and len(self.jmbg)==13:		
			return self.jmbg
		elif int(self.jmbg[12])==0 and provera>9 and self.jmbg.isnumeric() and len(self.jmbg)==13:
			return self.jmbg
		else:
			pass	


	def godinaRodjenja(self):
		g=self.jmbg[4:7]
		if g[0]=="9":
			g="1"+g
		else:
			g="2"+g
		return int(g)
        
	def godine(self, godina):
		god=int(godina)-self.godinaRodjenja()
		if god<0:
			return 0
		else:
			pass
		return god
	
	def __repr__(self):
		return self.ime.capitalize()+" "+self.prezime.capitalize()+" "+self.jmbg


        
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
		nastavi=input("y/n :")
	except ValueError:
		print("Uneli ste neispravan JMBG.")
		
	except IOError:
		print("Uneli ste neispravan JMBG.")

	except IndexError:
		print("Uneli ste neispravan JMBG.")

istiInicijali=[ x for x in osobe if x.istiInicijali()]


from operator import attrgetter
osobeSort=sorted(osobe, key=attrgetter('prezime', 'ime'))


karakter=input("Unesite karakter za filtriranje liste: ")
osobeSaKarakterom=[x for x in osobe if (x.ime.lower()).startswith(karakter.lower())]



godina=input("Unesi godinu za odredjivanje starosti osobe: ")
krit=input("Unesi neki broj godina: ")
najmladjaOsoba=osobe[0]
for osoba in osobe:
	if osoba.godine(godina)<najmladjaOsoba.godine(godina):
		najmladjaOsoba=osoba

l=[]
for god in osobe:
	if god.godine(godina)==najmladjaOsoba.godine(godina):
		god=god.ime.capitalize()+" "+god.prezime.capitalize()
		l.append(god)

l1=[]
for osoba1 in osobe:
	if osoba1.godine(godina)<int(krit):
		osoba1=osoba1.ime.capitalize()+" "+osoba1.prezime.capitalize()
		l1.append(osoba1)


print("Sortirana lista osoba po prezimenu u leksikografskom poretku je: {}\nIste inicijale imaju osobe: {}\nOsobe cije ime pocinje na zadati karakter su: {}\nNajmanje godina ima osoba: {}\nOsobe koje su mladje od {} godina su: {}".format(osobeSort,istiInicijali,osobeSaKarakterom,l,krit,l1))
