# ## Zadanie 1 - Random
# import random
# import cmath
#
# ## a) "Szczęśliwy numerek"
# szczesliwy_numerek = random.randint(1, 30)  # Przyjmuje, że grupa ma maksymalnie 30 osób
# print("Szczęśliwy numerek: ", szczesliwy_numerek)
#
# # b) Wylosowanie szczęśliwego rocznika
# roczniki = [2000, 2001, 2002, 2003, 2004]
# szczesliwy_rocznik = random.choice(roczniki)
# print("Szczęśliwy rocznik: ", szczesliwy_rocznik)
#
# ## c) Losowanie totolotka
# liczby = list(range(1, 50))
# wynik = random.sample(liczby, 6)
# print("Wynik totolotka: ", wynik)
#
# ## Zadanie 2 - Math
# import math
#
# ## a) Pierwiastek kwadratowy z 81
# print("\u221A81 =", math.sqrt(81))
#
# ## b) Potęga 8^10
# print("8^10 =", math.pow(8, 10))
#
# ## c) \u221A2 + \u221A3 + \u221A6
# print("\u221A2 + \u221A3 + \u221A6 =", math.sqrt(2) + math.sqrt(3) + math.sqrt(6))
#
# ## d) \u221A(-5) (rzeczywista część liczby zespolonej)
# print("\u221A(-5) =", cmath.sqrt(-5))
#
# ## e) 3\u221A125
# print("3\u221A125 =", math.pow(125, 1/3))
#
# ## Zadanie 3 - Time
# import time
#
# def sekundnik(czas):
#     for i in range(czas, 0, -1):
#         print(f"Pozostalo: {i} sekund")
#         time.sleep(1)
#
# # Przykład: sekundnik(5)
#
# ## Zadanie 4 - Datetime
# from datetime import datetime, timedelta
#
# # Ostatnie laboratoria
# ostatnie_laby = datetime(2024, 12, 9)
# obecna_data = datetime.now()
# il_dni = (obecna_data - ostatnie_laby).days
# print("Od ostatnich laboratoriów upłynęło: ", il_dni, "dni")
#
# # Czas do kolokwium
# kolokwium = datetime(2024, 12, 23)
# pozostalo = (kolokwium - obecna_data).days
# print("Do kolokwium pozostało: ", pozostalo, "dni")
#
# ## Zadanie 5 - Keyword
# import keyword
# slowa = ["for", "print", "break", "done", "bad"]
# for slowo in slowa:
#     print(f"Czy '{slowo}' jest słowem kluczowym? ", keyword.iskeyword(slowo))
#
# ## Zadanie 6 - dir() funkcji
# print("Funkcje w module math:", dir(math))
# print("Funkcje w module keyword:", dir(keyword))
#
# ## Zadanie 7 - Moduł geometria
# PI = 3.14159
#
# def obwod_kola(promien):
#     return 2 * PI * promien
#
# def pole_kola(promien):
#     return PI * promien**2
#
# # Przykład użycia
# r = 16
# print("Obwód koła:", obwod_kola(r))
# print("Pole koła:", pole_kola(r))
#
# ## Zadanie 8 - Moduł temperatura
# def c_to_f(celsius):
#     return celsius * 9/5 + 32
#
# def f_to_c(fahrenheit):
#     return (fahrenheit - 32) * 5/9
#
# def c_to_k(celsius):
#     return celsius + 273.15
#
# # Przykład użycia
# print("21°C na Fahrenheita:", c_to_f(21))
# print("89°F na Celsjusza:", f_to_c(89))
# print("35°C na Kelwiny:", c_to_k(35))
#
# ## Zadanie 9 - Moduł f_mat.py i ćwiczenia.py
# def kwadrat(x):
#     return x ** 2
#
# def szescian(x):
#     return x ** 3
#
# def dodaj(a, b):
#     return a + b
#
# # Przykłady
# print("Kwadrat 10:", kwadrat(10))
# print("Sześcian 3:", szescian(3))
# print("Dodaj 10 i 5:", dodaj(10, 5))
#
# ## Zadanie 10 - Krotka i średnia geometryczna
# from functools import reduce
#
# zakres_od = int(input("Podaj dolny zakres: "))
# zakres_do = int(input("Podaj górny zakres: "))
# krotka = tuple(random.randint(zakres_od, zakres_do) for _ in range(10))
# srednia_geo = reduce(lambda x, y: x * y, krotka) ** (1/len(krotka))
# print("Krotka:", krotka)
# print("Średnia geometryczna:", srednia_geo)
#
# ## Zadanie 11 (Zadania dodatkowe)- Gra w zgadywanie liczby
# def gra():
#     print("Witaj w grze!")
#     zakres_od = int(input("Podaj początek zakresu: "))
#     zakres_do = int(input("Podaj koniec zakresu: "))
#     liczba = random.randint(zakres_od, zakres_do)
#     for i in range(3):
#         proba = int(input("Zgadnij liczbę: "))
#         if proba < liczba:
#             print("Za mało!")
#         elif proba > liczba:
#             print("Za dużo!")
#         else:
#             print("Brawo, zgadłeś!")
#             return
#     print("Przegrałeś! Liczba to:", liczba)
#
# ## Zadanie 12 - Pole trójkąta ostrokątnego
# def pole_trojkata(a, b, kat):
#     if kat <= 0 or kat >= 90:
#         return "To nie jest trójkąt ostrokątny."
#     pole = 0.5 * a * b * math.sin(math.radians(kat))
#     return pole
#
# ## Zadanie 13 - Obliczenia na datach
# def oblicz_daty(rok, miesiac, dzien):
#     data = datetime(rok, miesiac, dzien)
#     dzien_roku = data.timetuple().tm_yday
#     numer_tygodnia = data.isocalendar()[1]
#     dwa_tygodnie_przed = data - timedelta(weeks=2)
#     dwa_tygodnie_po = data + timedelta(weeks=2)
#     najblizsza_niedziela = data + timedelta(days=(6 - data.weekday()))
#     czas_unixowy = int(data.timestamp())
#
#     print(f"Dzień roku: {dzien_roku}")
#     print(f"Numer tygodnia: {numer_tygodnia}")
#     print(f"Data dwa tygodnie przed: {dwa_tygodnie_przed}")
#     print(f"Data dwa tygodnie po: {dwa_tygodnie_po}")
#     print(f"Najbliższa niedziela: {najblizsza_niedziela}")
#     print(f"Czas unixowy: {czas_unixowy}")
#
# # Przykład
# # oblicz_daty(2024, 12, 16)
