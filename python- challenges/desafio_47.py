'''
Crie um codigo que leia vários numero inteiros. O codigo só vai parar de ser executado se o usuário digitar 999. No final mostre quantos 
numero foram digitados e a soma entre eles
'''
import os
import time

def loading():
    os.system('cls')
    print('Carregando...')
    time.sleep(1.5)
    os.system('cls')



cont = True
num_list = []

while cont:
    os.system('cls')
    print('CASO QUEIRA FINALIZAR PRESSIONE 999\n')
    try:
        num = int(input('Insira o valor: '))
    except Exception as e:
        os.system('cls')
        print('Valor Inválido!!')
        time.sleep(0.5)
        os.system('cls')
    else:
        loading()
        if num != 999:
            num_list.append(num)
        else:
            num_size = len(num_list)
            num_sum = sum(num_list)
            os.system('cls')
            print('=====================================================')
            print(f'A quantidade de números digitados foi {num_size}')
            print(f'E a soma entre eles é {num_sum}')
            print('=====================================================\n\n')
            cont = False


