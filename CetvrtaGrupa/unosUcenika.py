from klaseNasledjivanje import Ucenik, Pol

            
ucenici=[]
nastavi="y"
while nastavi=="y":
    ime=input("Unesite ime ucenika: ")
    prezime=input("Unesite prezime ucenika: ")
    jmbg=input("Unesite jmbg ucenika: ")
    uspesnoUnetPol=False
    while uspesnoUnetPol==False:
        pol=input("Unesite pol ucenika: m-z ")
        if pol.lower()=="m":
            pol=Pol.MUSKI
            uspesnoUnetPol=True
        elif pol.lower()=="z":
            pol=Pol.ZENSKI
            uspesnoUnetPol=True
        else:
            print("Uneli ste nepostojeci pol")
    odeljenje=input("Unesite odeljenje: ")
    ucenici.append(Ucenik(ime=ime, prezime=prezime,jmbg=jmbg, pol=pol, odeljenje=odeljenje))
    nastavi=input("Za dalji unos ucenika pritisnite 'y' ")
    
print(ucenici)
        
    