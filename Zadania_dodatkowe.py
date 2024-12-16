"""Zadania dodatkowe Lab1/2/3/4"""
####Lab 1
# # Zadanie 15: Rozwiązywanie równania liniowego 0 = ax + b
# def solve_linear_equation(a, b):
#     if a == 0:
#         if b == 0:
#             return "Równanie ma nieskończenie wiele rozwiązań."
#         else:
#             return "Równanie nie ma rozwiązania."
#     else:
#         x = -b / a
#         return f"Rozwiązanie równania to x = {x}"
#
# # Test
# print(solve_linear_equation(2, -4))
#
# # Zadanie 16: Obwód i pole trójkąta o danych bokach
# def triangle_properties(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         perimeter = a + b + c
#         s = perimeter / 2
#         area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#         return f"Obwód: {perimeter}, Pole: {area}"
#     else:
#         return "Podane boki nie tworzą trójkąta."
#
# # Test
# print(triangle_properties(3, 4, 5))
#
# # Zadanie 17: Sprawdzenie wielkości litery
# def check_letter_case(letter):
#     if len(letter) != 1 or not letter.isalpha():
#         return "Podaj dokładnie jeden znak będący literą."
#     if letter.islower():
#         return "Litera jest mała."
#     else:
#         return "Litera jest duża."
#
# # Test
# print(check_letter_case("A"))
#
# # Zadanie 19: Zamiana wielkości litery
# def swap_case(letter):
#     if len(letter) != 1 or not letter.isalpha():
#         return "Podaj dokładnie jeden znak będący literą."
#     swapped = letter.lower() if letter.isupper() else letter.upper()
#     return f"Po zamianie: {swapped}"
#
# # Test
# print(swap_case("a"))
#
# # Zadanie 20: Obliczanie wyniku drużyny piłkarskiej
# def calculate_team_score(goals, bonus):
#     points = goals * 10
#     if goals > 5:
#         points += 5
#     if goals > 10:
#         points += 10
#     points += bonus
#     return f"Łączny wynik drużyny: {points} punktów"
#
# # Test
# print(calculate_team_score(6, 2))

####Lab 2
# # Zadanie 12: Obliczanie średniej liczby punktów w grupie
# def average_points():
#     """Obliczanie średniej liczby punktów dla n studentów."""
#     n = int(input("Podaj liczbę studentów w grupie: "))
#     total_points = 0
#     i = 0
#
#     while i < n:
#         points = float(input(f"Podaj liczbę punktów dla studenta {i + 1}: "))
#         if 0 <= points <= 100:
#             total_points += points
#             i += 1
#         else:
#             print("Nieprawidłowa liczba punktów. Podaj wartość z zakresu 0-100.")
#
#     average = total_points / n
#     print(f"Średnia liczba punktów w grupie: {average:.2f}")
#
#
# # Zadanie 13: Wersja z continue i break
# def average_points_with_continue_and_break():
#     """Obliczanie średniej liczby punktów z obsługą błędów za pomocą continue i break."""
#     n = int(input("Podaj liczbę studentów w grupie: "))
#     total_points = 0
#     i = 0
#
#     while True:
#         if i == n:
#             break
#
#         points = float(input(f"Podaj liczbę punktów dla studenta {i + 1}: "))
#         if points < 0 or points > 100:
#             print("Nieprawidłowa liczba punktów. Pomijam tego studenta.")
#             continue
#
#         total_points += points
#         i += 1
#
#     average = total_points / n
#     print(f"Średnia liczba punktów w grupie: {average:.2f}")
#
#
# # Zadanie 14: Program z pierwiastkiem kwadratowym i sprawdzaniem liczby dodatniej
# def square_root_program():
#     """Wczytuje liczbę i wyświetla jej pierwiastek kwadratowy, jeśli jest dodatnia."""
#     import math
#
#     while True:
#         try:
#             number = float(input("Podaj liczbę: "))
#             if number < 0:
#                 print("Dziękujemy za skorzystanie z naszej aplikacji.")
#                 break
#
#             print(f"To jest liczba dodatnia. Pierwiastek kwadratowy: {math.sqrt(number):.2f}")
#         except ValueError:
#             print("Błąd: Podaj poprawną liczbę.")
#
#
# # Wywołania przykładowych funkcji
# # average_points()
# # average_points_with_continue_and_break()
# # square_root_program()

####Lab3
# # Zadanie 8: Operacje na podanych cyfrach
# def handle_numbers():
#     """Poproś użytkownika o podanie 5 cyfr rozdzielonych przecinkiem, wykonaj operacje na nich."""
#     user_input = input("Podaj 5 cyfr rozdzielonych przecinkiem: ")
#     numbers = user_input.split(',')
#
#     # Sprawdzenie, czy podano dokładnie 5 cyfr
#     if len(numbers) != 5:
#         print("Błąd: Musisz podać dokładnie 5 cyfr.")
#         return
#
#     # Konwersja na liczby
#     try:
#         numbers = list(map(int, numbers))
#     except ValueError:
#         print("Błąd: Wszystkie wartości muszą być liczbami.")
#         return
#
#     # Zmiana tablicy na zbior dla losowości
#     import random
#     numbers_set = set(numbers)
#     random_element = random.choice(list(numbers_set))
#     print(f"Wylosowany element: {random_element}")
#
#     # Sprawdzenie, czy element jest najmniejszy lub największy
#     if random_element == min(numbers):
#         print("Wylosowana liczba jest najmniejsza.")
#     elif random_element == max(numbers):
#         print("Wylosowana liczba jest największa.")
#
#
# # Zadanie 9: Rysowanie pola gry
# def draw_game_board():
#     """Narysuj pole gry o rozmiarze 6x5 z przeciwnikami, monetami i rzeką."""
#     # Definicje obiektów na planszy
#     enemies = [(0, 1), (2, 3), (2, 4), (3, 4)]
#     coins = [(1, 1), (2, 0), (3, 3), (5, 3)]
#     river_y = 2
#
#     for y in range(6):
#         row = ""
#         for x in range(5):
#             if (y, x) in enemies:
#                 row += "x"
#             elif (y, x) in coins:
#                 row += "*"
#             elif y == river_y:
#                 row += "="
#             else:
#                 row += "."
#         print(row)
#
#
# # Zadanie 10: (Jeśli było pominięte, zostawiamy na później) Zadanie nie zostało zdefiniowane
#
# # Zadanie 11: Podział listy liter alfabetu na podlisty
# def split_alphabet():
#     """Podziel listę alfabetu na podlisty co n-ty element."""
#     import string
#     alphabet = list(string.ascii_lowercase)
#
#     try:
#         n = int(input("Podaj wartość n (podział co n-ty element): "))
#     except ValueError:
#         print("Błąd: Podaj liczbę całkowitą.")
#         return
#
#     if n <= 0:
#         print("Błąd: Liczba n musi być większa od zera.")
#         return
#
#     # Podział listy
#     sublists = [alphabet[i:i + n] for i in range(0, len(alphabet), n)]
#     print(sublists)
#
#
# # Wywołania przykładowych funkcji
# handle_numbers()
# draw_game_board()
# split_alphabet()

#####Lab 4
# #Zadanie 12: Funkcja określająca płeć na podstawie imienia
# def determine_gender(name):
#     """Funkcja zwraca "kobieta" lub "mężczyzna" na podstawie imienia."""
#     female_names = ["Anna", "Maria", "Katarzyna", "Ewa", "Zofia"]
#     return "kobieta" if name in female_names else "mężczyzna"
#
# # Tworzenie słownika
# names = ["Anna", "Piotr", "Maria", "Jan", "Zofia"]
# gender_dict = {name: determine_gender(name) for name in names}
# print(gender_dict)  # Output: {'Anna': 'kobieta', 'Piotr': 'mężczyzna', ...}
#
#
# # Zadanie 13: Funkcja zwracająca wspólne elementy w dwóch sekwencjach
# def common_elements(seq1, seq2):
#     """Funkcja zwraca listę wspólnych elementów dla dwóch sekwencji."""
#     return list(set(seq1) & set(seq2))
#
# # Przykład
# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]
#
#
# # Zadanie 14: Funkcja obliczająca NWD (największy wspólny dzielnik)
# def gcd(a, b):
#     """Funkcja oblicza NWD (największy wspólny dzielnik) za pomocą algorytmu Euklidesa."""
#     while b:
#         a, b = b, a % b
#     return a
#
# # Przykład
# print(gcd(48, 18))  # Output: 6
#
#
# # Zadanie 15: Funkcja sprawdzająca, czy dane słowo jest palindromem
# def is_palindrome(word):
#     """Funkcja sprawdza, czy dane słowo to palindrom."""
#     word = word.lower().replace(" ", "")  # Ignorowanie spacji i wielkości liter
#     return word == word[::-1]
#
# # Przykład
# print(is_palindrome("kajak"))  # Output: True
# print(is_palindrome("python"))  # Output: False
#
#
# # Zadanie 16: Funkcja sprawdzająca, czy dwa słowa są anagramami
# def are_anagrams(word1, word2):
#     """Funkcja sprawdza, czy dwa słowa są anagramami."""
#     return sorted(word1.lower()) == sorted(word2.lower())
#
# # Przykład
# print(are_anagrams("listen", "silent"))  # Output: True
# print(are_anagrams("python", "java"))  # Output: False
#
#
# # Zadanie 17: Funkcja o zmiennej liczbie parametrów
# def display_and_max(*args):
#     """Funkcja wyświetla parametry i zwraca ich maksymalną wartość."""
#     print("Podane parametry:", args)
#     return max(args) if args else None
#
# # Przykład
# print(display_and_max(3, 5, 7, 2))  # Output: Podane parametry: (3, 5, 7, 2) i maksymalna: 7
