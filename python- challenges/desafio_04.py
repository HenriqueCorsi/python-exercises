"""
Digite um número para ver a sua tabuada: 
"""

def verificaTabuaada(x):
    print('----------------------')
    cont = 1
    while cont <= 10:
        y = x * cont
        print(f'{x} X {cont} = {y}')
        cont += 1


verificaTabuaada(5)
        


   

