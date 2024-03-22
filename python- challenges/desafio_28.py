'''
Escreve um código que aprova o emprestimo bancario para compra de um imovel.
    Pergunte o valor do imovel.
    Salario do comprador 
    Em qunatos anos ele vai pagar
A prestação mensal, não pode exceder 30% do salario ou então o emprestimo sera negado
'''

import os

def calculaSalario(salario):
    salarioTotal = salario
    salarioParcial = salarioTotal - (salarioTotal * 0.30)
    salario30 = salarioTotal - salarioParcial
    return salario30

def calculaPrestacao(valorImovel, valorFinanciamento):
    valorFinanciamento = valorImovel / valorFinanciamento
    return valorFinanciamento


cont = True
while cont:
    try:
        os.system('cls')
        salario = float(input('Salário: '))
        os.system('cls')
        valorImovel = float(input('Valor do Imovel: '))
        os.system('cls')
        numeroParcelas = float(input('Número de Parcelas: '))
        qtdAnos = int(numeroParcelas / 12)
    except Exception as e:
        os.system('cls')
        print('Valor Inválido! Pressione ENTER para tentar novamene')
        input()
        os.system('cls')
    else:

        valorParcela = calculaPrestacao(valorImovel, numeroParcelas)

        if calculaSalario(salario) < calculaPrestacao(valorImovel, numeroParcelas):
            os.system('cls')
            print(f'Valor do Imovel: R${valorImovel}')
            print(f'Financiameto em: {qtdAnos} anos') 
            print(f'Valor da Parcela: R${round(valorParcela, 2)}\n')
            print('EMPRESTIMO NEGADO!!')
            cont = False
        else:
            os.system('cls')
            print(f'Valor do Imovel: R${valorImovel}')
            print(f'Financiameto em: {qtdAnos} anos')
            print(f'Valor da Parcela: R${round(valorParcela, 2)}\n')
            print('EMPRESTIMO APROVADO!!')
            cont = False