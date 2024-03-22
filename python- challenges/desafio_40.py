'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. Mostre os 10 primeiros resultados dessa progressão
'''

primeiro_termo = 8
pa = 3
armazena_num = []

while primeiro_termo <=50:
    primeiro_termo = primeiro_termo + pa
    armazena_num.append(primeiro_termo)
    if len(armazena_num) > 10:
        break


print(armazena_num)