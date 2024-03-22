'''
Faça um código que leia o ano de nascimento de um atleta e calcule sua categoria:
    até 9 anos -> mirim 
    até 14 anos -> infantil
    até 19 anos -> juniot
    acima de 20 -> master
'''
from datetime import date
import os

cont = True
anoAtual = date.today().year

while cont:
    try:
        os.system('cls')
        anoNascimento = int(input('Ano Nascimento: '))
    except Exception as e:
        os.system('cls')
        print('Valor Inválido! Pressione ENTER para tentar novamente')
        input()
        os.system('cls')
    else:
        idadeUsuario = anoAtual - anoNascimento

        if idadeUsuario <= 9:
            os.system('cls')
            print(f'Atleta tem {idadeUsuario} anos')
            print(f'Categoria Mirim')
            cont = False
        elif idadeUsuario >= 10 and idadeUsuario <= 14:
            os.system('cls')
            print(f'Atleta tem {idadeUsuario} anos')
            print(f'Categoria Infantil')
            cont = False
        elif idadeUsuario >= 15 and idadeUsuario <= 19:
            os.system('cls')
            print(f'Atleta tem {idadeUsuario} anos')
            print(f'Categoria Junior')
            cont = False
        elif idadeUsuario >= 20:
            os.system('cls')
            print(f'Atleta tem {idadeUsuario} anos')
            print(f'Categoria Master')
            cont = False