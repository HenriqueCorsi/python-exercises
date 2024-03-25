'''
Desenvola um programa que leia o nome, idade e sexo de 4 pessoas. No final o codigo precisa mostrar:
    -> A Média de idade do grupo
    -> Qual é o nome do homem mais velho
    -> Quantas mulheres tem com menos de 20 anos
'''
import os
import re

def get_name():
    while True:
        name = input('Nome: ')
        if re.match("^[a-zA-Z ]+$", name):
            return name
        else:
            print('Nome inválido! Por favor, digite apenas letras e espaços.')

nome_usuario = get_name()






        
