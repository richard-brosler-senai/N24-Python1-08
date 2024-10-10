"""
Programa para calcular fatorial
Author: Richard Brosler
Version: 2024-10-09
"""
from funcoes import montar_tela, fatorial, min_max
# Montando minha tela
montar_tela(colunas=60,titulo="Programa para calcular fatorial")
numero = int(input("Digite um valor para calcular: "))
# Vamos calcular o fatorial
# exemplo 5! => 5 x 4 x 3 x 2 x 1 => 120

print("Resultado =",f"{fatorial(numero):.4f}")
a, b = min_max(5,9,3)
print(a, b)