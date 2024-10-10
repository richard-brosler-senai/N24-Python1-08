"""
Programa conversor de temperaturas
Author: Richard Brosler
Version: 2024-10-03
"""
from click import clear
clear()
# Pedindo a temperatura
temp = float(input("Digite a temperatura: "))
# Montando o menu de opções
print("Menu de opções")
print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")
print("3 - Fahrenheit para Celsius")
print("4 - Fahrenheit para Kelvin")
print("5 - Kelvin para Celsius")
print("6 - Kelvin para Fahrenheit")
# Solicitando a opção
opc = int(input("Digite a opção: "))
# Calculando a temperatura
if opc == 1: # c => f
    tempd = temp * 9 / 5 + 32
elif opc == 2: # c => k
    tempd = temp + 273
elif opc == 3: # f => c
    tempd = (temp - 32)* 5 / 9
elif opc == 4: # f => k
    tempd = (temp - 32) * 5 / 9 + 273
elif opc == 5: # k => c
    tempd = temp - 273
elif opc == 6: # k => f
    tempd = (temp - 273) * 9 / 5 + 32
else:
    tempd = 0
# mostrando o resultado
print("Temperatura final =",tempd)