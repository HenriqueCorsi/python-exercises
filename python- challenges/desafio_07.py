""""
Faça um código que leia o peso de um produto e mostre seu novo preço com 5% de desconto.
"""
import os

def addDescont(x):
    x = x - (x * 0.05)
    return  f'{round(x, 2)}'

cont = True

while cont:
    try:
        os.system('cls')
        price = float(input("Digite o valor: "))
    except Exception as e:
        os.system('cls')
        print("Valor Inválido! Tente nonvamente pressionando o ENTER")
        input()
        os.system('cls')
    else:
        os.system('cls')
        print(f'Preço de R${round(price, 2)} foi aplicado um cupom de desconto. Preço atualizado é de R${addDescont(price)}')
        cont = False