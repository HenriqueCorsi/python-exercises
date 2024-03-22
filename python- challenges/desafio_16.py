'''
Crie um código que leia um númeoo de 0 a 9999 e mostre na tela cada um dos digitos separdos
'''
import os

os.system('cls')
num = int(input("Valor: "))

if num >= 1000 and num <= 9999:
    os.system('cls')
    num = str(num)
    print(f'Unidade: {num[3]}')
    print(f'Dezena: {num[2]}')
    print(f'Centena: {num[1]}')
    print(f'Milhar: {num[0]}')
elif num >= 100 and num <= 999:
    os.system('cls')
    num = str(num)
    print(f'Unidade: {num[2]}')
    print(f'Dezena: {num[1]}')
    print(f'Centena: {num[0]}')
elif num >= 10 and num <= 99:
    os.system('cls')
    num = str(num)
    print(f'Unidade: {num[1]}')
    print(f'Dezena: {num[0]}')
elif num < 10:
    os.system('cls')
    num = str(num)
    print(f'Centena: {num[0]}')
else:
    print("Valor Inválido!")
    
