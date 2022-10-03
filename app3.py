#herhaling leerstof
#string -> tekst
#int -> geheel getal
#float -> kommagetal
#boolean -> true or false

x = "5"
y = 5
z = 5.0
# alle drie hetzelfde cijfer

# input("leeftijd: ") -> geeft een string
# int(input("leeftijd: ")) -> geeft een integer
# maar moet vooraf gegaan worden door een variabele
# vb. mijn_leeftijd = int(input("leeftijd: "))
# print(mijn_leeftijd)

#door het gebruik van een funtie kan je alleen deze laten runnen.
def print_leeftijd(a): #haakjes dienen om aan te geven dat er data wordt meegegeven.
    #mijn_leeftijd = int(input("leeftijd: "))
    print(a)

b = int(input("leeftijd: "))
print_leeftijd(b) # om de functie aan te roepen, gaat dus naar lijn 19 
#waarbij a overschreven wordt door b

def print_leeftijd(a,b): #haakjes dienen om aan te geven dat er data wordt meegegeven.
    #mijn_leeftijd = int(input("leeftijd: "))
    print(a)
    print(b)

k = int(input("leeftijd: "))
z = int(input("lengte: "))
print_leeftijd(k,z) # om twee parameters mee te geven.

def old_enough_to_drive(leeftijd):
    if leeftijd > 18:
        print ("oud genoeg om te rijden")
    else:
        print("mag nog niet rijden")

k = int(input("leeftijd: "))
old_enough_to_drive(k)

#9**0.5 (tot de macht 0.5 is gelijk aan de vierkantswortel)
# import math moet je dan helemaal bovenaan schrijven
def calc_sqrt(getal):
    x = math.sqrt(getal)
    print(x)

calc_sqrt(k)
# kan ook, eenvoudiger
def calc_sqrt(getal):
    getal = math.sqrt(int(input("getal: "))
    print(getal)

calc_sqrt(getal)

#oefening
#een functie die een lijst (getallen) mee krijgt
# over deze lijst loopt
#checkt hoeveel getallen kleiner zijn dan 5
# print het aantal getallen dat kleiner is dan 5



def getallen_kleinder_dan_vijf(array):
    count = 0
    for i in array:
        if i < getal:
            count += 1

x= [2, 4, 6, 8, 10]
y= int(input("vergeleken getal: "))
getallen_kleiner_dan_vijf(x,y)
