"""
Programa para demonstrar escopo global de variáveis
Author: Richard Brosler
Version: 2024-10-09
"""
from click import clear

def mostrar_mensagem():
    global mensagem, mensagem2
    mensagem = "Alterei a mensagem"
    print("Mostrando a mensagem....")
    print(mensagem)
    print('-' * 30)
    mensagem2 = "Sou criada agora"

clear()
mensagem = "Mensagem original"
mostrar_mensagem()
print(mensagem)
print(mensagem2)