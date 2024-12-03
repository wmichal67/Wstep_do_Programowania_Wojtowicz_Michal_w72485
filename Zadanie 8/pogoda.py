# pogoda.py

# Importowanie modułu temperatura
import temperatura

# a) 21 stopni Celsjusza na Fahrenheita
celsius = 21
fahrenheit = temperatura.c_to_f(celsius)
print(f"{celsius} stopni Celsjusza to {fahrenheit} stopni Fahrenheita.")

# b) 89 stopni Fahrenheita na Celsjusza
fahrenheit = 89
celsius = temperatura.f_to_c(fahrenheit)
print(f"{fahrenheit} stopni Fahrenheita to {celsius} stopni Celsjusza.")

# c) 35 stopni Celsjusza na Kelwiny
celsius = 35
kelvins = temperatura.c_to_k(celsius)
print(f"{celsius} stopni Celsjusza to {kelvins} Kelwiny.")
