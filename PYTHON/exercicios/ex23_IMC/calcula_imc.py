import modulo_imc
peso = eval(input('Informa seu peso:'))
altura = eval(input(f'Informe sua altura:'))
indice = modulo_imc.calcula_imc(peso, altura)
modulo_imc.mostra_imc(indice)
print('Término do Programa')
