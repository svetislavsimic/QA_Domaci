
def udaljenostOdNule(lista):
    najkracaUdaljenost=min(lista, key=abs)
    print("Broj najblizi nuli je {}...".format(najkracaUdaljenost))


brojevi=[-2,22,3,55,1]
udaljenostOdNule(brojevi)
