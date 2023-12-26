# CALCULO FATORIAL
numero = eval(input('Digite um numero: '))


# ESTRATÉGIA 01
def fatorial_iterativo(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


# ESTRATEGIA 2
def fatorial_recursivo(n):
    if (n == 0) or (n == 1):
        return 1
    return n * fatorial_recursivo(n - 1)


print(f'O fatorial de {numero} é: {fatorial_iterativo(numero)}')
print(f'O fatorial de {numero} é: {fatorial_recursivo(numero)}')
