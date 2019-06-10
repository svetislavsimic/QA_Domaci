def a(ime, prezime, jmbg):
	lista=["01-stranci u BiH","02-stranci u Crnoj Gori","03–stranci u Hrvatskoj","04–stranci u Makedoniji","05–stranci u Sloveniji","07–stranci u Srbiji (bez pokrajina)","08–stranci u Vojvodini","09–stranci na Kosovu i Metohiji","10–Banja Luka","11–Bihac","12–Doboj","13–Gorazde","14–Livno","15–Mostar","16–Prijedor","17–Sarajevo","18–Tuzla","19–Zenica","21–Podgorica","26–Niksic","29–Pljevlja","30–Osijek, Slavonija regija","31–Bjelovar, Virovitica, Koprivnica, Pakrac, Podravina regija","32–Varazdin, Medjimurje regija","33–Zagreb","34–Karlovac","35–Gospic,Lika regija","36–Rijeka, Pula, Istra i Primorje regija","37–Sisak, Banovina regijaSisak, Banovina regija","38–Split, Zadar, Dubrovnik, Dalmacija regija","39–Hrvatska bez Osijeka, Zagreba,Karlovca, regije Slavonija, Bjelovara, Virovitice, Koprivnice, Pakraca, regije Podravina, Varazdina, regije Medjimurje, Gospica, regije Lika, Rijeke, Pule, Istre, regije Primorje, Siska, regije Banovina, Splita, Zadra, Dubrovnika, regije Dalmacija","41–Bitolj","42–Kumanovo","43–Ohrid","44–Prilep","45–Skoplje","46–Strumica","47–Tetovo","48–Veles","49–Stip","50–Slovenija","71–Beograd regija","72–Sumadija","73–Nis","74–Juzna Morava","75–Zajecar","76–Podunavlje","77–Podrinje i Kolubara","78–Kraljevo","79–Uzice","80–Novi Sad","81–Sombor","82–Subotica","85–Zrenjanin","86–Pancevo","87–Kikinda","88–Ruma","89–Sremska Mitrovica","91–Pristina","92–Kosovska Mitrovica","93–Pec","94–Djakovica","95–Prizren","96–Kosovsko Pomoravski okrug"]

	try:
		d=jmbg[:2]
		m=jmbg[2:4]
		g=jmbg[4:7]
		pol=jmbg[9:12]
		lista1=["1",g]
		lista2=["2",g]
		gSa1="".join(lista1)
		gSa2="".join(lista2)
		brGodina1=2019-(int(gSa1))
		brGodina2=2019-(int(gSa2))

		provera=11-((7*(int(jmbg[0])+int(jmbg[6]))+6*(int(jmbg[1])+int(jmbg[7]))+5*(int(jmbg[2])+int(jmbg[8]))+4*(int(jmbg[3])+int(jmbg[9]))+3*(int(jmbg[4])+int(jmbg[10]))+2*(int(jmbg[5])+int(jmbg[11])))%11)

		if len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and int(jmbg[4])==9 and 1<=int(d)<=28 and 1<=int(m)<=12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and 1<=int(d)<=28 and 1<=int(m)<=12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==29 and int(m)==2 and int(g)%4==0:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==29 and int(m)==2 and int(g)%4==0:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")
			
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==29 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==29 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")
					
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==30 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==30 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==1:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==1:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==3:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==3:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==5:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==5:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==7:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==7:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==8:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==8:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==10:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==10:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and int(pol)>=500 and "2"<=jmbg[4]<="8":
			return("Osoba "+str(ime).capitalize()+" "+str(prezime).capitalize()+"je zenskog pola i nije medju zivima.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and int(jmbg[4])==9 and 1<=int(d)<=28 and 1<=int(m)<=12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and 1<=int(d)<=28 and 1<=int(m)<=12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==29 and int(m)==2 and int(g)%4==0:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==29 and int(m)==2 and int(g)%4==0:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")
			
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==29 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==29 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")
					
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==30 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==30 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==1:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==1:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==3:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==3:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==5:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==5:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==7:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==7:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==8:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==8:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==10:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==10:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muskii imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")
		
		elif len(jmbg)==13 and (int(jmbg[12])==provera)!=0 and 0<=int(pol)<500 and "2"<=jmbg[4]<="8":
			return("Osoba "+str(ime).capitalize()+" "+str(prezime).capitalize()+"je muskog pola i nije medju zivima.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and int(jmbg[4])==9 and 1<=int(d)<=28 and 1<=int(m)<=12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and 1<=int(d)<=28 and 1<=int(m)<=12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==29 and int(m)==2 and int(g)%4==0:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==29 and int(m)==2 and int(g)%4==0:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")
			
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==29 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==29 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")
					
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==30 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==30 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==1:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==1:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==3:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==3:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==5:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==5:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==7:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==7:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==8:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==8:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==10:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==10:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and int(jmbg[4])==9 and int(d)==31 and int(m)==12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je zenski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je zenski i imate "+str(brGodina2)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and int(pol)>=500 and "2"<=jmbg[4]<="8":
			return("Osoba "+str(ime).capitalize()+" "+str(prezime).capitalize()+"je zenskog pola i nije medju zivima.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and int(jmbg[4])==9 and 1<=int(d)<=28 and 1<=int(m)<=12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and 1<=int(d)<=28 and 1<=int(m)<=12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==29 and int(m)==2 and int(g)%4==0:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==29 and int(m)==2 and int(g)%4==0:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")
			
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==29 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==29 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")
					
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==30 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==30 and 1<=int(m)<=12 and int(m)!=2:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==1:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==1:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==3:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==3:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==5:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==5:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==7:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==7:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==8:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==8:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==10:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muski i imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==10:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")

		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and int(jmbg[4])==9 and int(d)==31 and int(m)==12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".1"+str(g)+". Vas pol je muskii imate "+str(brGodina1)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and 0<=int(jmbg[4])<=1 and int(d)==31 and int(m)==12:
			return("Vase ime je "+str(ime).capitalize()+" "+str(prezime).capitalize()+". Rodjeni ste "+str(d)+"."+str(m)+".2"+str(g)+". Vas pol je muski i imate "+str(brGodina2)+" godina.")
		
		elif len(jmbg)==13 and int(jmbg[12])==0 and provera>9 and 0<=int(pol)<500 and "2"<=jmbg[4]<="8":
			return("Osoba "+str(ime).capitalize()+" "+str(prezime).capitalize()+"je muskog pola i nije medju zivima.")
		

		else:
			return("Uneli ste neispravan JMBG.")
	
	except ValueError:
		return("Uneli ste neispravan JMBG.")
		
	except IOError:
		return("Uneli ste neispravan JMBG.")

	except IndexError:
		return("Uneli ste neispravan JMBG.")
	
	finally:
		try:
			for mesto in lista:
				if len(jmbg)==13 and int(jmbg[4:7])>976 and mesto[:2]==jmbg[7:9] and int(jmbg[12])==0 and provera>9:
					mesto=mesto[3:]
					print("Mesto rodjenja je:",mesto)
				elif len(jmbg)==13 and int(jmbg[4:7])<=976 and mesto[:2]==jmbg[7:9] and int(jmbg[12])==0 and provera>9:
					mesto=mesto[3:]
					print("Mesto prebivalista u toku dodeljivanja JMBG je:",mesto)
				elif len(jmbg)==13 and int(jmbg[4:7])>976 and mesto[:2]==jmbg[7:9] and (int(jmbg[12])==provera)!=0:
					mesto=mesto[3:]
					print("Mesto rodjenja je:",mesto)
				elif len(jmbg)==13 and int(jmbg[4:7])<=976 and mesto[:2]==jmbg[7:9] and (int(jmbg[12])==provera)!=0:
					mesto=mesto[3:]
					print("Mesto prebivalista u toku dodeljivanja JMBG je:",mesto)
				elif int(jmbg[7:9])==0:
					pass
				elif int(jmbg[7:9])==10:
					pass
				elif int(jmbg[7:9])==20:
					pass
				elif 22<=int(jmbg[7:9])<=25:
					pass
				elif 27<=int(jmbg[7:9])<=28:
					pass
				elif int(jmbg[7:9])==40:
					pass
				elif 51<=int(jmbg[7:9])<=70:
					pass
				elif 83<=int(jmbg[7:9])<=84:
					pass
				elif int(jmbg[7:9])==90:
					pass
				elif int(jmbg[7:9])>=97:
					pass
				else:
					pass
		except ValueError:
			pass
		
		except IOError:
			pass

		except IndexError:
			pass



ime=input("Unesi ime: ")
prezime=input("Unesi prezime: ")
broj=input("Unesi JMBG: ")

print(a(ime, prezime, broj))	


