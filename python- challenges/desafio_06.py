"""
Crie um código que leia a largura e altura de uma pare dem metros e calcule a área total. Após isso
calcule a quantidade de tinta necessaria para pinta-la. Cada litro de tinta pinta uma área de 2m².
"""
import os

def CalculaRendimento(a, l):
    areaTotal = a * l
    litrosNecessario = areaTotal / 2
    return f'\nA parede tem {round(areaTotal, 1)}m² e precisa-se de {round(litrosNecessario, 1)} litros de tinta para pinta-la!\n'

cont = True

while cont:
    try:
        altura = float(input("\nAltura: "))
        largura = float(input("Lagura: "))
    except Exception as e:
        os.system('cls')
        print("Valor Inválido. Pressione ENTER para tentar novamente")
        input()
        os.system('cls')
    else:
        os.system('cls')
        print(CalculaRendimento(altura, largura))
        cont = False



