# Napisati funkciju koja iz JMBG-a vraća datum rođenja osobe, formatiran dd-mm-yyyy

def godinaRodjenja(jmbg):
	if jmbg[4] == "9" and len(jmbg) == 13  :
		return jmbg[:2] + "-" + jmbg[2:4]+ "-1" + jmbg[4:7]
	elif jmbg[4] == "0" and len(jmbg) == 13:
		return jmbg[:2] + "-" + jmbg[2:4]+ "-2" + jmbg[4:7]
	else:
		return "Netacan. Niste uneli dobar JMBG"
		
maticniBroj= input("Unesite Vas JMBG: ")

print("Vas datum rodjenja je: {}".format(godinaRodjenja(maticniBroj)))