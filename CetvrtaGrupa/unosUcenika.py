from klaseNasledjivanje import Osoba,Ucenik,Pol,Predmet

ucenici=[]
nastavi="y"
i=0
while nastavi=="y":
	for i in range(i+1):
		i=i+1
	ime=input("Unesite ime ucenika "+str(i)+": ")
	prezime=input("Unesite prezime ucenika "+str(i)+": ")
	jmbg=input("Unesite jmbg ucenika "+str(i)+": ")
	uspesnoUnetPol=False
	while uspesnoUnetPol==False:
		pol=input("Unesite pol ucenika "+str(i)+": m-z ")
		if pol.lower()=="m":
			pol=Pol.MUSKI
			uspesnoUnetPol=True
		elif pol.lower()=="z":
			pol=Pol.ZENSKI
			uspesnoUnetPol=True
		else:
			print("Uneli ste nepostojeci pol")
	odeljenje=input("Unesite odeljenje ucenika "+str(i)+": ")
	spisakPredmeta=[]
	x=0
	while nastavi=="y":
		for x in range(x+1):
			x=x+1
		uspesnoUnetPredmet=False
		while uspesnoUnetPredmet==False:
			predmet=input("Unesite predmet "+str(x)+" ucenika "+str(i)+": ")
			if predmet.lower()=="matematika":
				predmet=Predmet.MATEMATIKA
				uspesnoUnetPredmet=True
			elif predmet.lower()=="srpski":
				predmet=Predmet.SRPSKI
				uspesnoUnetPredmet=True
			elif predmet.lower()=="hemija":
				predmet=Predmet.HEMIJA
				uspesnoUnetPredmet=True
			elif predmet.lower()=="fizika":
				predmet=Predmet.FIZIKA
				uspesnoUnetPredmet=True
			elif predmet.lower()=="engleski":
				predmet=Predmet.ENGLESKI
				uspesnoUnetPredmet=True
			elif predmet.lower()=="istorija":
				predmet=Predmet.ISTORIJA
				uspesnoUnetPredmet=True
			elif predmet.lower()=="geografija":
				predmet=Predmet.GEOGRAFIJA
				uspesnoUnetPredmet=True
			elif predmet.lower()=="biologija":
				predmet=Predmet.BIOLOGIJA
				uspesnoUnetPredmet=True
			elif predmet.lower()=="nemacki":
				predmet=Predmet.NEMACKI
				uspesnoUnetPredmet=True
			elif predmet.lower()=="muzicko":
				predmet=Predmet.MUZICKO
				uspesnoUnetPredmet=True
			else:
				print("Uneli ste nepostojeci predmet")
			nastavi=input("Zelite li da nastavite unos predmeta: y/n ")
s=(Ucenik(ime=ime,prezime=prezime,jmbg=jmbg,pol=pol,odeljenje=odeljenje)).initPredmeti(predmet)
ucenici.append(Ucenik(ime=ime,prezime=prezime,jmbg=jmbg,pol=pol,odeljenje=odeljenje))
nastavi=input("Zelite li da nastavite unos: y/n ")

print(ucenici,s)