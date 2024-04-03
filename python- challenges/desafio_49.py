'''
Construa um codigo que mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuario.
Caso um numero negativo seja inserido, o codigo encerra sua execução
'''
import os
import time

def gera_tabuada(x):
    cont = 1
    while cont <= 10:
        resultado = x * cont
        print(f'{x} X {cont} = {resultado}')
        cont += 1

def loading():
    os.system('cls')
    print('Carregando...')
    time.sleep(1)
    os.system('cls')

cont = True

while cont:
    num = int(input('\nInsira um valor: '))
    if num > 0:
        loading()
        gera_tabuada(num)
    else: 
        loading()
        print('Até Breve!!')
        cont = False





        