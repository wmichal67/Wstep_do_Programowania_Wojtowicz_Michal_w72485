##Zadanie 1
# import math
# def promien_kola(r):
#     if r > 0:
#         pole = math.pi * r**2
#         print("Pole koła wynosi: ", pole)
#     else:
#         print("podaj odpowiedni promień")
# r = 5
# promien_kola(r)

#Zadanie 2
# def pole_trapezu(a, b, h):
#     pole = (a + b)*h/2
#     if a > 0 and b > 0 and h > 0 and a !=b :
#         print("Pole trapezu wynosi:",pole)
#     else:
#         print("Podaj prawidłowe dane")
# a = 5
# b = 6
# h = 5
# pole_trapezu(a, b, h)

##Zdanie 3
# def czy_dodatnia(x):
#     if x > 0:
#         print("X: Jest liczbą dodatnią")
#     elif x == 0:
#         print("X: Jest równy zero")
#     else:
#         print("X: Jest liczbą ujemną")
# x = 0
# czy_dodatnia(x)

##Zadanie 4
# def BMI(waga, wzrost):
#     BMI = waga/(wzrost)**2
#     if BMI < 18.5:
#         print("Masz niedowagę.")
#     #elif BMI 18.5 <= BMI < 24.9:
#     elif BMI >= 18.5 and BMI < 24.9:
#         print("Masz prawidłową wagę.")
#     elif BMI >= 25 and BMI < 29.9:
#         print("Masz nadwagę.")
#     else:
#         print("Masz otyłość.")
#         print("Twoje BMI wynosi", BMI)
# waga = 77
# wzrost = 1.76
# BMI(waga, wzrost)

##Zadanie 5
# def sredia(liczby):
#     if len(liczby) == 0:
#         return "Lista jest pusta, nie można obliczyć średniej."
#     else:
#         suma = sum(liczby)
#         srednia = suma / len(liczby)
#         return srednia
# liczby = [2, 5, 8, 12]
# wynik = sredia(liczby)
# print("Średia liczb", liczby, "wynosi: ", wynik)

##Zadanie 6
# def dane(imie, wiek=20):
#     """
#     Funkcja wypisuje na ekranie imię oraz wiek podane jako argumenty.
#     Jeśli wiek nie zostanie podany, przyjmuje wartość domyślną 20.
#     """
#     print(f"Imię: {imie}, Wiek: {wiek}")
#
# dane("Anna", )
#
# print(dane.__doc__)

##Zadanie 7
# import math
#
# def pole_trojkata(a, b, c):
#     # Warunek na istnienie trójkąta
#     if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
#         # Półobwód
#         s = (a + b + c) / 2
#         # Pole z wzoru Herona
#         pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
#         return pole
#     else:
#         return "Nie można utworzyć trójkąta z podanych boków!"
#
# # Przykłady użycia
# print(pole_trojkata(3, 4, 5))  # Wynik: 6.0
# print(pole_trojkata(1, 2, 3))  # Wynik: "Nie można utworzyć trójkąta z podanych boków!"
# print(pole_trojkata(-3, 4, 5))  # Wynik: "Nie można utworzyć trójkąta z podanych boków!"

##Zadanie 8
# def potega(a, n):
#     # Warunek bazowy: każda liczba do potęgi 0 to 1
#     if n == 0:
#         return 1
#     # Jeśli wykładnik jest ujemny, zamieniamy na dodatni i odwracamy wynik
#     elif n < 0:
#         return 1 / potega(a, -n)
#     # Rekurencja: a^n = a * a^(n-1)
#     else:
#         return a * potega(a, n - 1)
#
#
# # Przykłady użycia
# print(potega(2, 3))  # Wynik: 8 (2^3)
# print(potega(5, 0))  # Wynik: 1 (5^0)
# print(potega(2, -2))  # Wynik: 0.25 (2^-2)

##Zadanie 9
# def fibonacci(n):
#     # Warunki bazowe
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     # Rekurencja: F(n) = F(n-1) + F(n-2)
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# # Przykłady użycia
# print(fibonacci(0))  # Wynik: 0
# print(fibonacci(1))  # Wynik: 1
# print(fibonacci(7))  # Wynik: 13
# print(fibonacci(10))  # Wynik: 55

##Zadanie 10
# def hanoi(n, start, pomocniczy, cel):
#     if n == 1:
#         # Warunek bazowy: przenieś 1 krążek bezpośrednio
#         print(f"Przenieś krążek z {start} na {cel}")
#     else:
#         # Przenieś n-1 krążków na pręt pomocniczy
#         hanoi(n - 1, start, cel, pomocniczy)
#         # Przenieś największy krążek na pręt docelowy
#         print(f"Przenieś krążek z {start} na {cel}")
#         # Przenieś n-1 krążków z pręta pomocniczego na pręt docelowy
#         hanoi(n - 1, pomocniczy, start, cel)
#
# # Przykład użycia
# hanoi(2, "A", "B", "C")

##Zadanie 11
# def odwracanie_stringa(str):
#     # Warunek bazowy: pusty string lub jeden znak jest już "odwrócony"
#     if len(str) <= 1:
#         return str
#     # Rekurencja: ostatni znak + odwrócony reszta stringa
#     else:
#         return str[-1] + odwracanie_stringa(str[:-1])
#
#
# # Przykłady użycia
# print(odwracanie_stringa("hello"))  # Wynik: "olleh"
# print(odwracanie_stringa("python"))  # Wynik: "nohtyp"


