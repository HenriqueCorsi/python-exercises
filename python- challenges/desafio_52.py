'''
Crie uma codigo que leia o nome e preço de varios produtos. Ao final mostre:
    -> Qualo total gasto
    -> Quantos produtos custam mais de 1000
    -> Qual o nome do produto mais barato
'''
import os

def menu():
    os.system('cls')
    print('=========================')
    print('        BEM-VINDO        ')
    print('=========================')

cont = True
price_list = []
price_1000 = []
product_name_cheap = []

while cont:
    menu()
    product_name = input('Produto: ')
    product_price = float(input('Valor: '))

    price_list.append(product_price)

    if product_price >= 1000:
        price_1000.append(product_name)
    
    product_price = str(product_price)

    if len(product_name_cheap) == 0:
        product_name_cheap.append(product_name)
    elif product_price < product_name_cheap[0]:
        product_name_cheap.append(product_name)

    os.system('cls')
    continue_ = input('Quer Continuar? [S/N]').lower()
    
    if continue_ == 's':
        os.system('cls')
    elif continue_ == 'n':
        total_price = sum(price_list)
        product_1000 = len(price_1000)
        product_cheap = product_name_cheap[0]

        os.system('cls')

        print(f'Preço total dos seus produtos é R${total_price}')
        print('==================================================')
        print(f'Você tem {product_1000} que custam acima de R$1000')
        print('==================================================')
        print(f'O produto mais barato que você adicionou é {product_cheap}')
        print('==================================================')
        cont = False
