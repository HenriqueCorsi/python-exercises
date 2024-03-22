'''
Escreva um código que pergunte o valor do funcionario:
    Para salarios acima de 1250 calcule um aumento de 10%
    Para salarios inferiores ou iguais 1250 calcule um aumento de 15% 
'''
import os

def calculaAumentoSalarial(salario):
    if salario > 1250:
        reajusteSalarial = salario + (salario * 0.10)
        return f'O seu sálario de R${salario} foi reajustado para R${reajusteSalarial}'
    else:
        reajusteSalarial = salario + (salario * 0.15)
        return f'O seu sálario de R${salario} foi reajustado para R${reajusteSalarial}'


cont = True
while cont:
    try:
        os.system('cls')
        salarioUser = float(input('Sálario: '))
    except Exception as e:
        os.system('cls')
        print('Valor Inválido! Pressione ENTER para tentar novamente')
        input()
        os.system('cls')
    else:
        os.system('cls')
        print(calculaAumentoSalarial(salarioUser))
        cont = False


