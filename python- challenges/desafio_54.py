'''
Em um cenário de RPG crie uma função que crie NPCs. Elese devem conter:
    -> CLASSE
    -> LEVEL 
    -> HP (hp é 5 * level)
    -> DANO (dano é 100 * level)
    -> 
'''
from random import randint
from os import system

def create_class():
    classe = ['Warrior', 'Mage', 'Thief', 'Archer']
    select_class = classe[randint(0, 3)]
    return select_class

def create_level():
    level = randint(1, 10)
    return level


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

def print_npc(num):
    for x in range(num):
        print(create_npc())



print_npc(2)