# Lidur1: MinnstaTala2

while True:
    tala1 = int(input ('Sláðu inn tölu: '))
    tala2 = int(input ('Sláðu inn aðra tölu: '))
    tala3 = int(input ('Sláðu inn þriðju tölu: '))

    if tala1 != tala2 and tala2 != tala3 and tala1 != tala3:
        break
    else:
        print ("Ekki slá inn sömu tölu tvisvar")


if tala1 < tala2 and tala1 > tala3 or tala1 < tala3 and tala1 > tala2:
    print(tala1)

elif tala2 < tala1 and tala2 > tala3 or tala2 < tala3 and tala2 > tala1:
    print(tala2)

elif tala3 < tala1 and tala3 > tala2 or tala3 < tala2 and tala3 > tala1:
    print(tala3)

#Þessi kóði segir þér hver af þeim þremur tölum sem nnotandi slær inn er miðgildið. Kóðinn biður um 3 tölur og finnur svo út hver af þessum tölum er miðgildið með því að bera þær saman. Ég notaði if statements og gogga til þess að finna þetta út.


# Lidur2: Tommur_Sentimetra

cm_tommur = input("Sláðu inn A ef þú vilt breyta tommum í sentimetra og B ef þú vilt breyta sentimetrum í tommur: ")


if cm_tommur == "a" or cm_tommur == "A":
    tommur = int(input ("Sláðu inn tommur: "))
    print(tommur*2.54, "cm")

if cm_tommur == "b" or cm_tommur == "B":
    cm = int(input ("Sláðu inn sentimetra: "))
    print(cm/2.54, "tommur")

#Þessi kóði er reiknivél sem að breytir tommum í sentimetra eða öfugt. Hann gerir þetta með því að finna út hvort að notanda langar að breyta tommum í sentimetra eða öfugt. Kóðinn biður síðan um tommur eða sentimetra og deilir eða margfaldar töluni sem að notandi sló inn með 2.54

# Lidur3: Arstidir

manudur = int(input ("Sláðu inn númer mánaðar: "))


if manudur == 12 and manudur <= 2:
    print("Það er vetur!")

elif manudur >= 3 and manudur <= 5:
    print("það er vor!")

elif manudur >= 6 and manudur <= 8:
    print("það er sumar!")

elif manudur >= 9 and manudur <= 11:
    print("það er haust!")

elif manudur >= 13 or manudur <= 0:
    print("Rangur innsláttur")


if manudur >=1 and manudur <= 3:
    print("Nú er daginn tekið að lengja.")

elif manudur >=4 and manudur <= 5:
    print("Vorið er komið og grundirnar gróa.")

elif manudur >=6 and manudur <= 8:
    print("Núna er sumarið komið með blóm í haga.")

elif manudur >=9 and manudur <= 10:
    print("Núna er haustið gengið í garð.")

elif manudur >=11 and manudur <= 12:
    print("Núna styttist í jólin")

#Þessi kóði byður um númer mánaðar og prentar hvort mánuðurinn sé um vetur, vor, sumar eða haust. Hann prentar svo einhvern texta um mánuðinn sem að notandi stimplaði inn. Ég notaði if, else og elif statements til þess að finna út hvaða árstíð mánuðurinn sem notandi stimplaði inn er í. 

# Lidur4: NafnManadar

nafn = input("Hvað heitiru?: ")
kyn = input("Ertu kk eða kvk?: ")
t1 = int(input("Sláðu inn tölu: "))
t2 = int(input("Sláðu inn aðra tölu: "))



if kyn == "kk" or kyn == "KK":
    print("Blessaður", nafn)

elif kyn == "kvk" or kyn == "KVK":
        print("blessuð", nafn)

else:
    print("Blessaður eða blessuð ég veit ekki hvors kyns þú ert. ")

bigger = 0

smaller = 0

if t1 > t2:
    print(t1, "er stærri en", t2)
    bigger = t1
    smaller = t2
elif t1 < t2:
    print(t2, "er stærri en", t1)
    bigger = t2
    smaller = t1
elif t1 == t2:
    print ("Tölurnar eru jafnstórar.")

if (bigger - smaller) > 100:
    print ("Það er meira en hundrað á milli talnanna sem þú slóst inn.")

elif (bigger - smaller) < 100:
    print ("Það er minna en hundrað á milli talnanna sem þú slóst inn.")

#Þessi kóði prentar blessaður eða blessuð og síðan nafn notanda eftir því hvaða kyn notandi slær inn. Kóðinn prentar svo upplýsingar um tölurnar þrjár sem að notandi sló inn. Ég notaði if statements, else og elif statements til þess að finna út hvaða kyn notandi er og hvort það sé 100 á milli talnanna sem notandi sló inn.

# Lidur5:Talnabil

talnabil = int(input ("Sláðu inn tölu lægri en 0 en hærri en 10: "))

if talnabil <= 10 and talnabil >= 0:
    print ("Þessi tala er hvorki lægri en núll né hærri en tíu. ")

else:
    print ("Vel gert!!")

#Þessi kóði biður um tölu sem er minni en 0 eða stærri en 100 og prentar vel gert ef að þú gerir það. Annars prentar hún "Þessi tala er ekki lægri en núll eða hærri en tíu."