##adanie 1
#lista = ["Marta", "Zofia", "Anna", "Kamil"]

##a)
# lista.sort()
# print(lista)

##b)
# lista.append("Łukasz")
# lista.append("Michał")
# ostatnia_osoba = lista.pop()
# print(lista)
# print(ostatnia_osoba)

##c)
# lista.insert(3,"Andrzej")
# print(lista)

##d)
# print(lista)
# lista.reverse()
# print(lista*2)

##Zadanie 2
# zdanie = input("Podaj zdanie: ")
# print(zdanie)

# # a)
# litery = sorted(set(filter(str.isalpha, zdanie.lower())))
# alfabet = set('abcdefghijklmnopqrstuvwxyz')
# brakujące_litery = alfabet - set(litery)
# print("Występujące litery:", litery)
# print("Brakujące litery:", brakujące_litery)

# #b)
# filtrowanie = ''.join([char for i, char in enumerate(zdanie) if i % 2 == 0])
# print("Zdanie po usunięciu znaków na nieparzystych indeksach:", filtrowanie)

# #c)
# wielkie_litery = ' '.join(word.capitalize() for word in zdanie.split())
# print("Zdanie z wielkimi literami na początku:", wielkie_litery)

# #d)
# slowo = zdanie.split()
# dlugosc_slowa = max(slowo, key=len)
# print("Najdłuższe słowo:", dlugosc_slowa, "o długości:", len(dlugosc_slowa))

# #e)
# powtorzenia = ''.join(['@' if zdanie.count(char) > 1 else char for char in zdanie])
# print("Zdanie po zamianie powtarzających się znaków:", powtorzenia)

##Zadanie 2
# tekst = input("Podaj ciąg znaków: ")
# palindrom = tekst == tekst[::-1]
# if palindrom:
#      print("Podany ciąg znaków jest palindromem")
# else:
#      print("Podany ciąg znaków nie jest palindromem")

##Zadanie 3
# krotka1 = 5, 6, 7, 8
# krotka2 = 1, 2, 3, 4
# krotka3 = krotka1 + krotka2
# krotka4 = krotka3 *5
# print(krotka4)

##Zadanie 4
# n = int(input("Podaj n: "))
# x = int(input("Podaj x: "))
# str = [input(f"Podaj ciąg {i+1}: ") for i in range(n)]
# krotka = tuple(str)

# #a)
# total_chars = sum(len(s) for s in krotka)
# print("Ilość znaków w liście:", total_chars)

# #b)
# k_count = sum(s.count('k') for s in krotka)
# print("Ilość liter 'k':", k_count)

# #c)
# kt_count = sum(s.count('kt') for s in krotka)
# print("Ilość ciągów 'kt':", kt_count)

# #d)
# s = int(input("Podaj s: "))
# dlugosc_s = sum(1 for s in krotka if len(s) > s)
# print("Ilość ciągów dłuższych niż s:", dlugosc_s)

##Zadanie 5
# zakupy = {"chleb": 3.5, "mleko": 2.0, "masło": 5.0}
# print("Lista zakupów:", zakupy)
# print("Suma wydatków:", sum(zakupy.values()))

##Zadanie 6
rachunki = {"styczeń": 90, "luty": 110, "marzec": 130, "kwiecień": 150}

# #a)
# print("największa wartość: ", max(rachunki.values()))
# print("najmniejsza wartość: ",min(rachunki.values()))
# suma = sum(rachunki.values())
# print("suma: ",sum(rachunki.values()))
# srednia = suma / len(rachunki)
# print(srednia)

# #b)
# ostatni_miesiac = list(rachunki.values())[-1]
# if ostatni_miesiac > srednia:
#     print("Trzeba zacisnąć pasa")
# else:
#     print("Wszystko okay")

##Zadanie 7
# import random
# a = random.randint(3, 7)
# b = random.randint(3, 7)
# X = {random.randint(0, 10) for _ in range(a)}
# Y = {random.randint(0, 10) for _ in range(b)}
# print("Zbiór X:", X)
# print("Zbiór Y:", Y)
# X1 = {1, 2, 3,}
# Y1 = {1, 2, 3, 4, 6}
# # #a)
# print("Czy X zawiera 5? ", 5 in X)

# #b)
# print("Czy zbiór X jest podzbiorem zbioru Y? ", X.issubset(Y))

# #c)
# print("Czy zbiór Y jest podzbiorem zbioru X? ", Y.issubset(X))

# #d)
# print("Suma X i Y:", X.union(Y))

# #e)
# print("Różnica X i Y:", X.difference(Y))

# #f)
# print("Różnica Y i X:", Y.difference(X))

# #g)
# print("Różnica Y i X:", Y.intersection(X))

# # h)
# print("Najwyższy element w X i Y:", max(X.union(Y)))

# # i)
# pierwszy_element = next(iter(X))
# X.remove(pierwszy_element)
# Y.add(pierwszy_element)
# print("X po usunięciu pierwszego elementu:", X)
# print("Y po dodaniu elementu:", Y)

# # j)
# X.update(Y)
# print("X po dodaniu elementów Y:", X)

# # k)
# X.clear()
# Y.clear()
# print("X i Y po wyczyszczeniu:", X, Y)

###Zadania dodatkowe
# # Zadanie 8
# numbers = input("Podaj pięć cyfr oddzielonych przecinkiem: ").split(',')
# if len(numbers) != 5:
#     print("Niepoprawna ilość cyfr.")
# else:
#     numbers = list(map(int, numbers))
#     numbers_set = set(numbers)
#     random_element = random.choice(list(numbers_set))
#     print("Wylosowany element:", random_element)
#     if random_element == min(numbers_set) or random_element == max(numbers_set):
#         print("Wylosowany element jest najmniejszy lub największy.")

# # Zadanie 9
# for y in range(6):
#     for x in range(5):
#         if (x, y) in [(0, 1), (2, 3), (2, 4), (3, 4)]:
#             print("X", end=" ")
#         elif (x, y) in [(1, 1), (2, 0), (3, 3), (5, 3)]:
#             print("*", end=" ")
#         elif y == 2:
#             print("-", end=" ")
#         else:
#             print(".", end=" ")
#     print()

# Zadanie 11
# alfabet = list('abcdefghijklmnopqrstuvwxyz')
# n = int(input("Podaj n: "))
# lista = [alfabet[i:i + n] for i in range(0, len(alfabet), n)]
# print("Podzielona lista:", lista)