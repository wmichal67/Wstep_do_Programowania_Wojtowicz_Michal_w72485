import random

##Zadanie 1
##a)
# szczesliwy_numerek = random.randint(1, 22)
# print(szczesliwy_numerek)

##b)
# roczniki = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
#
# szczesliwy_rocznik = random.choice(roczniki)
# print(szczesliwy_rocznik)

##c)
# # Tworzymy listę liczb od 1 do 49
# liczby = list(range(1, 50))
#
# # Losowanie 6 unikalnych liczb z zakresu 1-49
# wylosowane_liczby = random.sample(liczby, 6)
#
# # Wyświetlenie wylosowanych liczb
# print(wylosowane_liczby)

##Zadanie 2
import math
##c)
# w1 = math.sqrt(2) +  math.sqrt(3) + math.sqrt(6)
# # print(math.sqrt(2))
# # print(math.sqrt(3))
# # print(math.sqrt(6))
# w1 = math.floor(w1)
# w1 = math.ceil(w1)
# ##jest jeszcze poza math round()
# print(w1)

##Zadanie 3
# import time
#
# def sekundnik(czas):
#
#     while czas > 0:
#         print(f'Pozostało {czas} sekund.')
#         time.sleep(1)  # Czekaj przez 1 sekundę
#         czas -= 1
#     print("Czas minął!")
#
# czas_do_odliczenia = int(input("Podaj czas w sekundach: "))
# sekundnik(czas_do_odliczenia)

##Zadanie 4
# import datetime
#
#
# def oblicz_dni():
#     ostatnie_laboratoria = datetime.date(2024, 11, 19)
#     kolokwium = datetime.date(2025, 1, 7)  # Data kolokwium
#     # Dzisiejsza data
#     dzisiaj = datetime.date.today()
#     # Obliczamy ile dni upłynęło od ostatnich laboratoriów
#     dni_od_laboratoriow = (dzisiaj - ostatnie_laboratoria).days
#     # Obliczamy ile dni zostało do kolokwium
#     dni_do_kolokwium = (kolokwium - dzisiaj).days
#
#     print(f"Od ostatnich laboratoriów minęło: {dni_od_laboratoriow} dni.")
#     print(f"Do kolokwium zostało: {dni_do_kolokwium} dni.")
#
#     print(f"Data dzisiaj: {dzisiaj.strftime('%d %B %Y')}")
#     print(f"Data kolokwium: {kolokwium.strftime('%d %B %Y')}")
#
# oblicz_dni()



