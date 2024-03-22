"""
Escreva um código que converta uma temperaruta digita em °C para °F
"""

import os

def converteTemp(c):
    c = c * 1.8 + 32
    return f'{round(c, 1)}'

cont = True

while cont:
    try:
        os.system('cls')
        temp = float(input("Temperatura: "))
    except Exception as e:
        os.system('cls')
        print("Valor Inválido! Pressione ENTER para tentar novamente.")
        input()
        os.system('cls')
    else:
        os.system('cls')
        print(f'A temperatura {temp}°C convertida em Fahrenheit fica {converteTemp(temp)}°F')
        cont = False