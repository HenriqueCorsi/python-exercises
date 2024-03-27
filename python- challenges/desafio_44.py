'''
Crie um um jogo onde a CPU irá pensar em um número de 1 a 10. E o usuário precisa advinhar qual número
é esse. O usuário precisa ter apenas 4 chances para acertar
'''
import random
import os
import time

def random_number():
    n_secret = random.randrange(1, 10)
    return n_secret

def user_input():
    cont = True
    while cont:
        try:
            number = int(input('\nQual você seu palpite para o número secreto?\n '))
        except Exception as e:
            os.system('cls')
            print('Valor Inválido! Pressione ENTER para tentar novamente.')
            input()
            os.system('cls')
        else:
            if number >= 0 and number <= 10:
                cont = False
                return number
            else:
                os.system('cls')
                print('Valor Inválido. Escolha um número entre 1 e 10.')
                input()
                os.system('cls')

cont = 4
cpu_secret = random_number()

while cont >= 1:
    os.system('cls')
    print(cpu_secret)
    print('=========================================')
    print('       BEM VINDO AO ADIVINHE O NÚMERO    ')
    print('=========================================')
    
    secret_number = user_input()

    if secret_number == cpu_secret: # Se usário acertar o número
        os.system('cls')
        print('Parabén!! Você ACERTOU.')
        print(f'O número secreto é {cpu_secret}') 
        cont = 0
    elif cpu_secret > secret_number: # Se usário der um palpite maior que o número secreto
            os.system('cls')
            cont -= 1
            if cont != 0:
                print(f'ERROOOUUU!! O número secreto é MAIOR que {secret_number}')
                print(f'Você tem apenas mais {cont} tentativas. Pressione ENTER para tentar novamente')
                input()
                os.system('cls')
            elif cont == 0:
                print('ERROOUU!! O número de TENTATIVAS acabou!!')
                print(f'O número secreto era {cpu_secret}')
    elif cpu_secret < secret_number: # Se usário der um palpite menor que o número secreto
            os.system('cls')
            cont -= 1
            if cont != 0:
                print(f'ERROOOUUU!! O número secreto é MENOR que {secret_number}')
                print(f'Você tem apenas mais {cont} tentativas. Pressione ENTER para tentar novamente')
                input()
                os.system('cls')
            elif cont == 0:
                print('ERROOUU!! O número de TENTATIVAS acabou!!')
                print(f'O número secreto era {cpu_secret}')
        



    
    



