'''
Desenvolva um código que solicite a distancia de uma viagem em km e calcule o preço da passagem 
cobrando 0.50 em até 200km e 0.45 para viagnes mais longas. 
'''
def calculaPreco(x):
    if x >= 200:
        precoPass = x * 0.45
        return f'Valor da passagem é de R${precoPass}'
    else:
        precoPass = x * 0.50
        return f'Valor da passagem é de R${precoPass}'   


distanciaKm = float(input('Distância: '))

print(calculaPreco(distanciaKm))
