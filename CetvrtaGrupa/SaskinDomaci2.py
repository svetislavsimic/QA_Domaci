# 2. Napravite program za unos osoba. Svaka osoba se unosi kao tapl (ime,prezime)
# Kada se zavrsi unos osoba korisnik se pita da unese karaktere na koji zeli da isfiltrira listu osoba po imenima.
# Zatim se ispisuju sve osobe koje zadovoljavaju kriterijum. Potrebno je uraditi domaci sa list comprehension 
# Primer:
# Unete osobe su [("Petar","Petrovic"),("Pavle","Simic"),("Nikola","Nenadovic"),("Panta","Pantic")]
# korisnik unese : pa
# ispisuju se osobe ("Pavle","Simic"),("Panta","Pantic")

# osobe=[("Petar","Petrovic"),("Pavle","Simic"),("Nikola","Nenadovic"),("Panta","Pantic")]
# print(osobe)
# karakter=input("Unesite karakter po kojem zelite da isfiltrirate listu osoba po imenima: ")
# novaLista=[x for x in osobe if karakter.lower() in  x[0].lower()]
# print(novaLista)
x = 50
def funk(x):
    print('x je trenutno',x)
    x = 2
    print('Promenili smo lokalnu vrenost x na',x)
funk(x)
print('x je idalje',x)