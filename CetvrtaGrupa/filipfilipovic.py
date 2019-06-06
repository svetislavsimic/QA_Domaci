osobe=[]
i="y"
while i=="y":
    ime=input("Unesite ime osobe:")
    prezime=input("Unesite prezime osobe:")
    osobe.append((ime,prezime))
    i=input("y/n")


karakteri=input("Unesite karaktere za ispitivanje:").lower()
novaListaOsoba=[x for x in osobe if karakteri in x[0].lower()]
print(novaListaOsoba)
