import numpy as np
def calc_delta(a, b, c):
    delta = b * b - 4 * a * c
    return delta


def calcular_raizes(a, b, c, delta):
    if delta < 0:
        resultado = 'a equação não possui raízes nos números reais'
    elif delta == 0:
        x = -b / (2 * a)
        resultado = f'a equação possui apenas a raiz {x}'
    else:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        resultado = f'a equação possui as raizes: {x1} e {x2}'
    return resultado


a = eval(input('Digite o valor do coeficiente: '))
b = eval(input('Digite o valor do coeficiente: '))
c = eval(input('Digite o valor do coeficiente: '))
delta = calc_delta(a, b, c)
resultado = calcular_raizes(a, b, c, delta)
print(resultado)
