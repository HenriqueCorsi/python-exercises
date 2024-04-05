'''
Crie um codigo que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o program devera se o usuario
quer continuar. No final mostre:
    -> Quantas pessoas a cima de 18 anos temos
    -> Quantos homens foram cadastrados
    -> Quantas mulheres tem menos de 20 anos
'''
import os

def menu():
    os.system('cls')
    print('=================================')
    print('            BEM-VINDO            ')
    print('=================================')

def get_year():
    year = int(input('Idade: '))
    return year

def get_sex():
    sex = input('Sexo [M/F]: ').lower()
    return sex

cont = True
over_18 = []
men_list = []
woman_20 =[]

while cont:
    menu()
    year = get_year()
    sex = get_sex()

    if year >= 18:
        over_18.append(year)
    
    if sex == 'm':
        men_list.append(sex)

    if sex == 'f' and year < 20:
        woman_20.append(sex)
    
    os.system('cls')
    continue_ = input('Cadastrar mais dados [S/N]?').lower()

    if continue_ == 's': # Quer continuar a cadastrar
        os.system('cls')

    elif continue_ == 'n': # Não que continuar cadastrando
        over_total_18 = len(over_18)
        men_total = len(men_list)
        woman_over_20 = len(woman_20)

        os.system('cls')
        print('-----------------------------------------------------------------')
        print(f'O total de pessoas com mais de 18 anos é {over_total_18}')
        print('-----------------------------------------------------------------')
        print(f'O total de homens cadastrados é de {men_total}')
        print('-----------------------------------------------------------------')
        print(f'O total de mulheres com menos de 20 anos é de {woman_over_20}')
        print('-----------------------------------------------------------------')
        cont = False