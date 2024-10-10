"""
Programa para solicitar nomes de pessoas
Author: Richard Brosler
Version: 2024-10-09
"""
from funcoes import montar_tela, adicionar_nomes, remover_nomes
lista_nomes = []
def montar_menu():
    montar_tela("Menu Principal")
    print("1 - Adicionar Nomes")
    print("2 - Remover Nomes")
    print("3 - Listar Nomes")
    print("4 - Fim")
    print("Digite sua opção: ")

while True:
    montar_menu()
    opc = int(input())
    if opc == 4: break
    elif opc == 1: adicionar_nomes(lista_nomes)
    elif opc == 2: remover_nomes(lista_nomes)
    elif opc == 3:
        for it in lista_nomes:
            print(it)
    input("Tecle algo para continuar... ")