"""
Escreva um código que  pergunte a qtd de KM percorrido por um carro alugado e a qtd de dias pelos quais ele foi alugado.
Calcule que o preço a pagar, sabendo que o carro custa 60 por dia e 0.15 por km rodado. Caso o valor final ultrapasse 350 o clinte ganha
um desoconto de 15%
"""
import os

def calculaKM(km):
    km = km * 0.15
    return km

def calculaDia(qtd_dias):
    qtd_dias = qtd_dias * 60
    return qtd_dias

def calculaDesconto(desconto):
    desconto = desconto - (desconto * 0.15) 
    return desconto

cont = True

while cont:
    try:
        os.system('cls')
        km_rodado = float(input("Quantidade de KM Rodado: "))
        os.system('cls')
        dias_alugados = float(input("Quantidade de DIAS alugado: "))
    except Exception as e:
        os.system('cls')
        print("Valor Inválido. Pressione ENTER para tentar novamente!")
        os.system('cls')
    else:
        os.system('cls')
        valor_final = calculaKM(km_rodado) + calculaDia(dias_alugados)

        if valor_final >= 530:
            print(f"Você ganhou um cupom de desconto! Valor final a pagar é de R${calculaDesconto(round(valor_final, 2))}")
            cont = False
        else:   
            print(f'valor final {round(valor_final, 2)}')
            cont = False


