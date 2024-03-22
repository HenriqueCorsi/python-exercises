'''
Crie um código que leia o nome completo de uma pesssoa e mostre em seguida o primeiro e ultimo nome separadamente
'''

nome = 'Paulo Henrique Corsi dos Santos'
listNome = nome.split()

print(f'Seu primeiro nome é {listNome[0]}')
print(f'Seu último nome é {listNome[-1]}')