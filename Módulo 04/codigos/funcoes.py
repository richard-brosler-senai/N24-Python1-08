"""
Funções para uso nos sistemas
Author: Richard Brosler
Version: 2024-10-09
"""
from click import clear # importando a função clear do modulo click
# Função para montagem de tela
def montar_tela(titulo = 'Menu Principal', colunas = 42):
    # Ajuste no título
    if len(titulo) % 2 == 1:
        titulo += ' ' # coloco 1 espaço no fim
    espacos = (colunas - 2 - len(titulo)) // 2 * ' '
    clear() # limpando a tela
    print('+' + '-' * (colunas-2) + '+')
    print('|' + espacos + titulo + espacos + '|')
    print('+' + '-' * (colunas-2) + '+')
# Função para calcular o fatorial de um número
# 5! => 5 x 4 x 3 x 2 x 1 => 120
def fatorial(num):
    resultado = 1.
    for i in range(num,1,-1):
        resultado *= i # resultado = resultado * i
    return resultado
# Função fatorial recursiva
def fatorial_rec(num):
    if num < 0: return None
    if num < 2: return 1
    return num * fatorial_rec(num-1)
# Função para retornar o mínimo e o máximo
def min_max(vlra, vlrb, vlrc):
    return min(vlra,vlrb,vlrc), max(vlra,vlrb,vlrc)
# Função para verificar se o número é primo
def is_primo(numero):
    for i in range(2,1+int(numero**0.5)):
        if numero % i == 0:
            return False
    return True
# Função para adicionar nomes a uma lista
def adicionar_nomes(lista):
    lista.append(input("Digite um nome: "))

# Função para remover nome de uma lista
def remover_nomes(lista):
    nom = input("Digite o nome a ser removido: ")
    for i in range(len(lista)-1,-1,-1):
        if lista[i] == nom:
            del lista[i]
            return
    print("Nome não encontrado na lista!")

# Só quando for executado o script funcoes será executado abaixo
if __name__ == '__main__':
    montar_tela()
    input("Digite algo para continuar ")