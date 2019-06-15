# Napisati funkciju koja iz liste brojeva vraća broj koji je najmanje udaljen od nule.

# def najmanjeUdaljen(brojevi):
	# noviBrojevi=[x if x>=0 else -x for x in brojevi]
	# noviBrojevi.sort()
	# najmanji=noviBrojevi[0]
	# return("Lista brojeva je: {}\nNova lista je: {}\nBroj koji je najmanje udaljen od nule je: {}".format(brojevi,noviBrojevi,najmanji))

# brojevi=[]
# nastavi="y"
# i=0
# while nastavi=="y":
	# try:
		# for i in range(i+1):
			# i=i+1
		# broj=int(input("Unesite broj "+str(i)+": "))
		# brojevi.append(broj)
		# nastavi=input("Za unos novog broja pritisnite 'y': ")
	# except ValueError:
		# print("Uneli ste nesto pogresno.")

# print(najmanjeUdaljen(brojevi))
	
# Napisati funkciju koja proverava da li je registarski broj automobila u ispravnom formatu.

# BG-001-AA
# BG-0001-AA
# BG-MARKO
	

def ispravanRegistarski(regBroj):

	ordSlova=[262,268,272,352,381]
	for x in range (65,91):
		ordSlova.append(x)



	if len(regBroj)==9 and regBroj[2]=="-" and regBroj[6]=="-" and regBroj[3:6].isnumeric() and regBroj[3:6]!="000" and (ord(regBroj[0]) in ordSlova) and (ord(regBroj[1]) in ordSlova) and (ord(regBroj[-2]) in ordSlova) and (ord(regBroj[-1]) in ordSlova):
		return("Uneti registarski broj je ispravan")
	elif len(regBroj)==10 and regBroj[2]=="-" and regBroj[7]=="-" and regBroj[3:7].isnumeric() and regBroj[3:7]!="0000" and (ord(regBroj[0]) in ordSlova) and (ord(regBroj[1]) in ordSlova) and (ord(regBroj[-2]) in ordSlova) and (ord(regBroj[-1]) in ordSlova):
		return("Uneti registarski broj je ispravan")
	elif len(regBroj)==8 and regBroj[2]=="-" and (ord(regBroj[0]) in ordSlova) and (ord(regBroj[1]) in ordSlova) and (ord(regBroj[3]) in ordSlova) and (ord(regBroj[4]) in ordSlova) and (ord(regBroj[5]) in ordSlova) and (ord(regBroj[6]) in ordSlova) and (ord(regBroj[7]) in ordSlova):
		return("Uneti registarski broj je ispravan")
	else:
		return("Uneti registarski broj nije ispravan")
			

broj=(input("Unesite registarski broj automobila: ")).upper()
print(ispravanRegistarski(broj))

