'''
Crie um JOKEMPÔ!!

'''

import random
import os
import time

def menu():
    os.system('cls')
    print('=======================')
    print(' WELCOME TO JOKENPÔÔÔ ')
    print('=======================')
    list_menu = ['[1] Pedra', '[2] Papel', '[3] Tesoura', '[4] SAIR\n']
    for x in list_menu:
        print(x)

cont = True
placar_user = 0
placar_cpu = 0

while cont:
    menu()

    print(f'Placar YOU {placar_user} X {placar_cpu} CPU ')

    option_jokenpo = ['Pedra', 'Papel', 'Tesoura'] 
    cpu_select = random.choice(option_jokenpo) # CPU escolhe 

    user_select = int(input(''))

    if user_select == 1:
        
        user_select = 'Pedra'
        
        if user_select == cpu_select: # Pedra == Pedra
            os.system('cls')
            print('CARREGANDO...')
            time.sleep(1)
            os.system('cls')
            print('EMPATE!!')
            print('=======================')
            print(f'YOU: {user_select.upper()}')
            print(f'CPU: {cpu_select.upper()}')
            time.sleep(3)
        
        elif cpu_select == 'Papel': # Pedra == Papel
            os.system('cls')
            print('CARREGANDO...')
            time.sleep(1)
            os.system('cls')
            print('VOCÊ PERDEU!!')
            print('=======================')
            print(f'YOU: {user_select.upper()}')
            print(f'CPU: {cpu_select.upper()}')
            time.sleep(3)
            placar_cpu += 1
        
        elif cpu_select == 'Tesoura': # Pedra == Tesoura
            os.system('cls')
            print('CARREGANDO...')
            time.sleep(3)
            os.system('cls')
            print('VOCÊ GANHOU!!')
            print('=======================')
            print(f'YOU: {user_select.upper()}')
            print(f'CPU: {cpu_select.upper()}')
            time.sleep(3)
            placar_user += 1

    elif user_select == 2:

        user_select = 'Papel'

        if user_select == cpu_select: # Papel == Papel
            os.system('cls')
            print('CARREGANDO...')
            time.sleep(1)
            os.system('cls')
            print('EMPATE!!')
            print('=======================')
            print(f'YOU: {user_select.upper()}')
            print(f'CPU: {cpu_select.upper()}')
            time.sleep(3)
        
        elif cpu_select == 'Pedra': # Papel == Pedra
            os.system('cls')
            print('CARREGANDO...')
            time.sleep(1)
            os.system('cls')
            print('VOCÊ GANHOU!!')
            print('=======================')
            print(f'YOU: {user_select.upper()}')
            print(f'CPU: {cpu_select.upper()}')
            time.sleep(3)
            placar_user += 1
        
        elif cpu_select == 'Tesoura': # Papel == Tesoura
            os.system('cls')
            print('CARREGANDO...')
            time.sleep(1)
            os.system('cls')
            print('VOCÊ PERDEU!!')
            print('=======================')
            print(f'YOU: {user_select.upper()}')
            print(f'CPU: {cpu_select.upper()}')
            time.sleep(3)
            placar_cpu += 1

    elif user_select == 3:
        
        user_select = 'Tesoura'

        if user_select == cpu_select: # Tesoura == Tesoura
            os.system('cls')
            print('CARREGANDO...')
            time.sleep(1)
            os.system('cls')
            print('EMPATE!!')
            print('=======================')
            print(f'YOU: {user_select.upper()}')
            print(f'CPU: {cpu_select.upper()}')
            time.sleep(3)
        
        elif cpu_select == 'Pedra': # Tesoura == Pedra
            os.system('cls')
            print('CARREGANDO...')
            time.sleep(1)
            os.system('cls')
            print('VOCÊ PERDEU!!')
            print('=======================')
            print(f'YOU: {user_select.upper()}')
            print(f'CPU: {cpu_select.upper()}')
            time.sleep(3)
            placar_cpu += 1
        
        elif cpu_select == 'Papel': # Tesoura == Papel
            os.system('cls')
            print('CARREGANDO...')
            time.sleep(1)
            os.system('cls')
            print('VOCÊ GANHOU!!')
            print('=======================')
            print(f'YOU: {user_select.upper()}')
            print(f'CPU: {cpu_select.upper()}')
            time.sleep(3)
            placar_user += 1
        
    elif user_select == 4:
        cont = False
        os.system('cls')
        print('CARREGANDO...')
        time.sleep(1)
        print('\nAté Mais!!')