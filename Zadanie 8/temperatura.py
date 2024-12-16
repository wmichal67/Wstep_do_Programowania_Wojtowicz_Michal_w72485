# temperatura.py
def c_to_f(celsius):
    """Przelicza temperaturę z Celsjusza na Fahrenheita."""
    return celsius * 9 / 5 + 32

def f_to_c(fahrenheit):
    """Przelicza temperaturę z Fahrenheita na Celsjusza."""
    return (fahrenheit - 32) * 5 / 9

def c_to_k(celsius):
    """Przelicza temperaturę z Celsjusza na Kelwiny."""
    return celsius + 273.15
