def NajveciPalindrom(n):

    gornjaGranica=0

    for i in range(1, n+1):

        gornjaGranica=gornjaGranica * 10
        gornjaGranica=gornjaGranica +9

    donjaGranica= 1+gornjaGranica//10

    pocetna_vrednost= 0
    for i in range(gornjaGranica,donjaGranica-1,-1):
        for j in range(i,donjaGranica-1,-1):
            vrednost= i*j
            if (vrednost<pocetna_vrednost):
                break
            broj=vrednost
            reverse=0

            while(broj !=0):
                reverse=reverse*10+broj  %10
                broj =broj //10
            if(vrednost==reverse and vrednost>pocetna_vrednost):
                pocetna_vrednost=vrednost
    return pocetna_vrednost
n=3
print(NajveciPalindrom(n))
