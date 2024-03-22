"""
Crie um código onde o professor tenha que lançar 5 notas e no final o programa gera a média do aluno.

"""
def calcula_media(x, y):
    media = x / y
    return f'Média final é {round(media, 2)}'

lista_notas = []
cont = 1

while cont <= 5:
    try:
        n = float(input(f"Nota 0{cont}: "))
    except Exception as e:
        print("Nota Invalida! Pressione ENTER para tentar novamente")
        input()
    else:
        lista_notas.append(n)
        cont += 1

soma_notas = sum(lista_notas)
media_notas = len(lista_notas)

print(calcula_media(soma_notas, media_notas))









