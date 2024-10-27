#Zadanie 1
a = 1 + 2
b = 1 + 4.5
c = 3 / 2
d = 4 / 2
e = 3 // 2
f = -3 // 2
g = 11 % 2
h = 2 ** 10
i = 8 ** (1/3)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
"""
Wyniki obliczeń dla poszczególnych operacji:
a. 1 + 2 = 3
   Operator '+' wykonuje dodawanie dwóch liczb.
b. 1 + 4.5 = 5.5
   Operator '+' wykonuje dodawanie dwóch liczb (liczba całkowita i zmiennoprzecinkowa).
c. 3 / 2 = 1.5
   Operator '/' wykonuje dzielenie dwóch liczb, zwracając wynik jako liczba zmiennoprzecinkowa.
d. 4 / 2 = 2.0
   Operator '/' wykonuje dzielenie dwóch liczb, zwracając wynik jako liczba zmiennoprzecinkowa.
e. 3 // 2 = 1
   Operator '//' wykonuje dzielenie całkowite, zwracając tylko część całkowitą wyniku.
f. -3 // 2 = -2
   Operator '//' wykonuje dzielenie całkowite, zwracając tylko część całkowitą wyniku.
g. 11 % 2 = 1
   Operator '%' wykonuje dzielenie z resztą, zwracając resztę z dzielenia dwóch liczb.
h. 2 ** 10 = 1024
   Operator '**' wykonuje potęgowanie, zwracając wynik jako potęgę liczby (2 do potęgi 10).
i. 8 ** (1/3) = 2.0
   Operator '**' wykonuje potęgowanie; w tym przypadku oblicza pierwiastek sześcienny z 8.
"""
#Zadanie 2
result = int(3.0)
print(result)
result = float(3)
print(result)
result = float("3")
print(result)
result = str(12.4)
print(result)
result = bool(0)
print(result)
"""
a. int(3.0)
Działanie: Funkcja int() konwertuje wartość na typ całkowity. W tym przypadku 3.0 (liczba zmiennoprzecinkowa) jest konwertowana na 3 (liczba całkowita).
Wynik: 3
b. float(3)
Działanie: Funkcja float() konwertuje wartość na typ zmiennoprzecinkowy. Tutaj 3 (liczba całkowita) jest konwertowana na 3.0 (liczba zmiennoprzecinkowa).
Wynik: 3.0
c. float("3")
Działanie: Funkcja float() może również konwertować ciągi znaków (stringi) na liczby zmiennoprzecinkowe. W tym przypadku "3" (ciąg znaków) jest konwertowany na 3.0 (liczba zmiennoprzecinkowa).
Wynik: 3.0
d. str(12.4)
Działanie: Funkcja str() konwertuje wartość na typ string (ciąg znaków). W tym przypadku 12.4 (liczba zmiennoprzecinkowa) jest konwertowana na "12.4" (ciąg znaków).
Wynik: "12.4"
e. bool(0)
Działanie: Funkcja bool() konwertuje wartość na typ logiczny (True/False). W Pythonie 0 jest interpretowane jako fałsz, więc wynik tej konwersji to False.
Wynik: False
"""
#Zadanie3
Imie = "Michał"
Kierunek ="Informatyka"
Uczelnia = "Wyższą Szkołę Informatyki i Zarządzania"

print("Nazywam się",Imie)
print("Mój kierunek to",Kierunek)
print("Uczęszczam na",Uczelnia)

#Zadanie4
print("Jak się nazywasz?")
imie = input("Wpisz tutaj swoje Imie:")
print("Cześć",imie+ ", witaj na zajęciach 😊😊")

#Zadanie5
bok1 = float (input("Podaj pierwszy bok: "))
bok2 = float (input("Podaj drugi bok: "))
pole = bok1 * bok2
obw = (bok1 *2) + (bok2 *2)
print("Obwód prostokąta wynosi:", obw)
"""
Pobranie długości boków prostokąta od użytkownika
Funkcja input() umożliwia wczytanie danych od użytkownika z klawiatury.
Zawarty tekst w nawiasach jest wyświetlany jako komunikat, aby użytkownik wiedział, co ma wpisać.
Użytkownik wprowadza dane, a funkcja zwraca je jako ciąg znaków (str).
Jak uzyskać efekt zadawania pytania użytkownikowi bez użycia print()?
Możesz to zrobić, przekazując argument do funkcji input(). Argument ten jest komunikatem, który zostanie
wyświetlony na ekranie przed wprowadzeniem danych, więc nie ma potrzeby stosowania dodatkowego print().
Użytkownik zobaczy pytanie lub prośbę o wprowadzenie danych w tym komunikacie.
"""
#Zadanie6
cena = 6.5
droga = float (input("Podaj droge w km pokonaną przez samochód: "))
spalanie = float (input("Podaj średnie spalanie l/100km: "))
zuzycie = droga * (spalanie / 100)
koszty = zuzycie * cena
print("Zużycie paliwa wynosi", zuzycie)
print("Koszt podrózy:", koszty,"zł")

#Zadaie7
import random
cena1 = 6.5
spalanie1 = float(input("Podaj średnie spalanie l/100km: "))
droga1 = random.randint(10, 1000)
zuzycie1 = droga1 * (spalanie1 / 100)
koszty1 = zuzycie1 * cena1
print("Droga wynosi:", droga1)
print("Zużycie paliwa wynosi",zuzycie1)
print("Koszt podrózy:", koszty1,"zł")

"""
Wartości generowane przez funkcję randint są pseudolosowe, ponieważ są one tworzone na podstawie algorytmu.
Używają one ziarna (seed), które determinują ich losowość.
Dzięki temu, jeśli użyjemy tego samego ziarna, otrzymamy te same wyniki.
Prawdziwe losowe wartości byłyby niemożliwe do przewidzenia i nie można ich odtworzyć.
"""
