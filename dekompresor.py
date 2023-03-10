#zadeklarovanie pomocnych premennych a zoznamu
daco = 0
nieco = 0
vysledny_riadok = []

#otvorenie suboru
subor = open("dekompresia_obrazka_1.txt","r")
subor1 = open("dekompresia_obrazka_vystup.txt","w")

def spracuj_riadok(): #funkcie na spracovanie riadku
    #zadeklarovanie globalnych premennych
    global daco, nieco
    global riadocek
    
    for pismeno in riadocek: #cyklus pre pismena v riadku
        #podmienka na zapisanie ako 0
        if nieco == 0:
            nieco = 1
            if pismeno != " ":
                for i in range(int(pismeno)): #opakuje podla momentalneho cisla
                    vysledny_riadok.append("0")
        #podmienka na zapisanie ako 1
        elif nieco == 1:
            nieco = 0
            if pismeno != " ":
                for i in range(int(pismeno)): #opakuje podla momentalneho cisla
                    vysledny_riadok.append("1")

    #zjednotenie finalneho vysledku do premennej
    final = "".join(vysledny_riadok)

    #vypisanie do suboru
    subor1.write(final)
    subor1.write("\n")

    #vyprazdnenie pouzivaneho zoznamu
    vysledny_riadok.clear()

for riadok in subor: #cyklus pre riadky v subore
    riadocek = riadok.split()

    #podmienka pre zistenie pozadovanych hodnot
    if daco == 0:
        sirka = int(riadocek[0])
        vyska = int(riadocek[1])

        #vypisanie hodnot do suboru
        subor1.write(str(sirka)+" "+str(vyska)+"\n")

    else:
        if daco > 0:
            spracuj_riadok()

    #zmena pomocnych premennych
    nieco = 0
    daco += 1

#vypisanie pozadovanych hodnot               
print("Šírka je:",sirka,"bodov")
print("Výška je:",vyska,"bodov")
print("Dokopy je:",sirka*vyska,"bodov")

#zatvorenie suborov
subor.close()
subor1.close()

