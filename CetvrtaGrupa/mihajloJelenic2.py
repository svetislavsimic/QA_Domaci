
class Osoba:
	def __init__(self,ime,prezime,jmbg):
		self.ime=ime
		self.prezime=prezime
		self.jmbg=jmbg
	def __repr__(self):
			return "{} {}".format(self.ime,self.prezime)
	def ispravanjmbg(self):
		if len(self.jmbg)==13:
			return ("jmbg je ok")
		else: 
			return ("jmbg nije ok")
	def godine(self):
		if self.jmbg[4]=="9" and len(self.jmbg)==13:
			return godine-int ("1"+self.jmbg[4:7])
		elif self.jmbg[4]=="0" and len(self.jmbg)==13:
			return godine-int ("2"+self.jmbg[4:7])
		else:
			pass
osoba=[]
dalje="d"

while dalje=="d":
	ime=input("ime: ")
	prezime=input("prezime: ")
	jmbg=input("jmbg: ")
	osoba=Osoba(ime,prezime,jmbg)
	godine=int(input("godina za izrucanavanje je? "))
	dalje=input("d/n")
	
	#provera jmbg:

print (osoba.ispravanjmbg())
print ("prema godistu koje ste uneli {}, imate {} godina".format(godine,osoba.godine()))	



class Osoba:
	def __init__(self,ime,prezime,godine):
		self.ime=ime
		self.prezime=prez
		self.godine=godine
	def __repr__(self):
		return "{} {}". format(self.ime.self.prezime)
	
dalje="d"
osobe=[]
while dalje=="d":
	ime=input("ime: ")
	prezime=input("prezime: ")
	godine=int(input("godine: ")
	osoba=Osoba(ime,prezime,godine)
	osobe.append(osoba)
	dalje=input("d/n")
	
kriterijum=int(input("unesi godinu za mladju: "))

najmladja=osoba
for x in osobe:
	if x.godine>najmladja.godine:
		najmladja=x
print("najmladja osoba je {}: {}".format(osobe,najmladja)

lista=[x for x in osobe if x.godine<krit]
print("Lista osoba mljadjih od {} godina: {}".format(krit,lista))