'''
Escreva um código que faça o programa armazenar um número entre 0 e 5 e peça para o usuario advinhar!
'''
import random
import os
import emoji
import time

def msg(): #Função Mensagemd e Boas Vindas
    os.system('cls')
    print('---- ADVINHA O NÚMERO ----\n')

def verifcaNum(x): # Função que gera o número secreto e faz a verificação
    numSecreto = random.randint(1, 5)
    os.system('cls')
    print('CARREGANDO....')
    time.sleep(1)
    if x == numSecreto:
        os.system('cls')
        print(emoji.emojize(":grinning_face_with_smiling_eyes:"))
        print('Parabéns você acertou o número secreto!')
    else:
        os.system('cls')
        print(emoji.emojize(":grimacing_face:"))
        print('Errouuuuu...')
        print(f'O Número era: {numSecreto}')

cont = True
while cont:
    try:
        msg()
        numUser = int(input('Digite um número entre 1 a 5: '))
    except Exception as e:
        os.system('cls')
        print('Valor Inválido! Pressione ENTER para tentar novamente.')
        input()
        os.system('cls')
    else:
        if numUser >= 1 and numUser <= 5:
            os.system('cls')
            verifcaNum(numUser)
            cont = False
        else:
            os.system('cls')
            print('Valor Inválido! Lembre-se, os números precisam ser entre 1 a 5. Pressio ENTER para tentar novamente')
            input()
            os.system('cls')

