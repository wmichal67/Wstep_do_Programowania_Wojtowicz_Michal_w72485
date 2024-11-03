##Zadanie 1
##a)
#for i in range (1, 101,):
#    print(i, end=", ")

##b)
#for i in range (100, -1, -1 ):
#    print(i, end=", ")

##c)
#for i in range(7,78,7):
#    print(i, end=", ")

##d)
#for i in range(20,-1,-2):
#    print(i, end=", ")

##Zadanie 2
##a)
#n = int(input("Podaj liczbę wierszy: "))
#for i in range(n):
#    print(" * " * 3)

##b)
#n = int(input("Podaj liczbę wierszy: "))
#for i in range(1, n + 1):
#    print(" * " * i )

##c)
#n = int(input("Podaj liczbę wierszy: "))
#for i in range(1, n + 1):
#    print(" " * (n - i) + "* " * i)

##Zadanie 3
#n = int(input("Podaj liczbę elementów (n): "))
#a = float(input("Podaj pierwszy element (a): "))
#r = float(input("Podaj różnicę (r): "))

#for i in range(n):
#    print(a + i * r, end=", ")
#print()

##Zadanie 4
#n = int(input("Podaj liczbę do obliczenia silni: "))
#silnia = 1
#for i in range(1, n + 1):
#    silnia *= i
#print(f"{n}! = {silnia}")

##Zadanie 5
##a)
#tekst = "Rzeszów jest piękny"
#print(tekst[0])
##b)
#print(tekst[6], tekst[9], tekst[12], tekst[1])

##Zadanie 6
#tresc ="Python jest super"
##a)
#print(tresc[0])
##b)
#print(tresc[-1])
##c)
#print(tresc[0::2])
##d)
#print(tresc[1::3])
##e)
#print(tresc[10:])
##f)
#print(tresc[-1::-1])
##Zadanie 7
##a)
#Imie = input("Podaj Imie: ")
#print("Witaj", Imie)
##b)
#wiek = float(input("Podaj swój wiek: "))
#print("Twój wiek to:", wiek)
##c)
#imie = (input("Podaj imie: "))
#nazwisko = (input("Podaj nazwisko: "))
#print(f"Inicjały to: {imie[0]}{nazwisko[0]}")
##d)
#tekst = input("podaj dowolny łańcuch: ")
#print(f"Twój łańcuch: {tekst * 5}")
##e)
#lancuch1 = input("podaj pierwszy łańcuch: ")
#lancuch2= input("podaj drugi łańcuch: ")
#print(f"Trzeci łańcuch: {lancuch1+lancuch2}")
##f)
#lancuch1 = input("podaj pierwszy łańcuch: ")
#lancuch2= input("podaj drugi łańcuch: ")
#pol1 = len(lancuch1) // 2
#pol2 = len(lancuch2) // 2
#print(f"Trzeci łańcuch: {lancuch1[:pol1]+lancuch2[pol2:]}")