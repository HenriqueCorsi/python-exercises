'''
Faça um código que leia um número inteiro e mostre o seu fatorial sem usar a bibli math.
'''

def calcular_fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos"
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

# Entrada do usuário
numero = 5

# Chamada da função para calcular o fatorial
fatorial = calcular_fatorial(numero)

# Exibição do resultado
print("O fatorial de", numero, "é:", fatorial)

