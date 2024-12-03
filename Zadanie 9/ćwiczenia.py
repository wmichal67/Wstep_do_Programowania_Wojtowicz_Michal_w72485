# ćwiczenia.py

# Sposób 1: Importowanie całego modułu f_mat
import f_mat

# a) Obliczanie kwadratu liczby 10
kwadrat_10 = f_mat.kwadrat(10)
print(f"Kwadrat liczby 10 wynosi: {kwadrat_10}")

# b) Obliczanie sześcianu liczby 3
szescian_3 = f_mat.szescian(3)
print(f"Sześcian liczby 3 wynosi: {szescian_3}")

# c) Dodawanie liczb 10 i 5
dodawanie = f_mat.dodaj(10, 5)
print(f"Suma liczb 10 i 5 wynosi: {dodawanie}")

# Sposób 2: Importowanie tylko wybranych funkcji
from f_mat import kwadrat, szescian, dodaj

# a) Obliczanie kwadratu liczby 10
kwadrat_10_2 = kwadrat(10)
print(f"Kwadrat liczby 10 (import bez prefiksu) wynosi: {kwadrat_10_2}")

# b) Obliczanie sześcianu liczby 3
szescian_3_2 = szescian(3)
print(f"Sześcian liczby 3 (import bez prefiksu) wynosi: {szescian_3_2}")

# c) Dodawanie liczb 10 i 5
dodawanie_2 = dodaj(10, 5)
print(f"Suma liczb 10 i 5 (import bez prefiksu) wynosi: {dodawanie_2}")
