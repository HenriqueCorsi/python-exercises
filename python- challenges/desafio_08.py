"""
Crie um código que leia o salário do colaborador e mostre seu novo salário com um aumento de 15%
"""
import os

def reajusteSalario(x):
    x = (x * 0.15) + x
    return f'{round(x, 2)}'

cont = True


while cont:
    try:
        os.system('cls')
        salario = float(input("Salário: "))
    except Exception as e:
        os.system('cls')
        print("Valor Inválido! Pressione ENTER para tentar novamente.")
        input()
    else:
        os.system('cls')
        print(f"Seu salário de R${salario} com reajuste foi para R${reajusteSalario(salario)}")
        cont = False