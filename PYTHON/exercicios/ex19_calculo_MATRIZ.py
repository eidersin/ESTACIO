from numpy import array
"""
vetor1 = array([1, 2, 3, 4], dtype=int)
vetor2 = array([0, 0, 0, 0], dtype=int)
aux = 0
for elemento in vetor1:
    vetor2[aux] = elemento * 10
    aux += 1
print(vetor2)
"""

"""
matriz = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=int)
aux_linha = 0
aux_coluna = 0
for linha in matriz:
    for elemento in linha:
        if aux_linha == aux_coluna:
            print(elemento)
        aux_coluna += 1
    aux_linha += 1
    aux_coluna = 0
"""