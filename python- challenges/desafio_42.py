'''
Crie um codigo que leia o peso de cinco pessoas. No final mostre qual o maior e o meno peso
'''
import os

lista_peso = []
cont = 1

while cont <= 5:
    os.system('cls')
    peso_input = float(input(f'Peso da Pessoa0{cont}: '))
    lista_peso.append(peso_input)
    cont += 1

os.system('cls')
print(f'O MAIOR peso registrado foi {max(lista_peso)}KG')
print(f'O MENOR peso registrado foi {min(lista_peso)}KG')

