# cwiczenia.py

# Import całego modułu f_mat
import f_mat

# Import wybranych funkcji z modułu f_mat
from f_mat import kwadrat, szescian, dodaj

# Testowanie funkcji poprzez import całego modułu
print("=== Import całego modułu ===")
print("Kwadrat liczby 10:", f_mat.kwadrat(10))
print("Sześcian liczby 3:", f_mat.szescian(3))
print("Suma liczb 10 i 5:", f_mat.dodaj(10, 5))

# Testowanie funkcji poprzez import wybranych funkcji
print("\n=== Import wybranych funkcji ===")
print("Kwadrat liczby 10:", kwadrat(10))
print("Sześcian liczby 3:", szescian(3))
print("Suma liczb 10 i 5:", dodaj(10, 5))
