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

os.system('cls')
select_user = input('Ímpar ou Par ? [I/P]').lower()
loading()
cpu_num = random.randint(0, 50)
user_num = 20
result = cpu_num + user_num

if select_user == 'i' and result % 2 != 0:#Usuario Ganha
    loading()
    print(f'Você: {user_num}')
    print(f'CPU: {cpu_num}')
    print(f'Soma: {result}')

    print(f'{result} é ÍMPAR vc GANHOU!!')
elif select_user == 'i' and result % 2 == 0:#Usuario Perde
    loading()
    print(f'Você: {user_num}')
    print(f'CPU: {cpu_num}')
    print(f'Soma: {result}')

    print(f'{result} não é ÍMPAR vc PERDEU!!')
elif select_user == 'p' and result % 2 == 0:#Usuario Ganha
    loading()
    print(f'Você: {user_num}')
    print(f'CPU: {cpu_num}')
    print(f'Soma: {result}')

    print(f'{result} é PAR vc GANHOU!!')#Usuario Perde
elif select_user == 'p' and result % 2 != 0:
    loading()
    print(f'Você: {user_num}')
    print(f'CPU: {cpu_num}')
    print(f'Soma: {result}')

    print(f'{result} não é PAR vc PERDEU!!')