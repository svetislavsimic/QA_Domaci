# Napisati funkciju koja proverava da li je registarski broj autobila u ispravnom formatu.
# 

regBroj=input("Unesite registarski broj: ")

def registarskiBroj(x):
	if regBroj[:2].isalpha() and regBroj[2]== "-" or regBroj[2]== " " and regBroj[-3]== "-" and regBroj[-2:].isalpha() and regBroj[3:6].isnumeric() and len(regBroj)==9:
		print ("Uneli ste ispravan format registarskog broja : {}".format (regBroj.upper()))
	elif regBroj[:2].isalpha() and regBroj[2]== "-" or regBroj[2]== " " and regBroj[-3]== "-" and regBroj[-2:].isalpha() and regBroj[3:7].isnumeric() and len(regBroj)==10:
		print ("Uneli ste ispravan format registarskog broja : {}".format (regBroj.upper()))
	else:
		print("Niste uneli ispravan format registarskog broja")
		
registarskiBroj(regBroj)