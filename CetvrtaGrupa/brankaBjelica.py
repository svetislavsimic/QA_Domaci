# Napravite program za unos osoba. Svaka osoba se unosi kao tapl (ime,prezime)
# Kada se zavrsi unos osoba korisnik se pita da unese karaktere na koji zeli da isfiltrira listu osoba po imenima.
# Zatim se ispisuju sve osobe koje zadovoljavaju kriterijum. Potrebno je uraditi domaci sa list comprehension 
# Primer:
# Unete osobe su [("Petar","Petrovic"),("Pavle","Simic"),("Nikola","Nenadovic"),("Panta","Pantic")]
# korisnik unese : pa
# ispisuju se osobe ("Pavle","Simic"),("Panta","Pantic")


osobe=[]
nastavi="y"
i=0
while nastavi=="y":
	for i in range(i+1):
		i=i+1
	ime=input("Unesite ime osobe "+str(i)+": ")
	prezime=input("Unesite prezime osobe "+str(i)+": ")
	osobe.append((ime.capitalize(), prezime.capitalize()))
	nastavi=input("Za unos nove osobe pritisnite 'y': ")


karakter=input("Unesite karakter za filtriranje liste: ")

osobeNovo=[x for x in osobe if ((x[0]).lower()).startswith(karakter.lower())]
print("Lista osoba je: {}\nFiltrirana lista je: {}".format(osobe,osobeNovo))
