'''
Crie um código que irá cadastrar 5 nome e sortear um
'''
import random
import os

cont = 1
alunos = []

while cont <= 5:
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

elemento = random.choice(alunos)

os.system('cls')
print(elemento)