def minimo(lista):
    menor_numero = lista[0]
    for elementoMinimo in lista:
        if elementoMinimo < menor_numero:
            menor_numero = elementoMinimo
    return menor_numero


def maior(lista):
    maior_numero = lista[0]
    for elementoMaior in lista:
        if elementoMaior > maior_numero:
            maior_numero = elementoMaior
    return maior_numero


teste = [10, 5, 8, 2, 9, 22]
teste2 = [2, 10, 54, 23, 4, 9]
menor = minimo(teste)
maior = maior(teste2)
print(menor, maior)
