'''
Crie um código que leia uma frase e mostre no final:
    Qtds vezes aparece a lera A
    Em que posição ela aparece a primeiva vez
    Em que posição ela pareec a última vez
'''

frase = 'Amanda ama Pedro'
frase = frase.lower().strip()

print(f'A letra A aparece {frase.count('a')} vezes')
print(f'A prmeira ocorrencia da letra A se encontra na posição {frase.find('a')}')
print(f'A posição que ela aparece é na {frase.rfind('a')}')


