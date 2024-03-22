'''
Crie um código que irá cadastrar 4 alunos e mostre a ordem sorteada

'''
import random
import os

cont = 1
alunos = []

while cont <= 4:
    try:
        os.system('cls')
        nomeAluno = input("Digite o Nome Completo do Aluno: ")      
    except Exception as e:
        os.system('cls')
        print("Valor Inválido! Pressione  ENTER para começar novamente.")
        input()
        os.system('cls')
    else:
        alunos.append(nomeAluno)
        cont += 1 

os.system('cls')
random.shuffle(alunos)
print(alunos)