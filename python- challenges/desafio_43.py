'''
Desenvola um programa que leia o nome, idade e sexo de 4 pessoas. No final o codigo precisa mostrar:
    -> A Média de idade do grupo
    -> Qual é o nome do homem mais velho
    -> Quantas mulheres tem com menos de 20 anos
'''
import os
import re

def get_name():
    os.system('cls')
    print('-- SISTEMA DE CADASTRO --')
    cont = True
    while cont:
        name = input('Nome: ')
        if re.match("^[a-zA-Z ]+$", name):
            cont = False
            return name
        else:
            os.system('cls')
            print('Nome inválido! Pressione ENTER para tentar novamente')
            input()
            os.system('cls')

def get_year():
    cont = True
    while cont:
        try:
            year = int(input('Idade: '))
        except Exception as e:
            os.system('cls')
            print('Valor Inválido! Pressio ENTER para tentar novamente')
            input()
            os.system('cls')
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
            os.system('cls')
            print('Nome inválido! Pressione ENTER para tentar novamente')
            input()
            os.system('cls')

def calculate_average_age(age_list):
    age_media = sum(age_list) / len(age_list)
    return age_media










        
