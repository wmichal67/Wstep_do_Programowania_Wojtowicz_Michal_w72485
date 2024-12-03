import random
import math

# średnia geometryczna
def srednia_geometryczna(krotka):
    iloczyn = 1
    for liczba in krotka:
        iloczyn *= liczba
    return iloczyn ** (1 / len(krotka))

min = float(input("Podaj dolny zakres przedziału: "))
max = float(input("Podaj górny zakres przedziału: "))

# Generowanie krotki z 10 losowymi elementami z podanego przedziału
krotka = tuple(random.uniform(min, max) for _ in range(10))

srednia_geo = srednia_geometryczna(krotka)

print(f"Zdefiniowana krotka: {krotka}")
print(f"Średnia geometryczna krotki: {srednia_geo}")
