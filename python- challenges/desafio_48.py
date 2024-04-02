'''
Crie um codigo que leia varios numeros inteiros. No final da execução mostre:
    -> A média entre todos os números
    -> O maior Valor
    -> O menor Valor
    -> E ao final o programa deve perguntar se o usario quer continuar ou não
'''
import os
import time

def average_cal(list):
    average = (sum(list)) / len(list)
    return average

def loading():
    print('Carregando...')
    time.sleep(1)

cont = True
num_list = []

while cont:
    os.system('cls')
    num = int(input('Insira o Valor: '))
    num_list.append(num)
    
    os.system('cls')
    loading()
    os.system('cls')

    select_continue = input('Quer CONTINUAR? ').lower()

    if select_continue == 's':
        os.system('cls')
        loading()
    elif select_continue == 'n':
        average = average_cal(num_list)
        max_value = max(num_list)
        min_value = min(num_list)

        os.system('cls')
        loading()
        os.system('cls')
    
        print(f'A média dos números é {average}')
        print(f'O maior valor encontrado é o {max_value}')
        print(f'O menor valor encontrado é o {min_value}')
        cont = False

        


