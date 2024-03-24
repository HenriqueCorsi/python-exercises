'''
Crie um codigo que leia o ano de nascimento de 7 pessoas e mostre quantas delas atingiram e não atingiram a maioridade 
'''
import os
from datetime import date

cont = 1
lista_ano = []
ano_atual = date.today().year
maior_de_idadde = []
menor_de_idadde = []


while cont <= 7:
    os.system('cls')
    ano_nascimento = int(input(f'Ano Nascimento da Pessoa 0{cont}: '))
    lista_ano.append(ano_nascimento)
    cont += 1

for x in lista_ano:
    if ano_atual - x < 18:
        maior_de_idadde.append(x)
    else:
        menor_de_idadde.append(x)

print(f'Temos {len(maior_de_idadde)} pessoas MAIORES  de idade')
print(f'Temos {len(menor_de_idadde)} pessoas MENORES de idade')