'''
Escreva um código que leia um número inteiro qualquer e peça para ele escolher a base de conversã:
    1 - binario
    2 - octal
    3 - hexadecimal
'''
import os

def menu():
    os.system('cls')
    print('-- CONVERSOR DE BASES NÚMERICAS --')
    listMenu = ['1 -> Binário', '2 -> Octal', '3 -> Hexadecimal']
    for x in listMenu:
        print(x)

def binario(num):
    numBinario  =bin(num)
    return f'O valor {num} em BINÁRIO é {numBinario}'

def octal(num):
    numOctal = oct(num)
    return f'O valor {num} em OCTAL é {numOctal}'

def hexadecimal(num):
    numHexadecimal = hex(num)
    return f'O valor {num} em HEXADICAMAL é {numHexadecimal}'

cont = True

while cont:
    try:
        menu()
        inputMenu = int(input(''))
    except Exception as e:
        print('Valor Inválido!! Pressione ENTER para tentaer novamente.')
        input()
        os.system('cls')
    else:
        cont2 = True
        while cont2:
            os.system('cls')
            if inputMenu == 1: #Opção Binario
                cont = False
                try:
                    valorUser = int(input('Valor: '))
                    os.system('cls')
                except Exception as e:
                    print('Valor Inválido!! Pressione ENTER para tentaer novamente.')
                    input()
                    os.system('cls')
                else:
                    print(binario(valorUser)) 
                    cont2 = False
            elif inputMenu == 2: #Opção Octal
                cont = False
                try:
                    valorUser = int(input('Valor: '))
                    os.system('cls')
                except Exception as e:
                    print('Valor Inválido!! Pressione ENTER para tentaer novamente.')
                    input()
                    os.system('cls')
                else:
                    print(octal(valorUser))
                    cont2 = False
            elif inputMenu == 3: #Opção Hexadecimal
                cont = False
                try:
                    valorUser = int(input('Valor: '))
                    os.system('cls')
                except Exception as e:
                    print('Valor Inválido!! Pressione ENTER para tentaer novamente.')
                    input()
                    os.system('cls')
                else:
                    print(hexadecimal(valorUser))
                    cont2 = False
            else:
                print('Valor Inválido!! Pressione ENTER para tentaer novamente.')
                input()
                os.system('cls')
                break

