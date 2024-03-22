'''
Faça um código que calcule a soma entre todos os números impares que são multiplos de 3 que se encontra em um intervaldo de 1 a 500
'''

cont = 0
number_list = []

while cont < 500:
    cont += 1
    if cont % 2 != 0 and cont % 3 == 0:
        number_list.append(cont)
    
sum_value = sum(number_list)

print(sum_value)


