'''
Desenvola um programa que leia o nome, idade e sexo de 4 pessoas. No final o codigo precisa mostrar:
    -> A Média de idade do grupo
    -> Qual é o nome do homem mais velho
    -> Quantas mulheres tem com menos de 20 anos
'''
import os
import re

def get_name():
    cont = True
    while cont:
        name = input('Nome: ')
        if re.match("^[a-zA-Z ]+$", name):
            cont = False
            return name
        else:
            print('Nome inválido! Pressione ENTER para tentar novamente')
            input()

def get_year():
    cont = True
    while cont:
        try:
            year = int(input('Idade: '))
        except Exception as e:
            print('Valor Inválido! Pressio ENTER para tentar novamente')
        else:
            cont = False
            return year
    
def get_sex():
    cont = True
    while cont:
        sex = input('Sexo [M/F]: ').upper()
        if re.match("^[a-zA-Z ]+$", sex) and sex == 'M' or sex == 'F':
            cont = False
            return sex
        else:
            print('Nome inválido! Pressione ENTER para tentar novamente')
            input()
        


nome_usuario = get_name()
idade_usuario = get_year()
sexo_usuario = get_sex()

print(nome_usuario, idade_usuario, sexo_usuario)






        
