# temperatura.py

# Funkcja przeliczająca temperaturę z Celsjusza na Fahrenheita
def c_to_f(celsius):
    return (celsius * 9/5) + 32

# Funkcja przeliczająca temperaturę z Fahrenheita na Celsjusza
def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Funkcja przeliczająca temperaturę z Celsjusza na Kelwiny
def c_to_k(celsius):
    return celsius + 273.15
