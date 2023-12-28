def taximetro_1(distancia):
    largada = 3
    km_rodado = 2
    valor = largada + distancia * km_rodado
    return valor

def taximetro_2(distancia):
    largada = 6
    km_rodado = 4
    valor = largada + distancia * km_rodado
    return valor

taximetro = eval(input("Digite qual o Taximetro 1 ou 2\n"))
if taximetro == 1:
    pagamento = taximetro_1(float(input('Quantos KM rodados: ')))
    print('O valor a ser pago é R${}'.format(pagamento))
elif taximetro == 2:
    pagamento = taximetro_2(float(input('Quantos KM rodados: ')))
    print('O valor a ser pago é R${}'.format(pagamento))
else:
    print("Escolha invalida")




