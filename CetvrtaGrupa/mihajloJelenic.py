# osobe=[]
# nastavi="d"

# while nastavi =="d":
	# ime=input("Unesite ime: ")
	# prez=input("Unesite prezime: ")a
	# nastavi=input("Nastavi: d/n? ")
	# osobe.append((ime,prez))
	
# filter=input("Unesite slova za filtriranje imena: ")
	
# print(osobe)

# filtriranaLista=[x for x in osobe if filter in x[0]]
# print(filtriranaLista)

class osoba:
	def __init__(self,ime,prezime):
		self.ime=ime
		self.prezime=prezime
	def inicijali (self):
		return self.ime[0]+self.prezime[0]