'''
Crie um codigo que ira receber o nome e a idade do usário. Apos receber os dados o sistema deve armazenar as informações
dentro de um arquivo TXT. Crie tambem a opção de vizualizar os dados cadastrados
'''
from modulos_desafio_55.feature import *

while True:
    menu()
    try:
        select_menu = int(input('\n'))
    except Exception as e:
        system('cls')
        print('Valor Inválido!')
        sleep(1)
    else:
        if select_menu == 1:
            nome = pega_nome()
            idade = pega_idade()

            cadastra_dados(nome, idade)
        elif select_menu == 2:
            vizualizar_dados()
        elif select_menu == 3:
            system('cls')
            print('Saindo....')
            sleep(1)
            break
        else:
            system('cls')
            print('Valor Inválido!')
            sleep(1)
      