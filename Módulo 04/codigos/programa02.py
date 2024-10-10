"""
Programa para verificar se um número é primo
Author: Richard Brosler
Version: 2024-10-09
"""
from funcoes import montar_tela, is_primo
while True:
    montar_tela('Programa para verificar número primo',60)
    numero = int(input("Digite o número (0-fim): "))
    if numero == 0: break
    if is_primo(numero): print("O número é primo")
    else: print("O número não é primo")
    input("Tecle enter para continuar... ")
print("Fim do programa!")