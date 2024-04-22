'''
Crie um codigo que ira receber o nome e a idade do usário. Apos receber os dados o sistema deve armazenar as informações
dentro de um arquivo TXT. Crie tambem a opção de vizualizar os dados cadastrados
'''
from modulos_desafio_55.feature import *

while True:
    menu() # Chama Menu
    try:
        select_menu = int(input('\n')) # Input Usuário
    except Exception as e:
        system('cls')
        print('Valor Inválido!')
        sleep(1)
    else:
        if select_menu == 1: # Cadastro de nome e idade
            nome = pega_nome() 
            idade = pega_idade()

            cadastra_dados(nome, idade)
        elif select_menu == 2: # Vizualizar Dados cadastrados
            vizualizar_dados()
        elif select_menu == 3: # Sair
            system('cls')
            print('Até Breve!!')
            sleep(1)
            break
        else: # Opção Inválida
            system('cls')
            print('Valor Inválido!')
            sleep(1)
      