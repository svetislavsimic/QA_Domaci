lista=[]
nastavi="y"

while nastavi =="y":
	ime=input("Unesite ime: ")
	prezime=input("Unesite prezime: ")
	nastavi=input("Da li zelite da nastavite sa unosom: y/n? ")
	lista.append((ime,prezime))
	
filter=input("Unesite karaktere za filtriranje imena: ")
	
print(lista)

filtriranaLista=[x for x in lista if filter.lower() in x[0].lower()]
print(filtriranaLista)