

def regBroj(registracija):
    if len(registracija)==9:
        if registracija[0:2].isalpha() and registracija[0:2].isupper():
            if registracija[2]=="-":
                if registracija[3:6].isdigit():
                    if registracija[6]=="-":
                        if registracija[7:9].isalpha() and registracija[7:9].isupper():
                            print("Format je ispravan!")
                        else:
                            print("Format je neispravan!")
                    else:
                        print("Format je neispravan!")
                else:
                    print("Format je neispravan!")
            else:
                print("Format je neispravan!")
        else:
            print("Format je neispravan!")
    elif len(registracija)==10:
        if registracija[0:2].isalpha() and registracija[0:2].isupper():
            if registracija[2]=="-":
                if registracija[3:7].isdigit():
                    if registracija[7]=="-":
                        if registracija[8:10].isalpha() and registracija[8:10].isupper():
                            print("Format je ispravan!")
                        else:
                            print("Format je neispravan!")
                    else:
                        print("Format je neispravan!")
                else:
                    print("Format je neispravan!")
            else:
                print("Format je neispravan!")
        else:
            print("Format je neispravan!")
    else:
        print("Format je neispravan!")

broj=input("Unesite broj vase registracije:")
regBroj(broj)        




