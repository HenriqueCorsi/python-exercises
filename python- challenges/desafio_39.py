'''
Escreva um código que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
'''
import os
import time

armazena_valores = []

for x in range(1, 7):
    os.system('cls')
    time.sleep(0.5)
    num = int(input(f'Valor 0{x}: '))
    if num % 2 == 0:
        armazena_valores.append(num)
    else:
        pass

os.system('cls')
print('SOMANDO....')
time.sleep(1)
os.system('cls')
soma_valores = sum(armazena_valores)

print(soma_valores)



