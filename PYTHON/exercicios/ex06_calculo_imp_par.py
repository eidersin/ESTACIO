def ehPar(n1):
    par = n1 % 2 == 0
    return par
def ehImp(n2):
    imp = n2 % 2 != 0
    return imp
def somar_par(lista):
    soma1 = 0
    for num in lista:
        if ehPar(num):
            soma1 = soma1 + num
    return soma1

def somar_imp(lista):
    soma2 = 0
    for num in lista:
        if ehImp(num):
            soma2 = soma2 + num
    return soma2

lista = eval(input('Digite os valores separando por virgula: '))
soma1 = somar_par(lista)
soma2 = somar_imp(lista)
print(f'O somatório dos elementos pares da lista é: {soma1}')
print(f'O somatório dos elementos impar da lista é: {soma2}')