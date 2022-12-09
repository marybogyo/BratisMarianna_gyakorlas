import random
#Készíts egy sorozat nevű tömböt
# a következő elemekkel: -3, 5, 11, -2, 4
sorozat = [-3, 5, 11, -2, 4]
def kiiras(kiir = ""):
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
def prim(szam):
    i = 2
    while(i< szam and szam % i != 0):
        i+=1
    return i==szam
print(prim(5))
print(prim(22))

def ketjegy():
    i = 0
    v = sorozat[0]
    while not (v>=10):
        i += 1
        v = sorozat[i]
    print(f"Az első kétjegyű szám {i}, értke: {v}")

def hany_primszam():
    i = 0
    db = 0

    while i < len(sorozat):
        if prim(sorozat[i]):
            db +=1
        i += 1
    print(f"Prím szám összesen: {db}")


