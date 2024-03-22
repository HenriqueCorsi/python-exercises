'''
Desenvolva um codigo que leia peso e altura de uma pessoa
Calcule o seu IMC e então Classifique
    abaixo de 18.5 -> abaixo do peso
    entre 18.5 e 25 -> Peso Ideal
    25 até 30 -> Sobrepeso
    30 até 40 -> Obesidade Nivel 2
    acima de 40 -> Obesidade Nivel 3
'''

peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura ** 2) 

if imc < 18.5:
    print('Abaixo de Peso!')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Nivel 02')
    