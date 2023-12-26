# O primeiro programa em Python

# Entrada de dados com a função Input()
# nome = input('Escreva seu nome: ')
# print(f'Prazer em te conhecer, {nome}')

# A função eval()
# s = '1 + 2'
# print(type(s))
# print(eval(s))

# Entrada de números com a função eval(input())
# idade = eval(input('Informe sua idade:'))
# print(f'Sua idade é {idade}')

# CALCULO DE IMC
# peso = eval(input('Informa seu peso:'))
# altura = eval(input(f'Informe sua altura:'))
# imc = peso / (altura ** 2)
# if imc < 16.9:
#     print(f'Seu IMC é: {imc:.1f} Muito abaixo do peso')
# elif 17 <= imc < 18.4:
#     print(f'Seu IMC é: {imc:.1f} Abaixo do peso normal')
# elif 18.5 <= imc < 24.9:
#     print(f'Seu IMC é: {imc:.1f} Peso normal')
# elif 25 <= imc < 29.9:
#     print(f'Seu IMC é: {imc:.1f} Acima do peso normal')
# elif 30 <= imc < 34.9:
#     print(f'Seu IMC é: {imc:.1f} Obesidade grau 1')
# elif 35 <= imc < 40:
#     print(f'Seu IMC é: {imc:.1f} Obesidade grau 2')
# elif imc >= 40:
#     print(f'Seu IMC é: {imc:.1f} Obesidade grau 3')
# else:
#     print('Calculo de IMC invalido')

# Formatação de dados de saída
# hora = 10
# minutos = 26
# segundos = 18

# print(str(hora) + ' : ' + str(minutos) + ' : ' + str(segundos))
# print('{} : {} : {}'.format(hora, minutos, segundos))
# print(f'{hora} : {minutos} : {segundos}')

# print(f'{10:4},{100:5}')
# print('{:4},{:5}'.format(10, 100))

# Ao usar {:8.5}, estamos determinando que a impressão será com 8 espaços, mas apenas 5 serão utilizados.
# print('{:8.5}'.format(10/3))
# print(f'{10/3:8.5}')

# Impressão de sequências
# seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(seq)

#Para imprimir uma substring
# str = 'Hello World'
# print(str[0:5])
# print(str[2:8])
# print(str[0:11])
# print(str[::-1])
# print(str[8:2:-1])

numero = eval(input('Digite um número decimal: '))
numero_binario = "{0:4b}".format(numero)
print(f'Número da base decimal: {numero}')
print(f'Número da base binária: {numero_binario}')