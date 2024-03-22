'''
Faça um código que leia o ano de nasciento do usuario e informe de acordo com sua idade, se ele ainda vai se alistar
'''
from datetime import date


data = date.today().year
anoNascimento = 2008
idadeUser = data - anoNascimento

if idadeUser > 18:
    saldoIdade = idadeUser - 18
    anoAlistamento = data - saldoIdade
    print(f'Quem nasceu em {anoNascimento} tem nesse momento {idadeUser} anos')
    print(f'Você deveria ter se alistado a {saldoIdade} anos atrá')
    print(f'Seu ano de alistamento foi em {anoAlistamento}')
elif idadeUser == 18:
    print(f'Você precisa de Alistar imediatamente')
else:
    saldoIdade = 18 - idadeUser
    anoAlistamento = saldoIdade + data
    print(f'Quem nasceu em {anoNascimento} tem nesse momento {idadeUser} anos')
    print(f'Você precisa se alistar daque {saldoIdade} anos')
    print(f'Seu ano de alistamento será em {anoAlistamento}')
