# pogoda.py
import temperatura  # Import modułu temperatura

# Wywołanie funkcji z modułu temperatura
celsius = 21
fahrenheit = 89
kelvin = 35

temp_f = temperatura.c_to_f(celsius)
temp_c = temperatura.f_to_c(fahrenheit)
temp_k = temperatura.c_to_k(kelvin)

print(f"{celsius}°C to {temp_f:.2f}°F")
print(f"{fahrenheit}°F to {temp_c:.2f}°C")
print(f"{kelvin}°C to {temp_k:.2f}K")
