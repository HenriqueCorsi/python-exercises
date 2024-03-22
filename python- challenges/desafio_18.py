'''
Crie um código que leia o nome da pessoa e diga se ela tem silva no nome
'''

nome = 'Paulo Henrique Corsi dos Santos Silva'
nome = nome.lower()

if nome.find('silva') != -1:
    print('True')
else:
    print('False')