'''
Crie um programa que leia 3 notas e calcula a méida
    Media abaixo de 5 -> Reprovado
    Media entre 5 e 6.9 -> Recuperação
    Média acima de 6.9 -> Aprovado
'''
import os

cont = True
lista_notas = []

while len(lista_notas) < 3 and cont:
    try:
        os.system('cls')
        nota = float(input('Nota: '))
    except Exception as e:
        print('Valor Inválido!! Tente Novamente pressionando ENTER')
        input()
        os.system('cls')
    else:
        lista_notas.append(nota)

        media = sum(lista_notas) / len(lista_notas)

        if media >= 7:
            os.system('cls')
            print(f'Aluno APROVADO!! Média de {round(media, 2)}')
        elif media >= 5 and media < 7:
            os.system('cls')
            print(f'Aluno em RECUPERAÇÃO!! Média de {round(media, 2)}')
        elif media < 5:
            os.system('cls')
            print(f'Aluno REPROVADO!! Média de {round(media,2)}')

