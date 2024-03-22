'''
Faça um código que leia um ano qualquer e mostre se ele é bissexto
'''
import os

def analisaAno(x):
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        os.system('cls')
        return f'O ano de {x} é Bissexto'
    else:
        os.system('cls')
        return f'O ano de {x} não é Bissexto'


cont = True

while cont:
    os.system('cls')
    try:
        ano = int(input("Ano: "))
    except Exception as e:
        os.system('cls')
        print('Valor Inválido! Pressione ENTER para tentar novamente')
        input()
        os.system('cls')
    else:
        os.system('cls')
        print(analisaAno(ano))
        cont = False






