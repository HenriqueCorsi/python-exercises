'''
Em um cenário de RPG crie uma função que crie NPCs. Elese devem conter:
    -> CLASSE
    -> LEVEL 
    -> HP (hp é 5 * level)
    -> DANO (dano é 100 * level)
'''
from random import randint
from os import system

list_npc = []

#Cria Classe do NPC
def create_class():
    classe = ['Warrior', 'Mage', 'Thief', 'Archer']
    select_class = classe[randint(0, 3)]
    return select_class

#Cria o Level do NPC
def create_level():
    level = randint(1, 10)
    return level

#Cria Personagem Principal
def create_main_character():
    main_character = {
        'Nome': 'Vann',
        'Classe': 'Ladão',
        'Level' : 1,
        'exp': 0,
        'exp_MAX': 0,
        'HP': 1000,
        'hp_MAX': 1000,
        'Dano': 35
    }

    return main_character

#Cria as caracteristicas do NPC
def create_npc():
    select_class = create_class()
    level = create_level()

    npc = {
        'Classe': f'{select_class}',
        'Level': level,
        'HP': 100 * level,
        'Dano': 5 * level
    }

    return npc

#Cria os NPC e coloca dentro de uma lista
def get_npc(num):
    for x in range(num):
        npc = create_npc()
        list_npc.append(npc)

#Printa na tela os atributos do NPC
def print_npc():
    get_npc(5)
    cont = 0
    for x in list_npc:
        cont += 1
        print(f'NPC: 0{cont} | Classe: {x['Classe']} | Level: {x['Level']} | HP: {x['HP']} | Dano: {x['Dano']}')


print_npc()

