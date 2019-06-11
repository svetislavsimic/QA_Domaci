

def datumRodjenja(jmbg):
    datum=None
    if jmbg!="" and len(jmbg)==13:
        if jmbg[4]=="9":
            datum=jmbg[0:2]+"-"+jmbg[2:4]+"-"+"1"+jmbg[4:7]
        elif jmbg[4]=="0":
            datum=jmbg[0:2]+"-"+jmbg[2:4]+"-"+"2"+jmbg[4:7]
        else:
            print("Doslo je do greske.")
        print("Osoba je rodjena {}".format(datum))

primerJmbg=input("Unesite jmbg:")
datumRodjenja(primerJmbg)
