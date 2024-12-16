# obliczenia.py
import geometria  # Import modułu geometria

# Wywołanie funkcji z modułu geometria
promien = 16
obwod = geometria.obwod_kola(promien)
pole = geometria.pole_kola(promien)

print(f"Obwód koła o promieniu {promien}: {obwod}")
print(f"Pole koła o promieniu {promien}: {pole}")
