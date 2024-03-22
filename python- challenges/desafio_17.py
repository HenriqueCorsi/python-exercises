'''
Crie um código que leia o nome de uma cidade e diga se ela começa ou não com a palavras SANTO
'''

def verificaNomeCity(x):
    if x.find('santo') == -1:
         return 'False'
    else:
        return 'True'

nomeCidade = 'Santo André'
nomeCidade = nomeCidade.lower()

print(verificaNomeCity(nomeCidade))