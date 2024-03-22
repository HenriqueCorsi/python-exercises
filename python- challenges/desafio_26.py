'''
Escreva um código que leia 3 números e mostre qual deles é o maior e quel é o menor
'''
import os

def verifcaMaiorValor(num01,num02,num03):
    if num01 >= num02 and num01 >= num03:
        return f'O maior valor é {num01}'
    elif num02 >= num01 and num02 >= num03:
        return f'O maior valor é {num02}'
    elif num03 >= num01 and num03 >= num02:
        return f'O maior valor é {num03}'

def verificaMenorValor(num01,num02,num03):
    if num01 <= num02 and num01 <= num03:
        return f'O maior valor é {num01}'
    elif num02 <= num01 and num02 <= num03:
        return f'O maior valor é {num02}'
    elif num03 <= num01 and num03 <= num02:
        return f'O maior valor é {num03}'


cont = True
while cont:
    try:
        os.system('cls')
        n1 = float(input('Primeiro Valor: '))
        n2 = float(input('Segundo Valor Valor: '))
        n3 = float(input('Terceiro Valor Valor: '))
    except Exception as e:
        os.system('cls')
        print('Valor Inválido! Pressione ENTER para tentar novamente')
        input()
        os.system('cls')
    else:
        os.system('cls')
        print(verifcaMaiorValor(n1,n2,n3))
        print(verificaMenorValor(n1,n2,n3))
        cont = False


