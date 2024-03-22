'''
Desenvolva um codigo que calcule o valor a ser pago por um prodruto:
    -> C/Débito 10% de desconto
    -> C/Crédito:
        1x desconto de 5%
        2x sem desconto
        3x juros de 20%
    -> Pix ou Dinheito 15% de desconto
'''
import os

def menuSelect():
    os.system('cls')
    print('--- FORMA DE PAGAMENTO ---')
    list_menu = ['[1] Débito', '[2] Crédito', '[3] Pix/Dinheiro']
    for x in list_menu:
        print(x)

def menuParcelamento():
    os.system('cls')
    list_menu = ['-> 1x', '-> 2x', '-> 3x']
    for x in list_menu:
        print(x)

menuSelect()

select_user = int(input(''))

if select_user ==  1: # Cartão de Débito
    valor_compra = float(input('Valor da Compra: '))
    valor_compra = valor_compra - (valor_compra * 0.10)
    print(f'Valor Final da Compra é {valor_compra}')
elif select_user == 2: # Cartão de Crédito

    menuParcelamento()
    valor_parcelamento = int(input('Valor Parcelamento: '))

    if valor_parcelamento == 1: # Parcelamento em 1x
         os.system('cls')
         valor_compra = float(input('Valor da Compra: '))
         os.system('cls')
         valor_compra = valor_compra - (valor_compra * 0.05)
         print(f'Valor Final da Compra é {valor_compra}')
    elif valor_parcelamento == 2: # Parcelamento em 2x
        os.system('cls')
        valor_compra = float(input('Valor da Compra: '))
        os.system('cls')
        print(f'Valor Final da Compra é {valor_compra}')
    elif valor_parcelamento == 3: # Parcelamento em 3x
        os.system('cls')
        valor_compra = float(input('Valor da Compra: '))
        valor_compra = valor_compra + (valor_compra * 0.20)
        os.system('cls')
        print(f'Valor Final da Compra é {valor_compra}')
        
elif select_user == 3: # Pix ou Dinheiro
    valor_compra = float(input('Valor da Compra: '))
    valor_compra = valor_compra - (valor_compra * 0.15)
    print(f'Valor Final da Compra é {valor_compra}')


