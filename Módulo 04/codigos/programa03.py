"""
programa para demonstrar escopo de variáveis no python
Author: Richard Brosler
Version: 2024-10-09
"""
from click import clear

def mostrar_mensagem():
    print("Vou mostrar uma mensagem...")
    mensagem = "abc" # Está só para a função
    print(mensagem)
    #mensagem += " - alterando o conteúdo!"
    print('-' * 30)
    print(mensagem)

clear()
mensagem = "Sei lá"
mostrar_mensagem()
print(mensagem)