"""Uzupełnienie braków Zad 8 - 11 Lab2"""
# # Zadanie 8: Wyświetlanie wartości funkcji y = 2x^2 - 5x - 8 dla x ∈ [-4, 4] z krokiem 0.5
# def calculate_function():
#     x = -4
#     while x <= 4:
#         y = 2 * (x ** 2) - 5 * x - 8
#         print(f"x = {x:.1f}, y = {y:.2f}")
#         x += 0.5
#
# # Test
# calculate_function()

# # Zadanie 9: Pętla nieskończona z warunkiem zakończenia przy liczbie ujemnej
# def infinite_loop():
#     while True:
#         number = int(input("Podaj liczbę całkowitą (liczba ujemna zakończy pętlę): "))
#         if number < 0:
#             print("Podano liczbę ujemną. Zakończenie programu.")
#             break
#         print(f"Podano liczbę: {number}")
#
# # Test
# infinite_loop()

# # Zadanie 10: Wypisywanie liczb w przedziale od mniejszej do większej
# def print_numbers_in_range():
#     a = int(input("Podaj pierwszą liczbę: "))
#     b = int(input("Podaj drugą liczbę: "))
#
#     start = min(a, b)
#     end = max(a, b)
#
#     for i in range(start, end + 1):
#         print(i)
#
# # Test
# print_numbers_in_range()
#
# # Zadanie 11: Wypisywanie tylko liczb parzystych w przedziale, pomijanie nieparzystych
# def print_even_numbers_in_range():
#     a = int(input("Podaj pierwszą liczbę: "))
#     b = int(input("Podaj drugą liczbę: "))
#
#     start = min(a, b)
#     end = max(a, b)
#
#     for i in range(start, end + 1):
#         if i % 2 != 0:
#             continue
#         print(i)
#
# # Test
# print_even_numbers_in_range()
