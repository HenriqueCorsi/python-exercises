'''
Crie um código que leia o comprimento do coteto oposto e do cateto adjacente de um
triângulo retângulo, calcule e mostre o comprimento da hipotenusa 
'''
import math
import os

def CalculaHipotenusa(x, y):
    hiportenusa = (x ** 2) + (y **2)
    return f'{round(math.sqrt(hiportenusa), 2)}'

cont = True

while cont:
    try:
        os.system('cls')
        catetoOposto = float(input("Digito Valor: "))
        catetoAdjacente = float(input("Digito Valor: "))
    except Exception as e:
        os.system('cls')
        print("Valor Inválido! Pressione ENTER para tentar novamnete.")
        input()
        os.system('cls')
    else:
        os.system('cls')
        print(f"O valor da hipotenusa é {CalculaHipotenusa(catetoOposto, catetoAdjacente)}")
        cont = False


