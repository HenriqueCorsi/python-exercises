""""
Construa um código que realiza as 4 operações básicas entre 2 números. 
"""

import os

def soma(n1, n2):
    return f'{round(n1 + n2, 2)}'

def sub(n1, n2):
    return f'{round(n1 - n2, 2)}'

def multi(n1, n2):
    return f'{round(n1 * n2, 2)}'

def div(n1, n2):
    return f'{round(n1 / n2, 2)}'

def menu():
    print("\n**** ESCOLHA A OPERAÇÃO DESEJADA **** ")
    menu = ["1 -> Adição", "2 -> Subtração", "3 -> Multiplicação", "4 - Divisão"]
    for x in menu:
        print(x)

teste_menu = True

while teste_menu: # Looop 01 inicia aqui!
    try:
        os.system('cls')
        menu()
        menu_input = int(input("\n"))
    except Exception as e:
        os.system('cls')
        print("Valor Invalido, pressione  o ENTER para tentar novamente.")
        input()
    else:
        teste_menu = False # Looop 01 encerra aqui!
        if menu_input == 1:
            teste_menu = True
            while teste_menu: # Loop 02 inicia aqui!
                try:
                    os.system('cls')
                    n1 = float(input("Primeiro Valor: "))
                    n2 = float(input("Segundo Valor: "))
                except Exception as e:
                    os.system('cls')
                    print("Valor Invalido, pressione  o ENTER para tentar novamente.")
                    input()
                else:
                    print(soma(n1, n2))
                    teste_menu = False # Loop 02 inicia aqui!
        elif menu_input == 2:
            teste_menu = True # Looop 01 encerra aqui!
            while teste_menu: # Loop 02 inicia aqui!
                try:
                    os.system('cls')
                    n1 = float(input("Primeiro Valor: "))
                    n2 = float(input("Segundo Valor: "))
                except Exception as e:
                    os.system('cls')
                    print("Valor Invalido, pressione  o ENTER para tentar novamente.")
                    input()
                else:
                    print(sub(n1, n2))
                    teste_menu = False # Loop 02 enceraa aqui!
        elif menu_input == 3:
            teste_menu = True # Looop 01 encerra aqui!
            while teste_menu: # Loop 02 inicia aqui!
                try:
                    os.system('cls')
                    n1 = float(input("Primeiro Valor: "))
                    n2 = float(input("Segundo Valor: "))
                except Exception as e:
                    os.system('cls')
                    print("Valor Invalido, pressione  o ENTER para tentar novamente.")
                    input()
                else:
                    print(multi(n1, n2))
                    teste_menu = False # Loop 02 enceraa aqui!
        elif menu_input == 4:
            teste_menu = True # Looop 01 encerra aqui!
            while teste_menu: # Loop 02 inicia aqui!
                try:
                    os.system('cls')
                    n1 = float(input("Primeiro Valor: "))
                    n2 = float(input("Segundo Valor: "))
                except Exception as e:
                    os.system('cls')
                    print("Valor Invalido, pressione  o ENTER para tentar novamente.")
                    input()
                else:
                    print(div(n1, n2))
                    teste_menu = False # Loop 02 enceraa aqui!
        else:
            os.system('cls')
            print("Valor Invalido, pressione  o ENTER para tentar novamente.")
            input()
            teste_menu = True

