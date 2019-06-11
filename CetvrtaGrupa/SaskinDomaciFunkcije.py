# Zadaci
# Napisati funkciju koja iz liste brojeva vraca broj koji je najmanje udaljen od nule.

# listaBrojeva = [1, 2, 3, 4, 5, 6, 7, 9, 10]
# mojBroj = 0
# def najblizi(list, Number):
    # najblizi = []
    # for i in list:
        # najblizi.append(abs(Number-i))

    # return najblizi.index(min(najblizi))

# a = najblizi(listaBrojeva, mojBroj)
# print ("Broj : ",a)
# print ("Broj najmanje udaljen od broja 0 je : ",listaBrojeva[a])

# Napisati funkciju koja iz JMBG-a vraca datum rodjenja osobe, formatiran dd-mm-yyyy

# a=input("Unesite JMBG: ")	
# if a[5]=="9":
    # print("datum rodjenja je: ",a[:2]+"-"+a[2:4]+"-"+"1"+a[4:7])
# elif a[5]=="0":
    # print("datum rodjenja je: ",a[:2]+"-"+a[2:4]+"-"+"2"+a[4:7])

# Napisati funkciju koja proverava da li je registarski broj autobila u ispravnom formatu.

# import re
# registarskaOznaka=input("Unesite registarsku oznaku (primer: BG XXX-AA): ")
# if (re.search(r"^[a-z,A-Z]{2} [0-9]{4}-[a-z,A-Z]{2}$", registarskaOznaka)):
    # print("Registarski broj autobila je unet u ispravnom formatu")
# elif (re.search(r"^[a-z,A-Z]{2} [0-9]{3}-[a-z,A-Z]{2}$", registarskaOznaka)):
    # print("Registarski broj autobila je unet u ispravnom formatu")
# else:
    # print("Registrarski broj automobila nije unet u ispravnom formatu")
