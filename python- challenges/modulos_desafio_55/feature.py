#Modulos referente ao desafio 55

from os import system
from time import sleep

def menu():
    opcoes = ['[1] Cadastrar', '[2] Vizualizar', '[3] Sair']

    system('cls')
    print('---- BEM VINDO ----')
    for x in opcoes:
        print(x)

#Get name
def pega_nome():
    while True:
        system('cls')
        nome = input('Nome Completo: ')
        if len(nome) != 0:
            return nome
        else:
            system('cls')
            print('Valor Inválido!')
            sleep(1)

#Get age
def pega_idade():
    while True:
        system('cls')
        try:
            idade = int(input('Idade: '))
        except Exception as e:
            system('cls')
            print('Valor Inválido!')
            sleep(1)
        else:
            return idade

def cadastra_dados(num01, num02):
    try:
        arquivo = open("python- challenges/desafio_55.txt", 'a')
    except Exception as e:
        print(f'Erro: {e}')
    else:
        try:
            arquivo.write(f'{num01} -> {num02}\n')
        except Exception as e:
            print(F'Erro: {e}')
        else:
            system('cls')
            print('Cadastrando Dados...')
            sleep(1)
        finally:
            system('cls')
            print('Cadastro Realizado!!')
            sleep(1)
            arquivo.close()

def vizualizar_dados():
        try:
            arquivo = open("python- challenges/desafio_55.txt", 'r')
        except Exception as e:
            print(f'Erro: {e}')
        else:
            system('cls')
            print('--- DADOS CADASTRADOS ---')
            print(arquivo.read())
        finally:
            print('\n\nPressione ENTER para voltar ao menu.')
            input()
            arquivo.close()