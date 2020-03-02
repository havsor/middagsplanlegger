# -*- coding: utf-8 -*-
"""
Ukeplanlegger for middagsmat
"""

import random


kjøttretter = open("kjøttretter.txt", encoding="utf-8")
kjøtt = kjøttretter.read().splitlines()

vegetarretter = open("vegetarretter.txt", encoding="utf-8")
vegetar = vegetarretter.read().splitlines()

fiskeretter = open("fiskeretter.txt", encoding="utf-8")
fisk = fiskeretter.read().splitlines()


ant_vegetar = int(input("Hvor mange vegetarmiddager ønsker du?"))
ant_fisk = int(input("Hvor mange fiskemiddager ønsker du?"))


def vegpop():
    return vegetar.pop(random.randint(0, len(vegetar)-1))
def fipop():
    return fisk.pop(random.randint(0, len(fisk)-1))
def kjøpop():
    return kjøtt.pop(random.randint(0, len(kjøtt)-1))

def nytt_forslag():
    ny = input("Vil du ha forslag til kjøtt, vegetar eller fisk?")
    gyldige_svar = ["kjøtt", "fisk", "vegetar"]
    if ny in gyldige_svar: 
        if ny == "kjøtt":
            print(kjøpop())
        elif ny == "fisk":
            print(fipop())
        elif ny == "vegetar":
            print(vegpop())  

while ant_vegetar + ant_fisk > 7:
    print()
    print("Oisann, dette ble vel litt for mange middager? Prøv igjen du. ")
    print()
    ant_vegetar = int(input("Hvor mange vegetarmiddager ønsker du?"))
    ant_fisk = int(input("Hvor mange fiskemiddager ønsker du?"))
        
veg = []
for i in range(ant_vegetar):
    veg.append(vegpop())


fi = []
for i in range(ant_fisk):
    fi.append(fipop())

if len(veg+fi) < 7:
    kjø = []
    for i in range(7-ant_vegetar-ant_fisk):
        kjø.append(kjøpop())

middager = veg + fi + kjø
random.shuffle(middager)

dager = ["Mandag ", "Tirsdag", "Onsdag ", "Torsdag", "Fredag ", "Lørdag ",
         "Søndag "]

print()
print("Dine middager denne uken: ")
print("--------------------------")


for i in range(7):
    print(dager[i], ": ", middager[i])


fler = "j"
while fler == "j":
    print()
    fler = input("Trenger du nye forslag? (j/n) ")
    if fler == "j":
        nytt_forslag()
    elif fler == "n":
        print()
        input("Så bra! Da er ukens middager klare. Trykk en tast for å avslutte.")
        



        


