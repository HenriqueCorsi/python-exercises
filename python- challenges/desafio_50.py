'''
Crie um codigo que jogue impar ou par com o usuario.
'''
import os
import time
import random

def loading():
    os.system('cls')
    print('Carregando...')
    time.sleep(1)
    os.system('cls')

def menu():
    os.system('cls')
    print('============================================')
    print('          BEM VINDO AO ÍMPAR OU PAR          ')
    print('============================================')

menu()
select_user = input('\nVocê escolhe ÍMPAR ou PAR ? [I/P]').lower()
loading()
cpu_num = random.randint(0, 50)
user_num = int(input('Insira um Valor: '))
result = cpu_num + user_num

if select_user == 'i' and result % 2 != 0:#Usuario Ganha
    loading()
    print(f'Você: {user_num}')
    print('============================================')
    print(f'CPU: {cpu_num}')
    print('============================================')
    print(f'Soma: {result}')
    print('============================================')
    print(f'{result} é ÍMPAR vc GANHOU!!')
    print('============================================')
elif select_user == 'i' and result % 2 == 0:#Usuario Perde
    loading()
    print(f'Você: {user_num}')
    print('============================================')
    print(f'CPU: {cpu_num}')
    print('============================================')
    print(f'Soma: {result}')
    print('============================================')
    print(f'{result} não é ÍMPAR vc PERDEU!!')
    print('============================================')
elif select_user == 'p' and result % 2 == 0:#Usuario Ganha
    loading()
    print(f'Você: {user_num}')
    print('============================================')
    print(f'CPU: {cpu_num}')
    print('============================================')
    print(f'Soma: {result}')
    print('============================================')
    print(f'{result} é PAR vc GANHOU!!')
    print('============================================')
elif select_user == 'p' and result % 2 != 0:#Usuario Perde
    loading()
    print(f'Você: {user_num}')
    print('============================================')
    print(f'CPU: {cpu_num}')
    print('============================================')
    print(f'Soma: {result}')
    print('============================================')
    print(f'{result} não é PAR vc PERDEU!!')
    print('============================================')