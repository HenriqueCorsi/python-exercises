"""
Escreva um código que leia um valor em metros e o exiba convertido em CM e em MM
"""

def converteCM(x):
    x = x * 100
    return x

def converteMM(x):
    x = x * 1000
    return x

cont = True

while cont:
    try:
        valorMetro = float(input("Valor: "))
    except Exception as e:
        print("Valor inválido! Pressione ENTER para tentar novamente.")
        input()
    else: 
        print(f'{valorMetro} MT é equivalente a {converteCM(round(valorMetro))} CM e {converteMM(valorMetro)} MM')
        cont = False



