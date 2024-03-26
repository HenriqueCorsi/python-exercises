'''
Desenvola um programa que leia o nome, idade e sexo de 4 pessoas. No final o codigo precisa mostrar:
    -> A Média de idade do grupo
    -> Qual é o nome do homem mais velho
    -> Quantas mulheres tem com menos de 20 anos
'''
import os
import re

# Pega nome
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

# Pega idade
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

# Pega Sexo  
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

# Calcula Média de Idade
def calculate_average_age(age_list):
    age_media = sum(age_list) / len(age_list)
    return age_media


cont = 1
year_list = []
old_men = []
woman_20 = []


while cont <= 4:
    name = get_name()
    year = get_year()
    year_list.append(year)
    sex = get_sex()

    if sex == 'M':
        if len(old_men) == 0:
            old_men.append(year)
        else:
            if  year > old_men[0]:
                old_men[0] = year

    if sex == 'F':
        if year < 20:
            woman_20.append(year)

    cont += 1

os.system('cls')
print(f'A média de idade do grupo é de {calculate_average_age(year_list)} anos')
print(f'A maior idade registrada de um hom é {old_men[0]} anos')
print(f'A quantidade de mulheres com menos de 20 anos é {len(woman_20)}\n\n')


    







        
