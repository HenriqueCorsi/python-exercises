'''
Crie um código que leia o seu nome completo e mostre:
    O nome em maisculo
    O nome em minusculo
    Quantas letras tem sem considerar os espaços
    Quantas letras tem o primeiro nome
'''
def converteMan(x):
    return x.upper()

def converteMin(x):
    return x.lower()

def contName(x):
    return len(x.replace(' ', ''))

def contFirst(x):
    listName = x.split()
    return len(listName[0])

nomeCompleto = 'Paulo Henrique Corsi dos Santos'


print(converteMan(nomeCompleto))
print(converteMin(nomeCompleto))
print(contName(nomeCompleto))
print(contFirst(nomeCompleto))

