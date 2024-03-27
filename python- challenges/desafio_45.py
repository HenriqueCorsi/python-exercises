'''
Crie um programa que leia dois números e mostre um menu na tela. O menu devara ter as opções de:
    -> SOMAR
    -> MULTIPLICAR
    -> EXIBIR O MAIOR
    -> ADD NOVOS NÚMEROS
    -> SAIR DO PROGRAMA
'''
import os
import time

def menu():
    os.system('cls')
    print('=================================')
    print('           SEJA-BEM VINDO         ')
    print('=================================')
    menu_list = ['[1] SOMAR', '[2] MULTIPLICAR', '[3] EXIBIR O MAIOR', '[4] ADICIONAR NOVOS NÚMEROS', '[5] SAIR']
    for x in menu_list:
        print(x)
    print('=================================\n\n')

def sum(n,y):
    sum_result = n + y
    return sum_result

def multi(n,y):
    multi_result = n * y
    return multi_result

def check_bigger(n,y):
    if n > y:
        return f'O maior número é {n}'
    elif n < y:
        return f'O maior número é {y}'
    elif n == y:
        return f'{n} e {y} são Iguais!!'

def get_firstNumber():
    cont = True
    while cont:
        try:
            print('=================================')
            n1 = float(input('Primeiro Valor: '))
        except Exception as e:
            os.system('cls')
            print('Valor Inválido. Pressione ENTER para tentar novamente!')
            input()
            print('=================================')
            os.system('cls')
        else:
            cont = False
            return n1

def get_seconftNumber():
    cont = True
    while cont:
        try:
            print('=================================')
            n2 = float(input('Segundo Valor: '))
            print('=================================')
        except Exception as e:
            os.system('cls')
            print('=================================')
            print('Valor Inválido. Pressione ENTER para tentar novamente!')
            input()
            print('=================================')
            os.system('cls')
        else:
            cont = False
            return n2

os.system('cls')
n1 = get_firstNumber()
n2 = get_seconftNumber()
cont = True

while cont:
    menu()
    try:
        user_input = int(input(''))
    except Exception as e:
        os.system('cls')
        print('=================================')
        print('Valor Inválido!!')
        print('=================================')
        time.sleep(1)
    else:
        if user_input == 1: # SOMAR 
            os.system('cls')
            result = sum(n1, n2)
            os.system('cls')
            print('=================================')
            print(f'A soma entre {n1} + {n2} é {result}')
            print('=================================')
            cont = False
        elif user_input == 2: # MULTIPLCIAR
            os.system('cls')
            result = multi(n1, n2)
            os.system('cls')
            print('=================================')
            print(f'A multiplicação entre {n1} x {n2} é {result}')
            print('=================================')
            cont = False
        elif user_input == 3: # VERIFICA O MAIOR NÚMERO
            os.system('cls')
            result = check_bigger(n1, n2)
            os.system('cls')
            print('=================================')
            print(result)
            print('=================================')
            cont = False
        elif user_input == 4: # ALTERA OS VALORES
            os.system('cls')
            n1 = get_firstNumber()
            n2 = get_seconftNumber()
            time.sleep(0.5)
            os.system('cls')
        elif user_input == 5: # SAIR
            os.system('cls')
            print('=================================')
            print('Até Breve!! ')
            print('=================================')
            cont = False
        else: # VALOR INVÁLIDO
            os.system('cls')
            print('=================================')
            print('Valor Inválido!!')
            print('=================================')
            time.sleep(1)    