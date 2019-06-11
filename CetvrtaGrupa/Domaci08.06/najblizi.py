# Napisati funkciju koja iz liste brojeva vraća broj koji je najmanje udaljen od nule.

listaBrojeva=[4,6,-4,-2,5,2,12]
novaLista=[]
def najbliziBroj(lista):
	novaLista.append(min(lista, key=lambda x:abs(x-0)))
	return novaLista
	
print("Najblizi broj nuli u listi brojeva: {} je broj: {}".format (listaBrojeva,najbliziBroj(listaBrojeva)))