'''
Escreva um código que leia a velocidade de um carro. Se ela ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado e o valor da multa.
A multa irá custar R$7,00 por cada km acima do limite
'''

velocidadePermitida = 80
velocidade = float(input('Digite a velocidade: '))

if velocidade > velocidadePermitida:
    valorMulta = (velocidade - velocidadePermitida) * 7
    print(f'Multado!! Valor da multa é de R${valorMulta}')
else:
    print('Velocidade Permitida!!')