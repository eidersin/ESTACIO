quantidade = eval(input('Qual a quantidade de produtos: '))
valor = eval(input('Qual o valor do produto: '))
DES10 = 0.1
DES20 = 0.2
if quantidade <= 10:
    valor_final = (quantidade * valor)
elif quantidade <= 20:
    valor_final = quantidade * valor * (1-DES10)
else:
    valor_final = quantidade * valor * (1-DES20)
print(f'O valor total a ser pago é: R${int(valor_final)}')
