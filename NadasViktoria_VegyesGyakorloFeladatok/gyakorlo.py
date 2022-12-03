import random

sorozat = [-3, 5, 11, -2, 4]

def masodik():
    szeparator = ","
    i = 0
    szoveg = ""
    while (i < len(sorozat)):
        if i == 4:
            szoveg += str(sorozat[i])
        else:
            szoveg += str(sorozat[i])+szeparator
        i += 1
    print(szoveg)

def szam_beszur():
   random_szam = random.randrange(5, 12)
   sorozat2 = [(-3 + int(random_szam)), 5, 11, -2, 4]
   print(sorozat2)

def utsoszam_csere():
    x = 0
    while not (100 > x >= 10 and x % 2 == 1):
        x = int(input("Adj meg egy páratlan 3-mal osztható 2 jegyű számot: "))
    sorozat[len(sorozat) - 1] = x
    print(sorozat)





