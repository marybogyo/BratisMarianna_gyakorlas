import random
#Készíts egy sorozat nevű tömböt
# a következő elemekkel: -3, 5, 11, -2, 4
sorozat = [-3, 5, 11, -2, 4]
def kiiras(kiir):
    i = 0

    szamok = ""
    while (i < len(sorozat)-1):
        szamok += str(sorozat[i]) + kiir
        i += 1
    print(szamok + str(i))

def vel():

    vel = int(random.random() * 7) + 5
    print(vel + sorozat[0])
    sorozat[0] += vel
    print(kiiras("*"))

def utolso():
    szam = int(input("Adj meg egy páratlan számot, ami 3-al osztható: "))
    while not((szam>= 10) and (szam <= 99) and (szam % 2 == 1) and (szam % 3 == 0)):
        szam = int(input("Adj meg egy páratlan számot, ami 3-al osztható:"))
    print(szam)
    sorozat[len(sorozat)-1] = szam
    print(sorozat)


#Egy paraméterében megadott számról eldönti, hogy prím-e?
def prim():
    szam = int(input("Adj meg egy prím számot: "))


