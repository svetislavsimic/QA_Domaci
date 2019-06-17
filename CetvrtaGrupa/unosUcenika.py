from klaseNasledjivanje import Ucenik,Pol

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
	ucenici.append(Ucenik(ime=ime,prezime=prezime,jmbg=jmbg,pol=pol,odeljenje=odeljenje))
	nastavi=input("Zelite li da nastavite unos: y/n ")

print(ucenici)