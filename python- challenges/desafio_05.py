"""
Converta valores em Dollares para Real. Taxa de Cambio R$4.94
"""
import os

def converteDollar(x):
    x = x / 4.94
    return f'{round(x, 2)}'

cont = True

while cont:
    try:
        x = float(input("Digite o Valor: "))
    except Exception as e:
        os.system('cls')
        print('___________________________________')
        print("Valor Inválido! Presione o ENTER para tentar novamente.")
        input()
        os.system('cls')
    else:
        os.system('cls')
        print('___________________________________')
        print(f"Com R$ {x} você consegue comprar US$ {converteDollar(x)}")
        cont = False


