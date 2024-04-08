'''
Crie uma lista preenchida com os 20 primeiros colcoaos do Campeonato BR de 2023. Depois mostre:
    -> Os 5 primeiros Times
    -> Os 4 ultimos times
    -> Em que posição esta o Santos 
'''
import os

def conf():
    print('============================')

table_camp = [
     'Palmeiras', 'Gêmio', 'Atlético MG', 'Flamengo', 'Botafogo', 'RB Bragantino', 'Fluminense', 'Athletico PR', 'Internacional', 'Fortaleza', 'São Paulo',
     'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América MG'
]

top_fiven = table_camp[:5]
last_four = table_camp[-4:]
position_santos = table_camp.index('Santos')

os.system('cls')
conf()
print('TOP FIVE')
print(top_fiven)
conf()
print('LAST-FOUR')
print(last_four)
conf()
print('POSITION SANTOS')
print(position_santos)

