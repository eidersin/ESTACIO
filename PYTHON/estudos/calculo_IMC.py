# CALCULO DE IMC
peso = eval(input('Informa seu peso:'))
altura = eval(input(f'Informe sua altura:'))
imc = peso / (altura ** 2)
if imc < 16.9:
    print(f'Seu IMC é: {imc:.1f} Muito abaixo do peso')
elif 17 <= imc < 18.4:
    print(f'Seu IMC é: {imc:.1f} Abaixo do peso normal')
elif 18.5 <= imc < 24.9:
    print(f'Seu IMC é: {imc:.1f} Peso normal')
elif 25 <= imc < 29.9:
    print(f'Seu IMC é: {imc:.1f} Acima do peso normal')
elif 30 <= imc < 34.9:
    print(f'Seu IMC é: {imc:.1f} Obesidade grau 1')
elif 35 <= imc < 40:
    print(f'Seu IMC é: {imc:.1f} Obesidade grau 2')
elif imc >= 40:
    print(f'Seu IMC é: {imc:.1f} Obesidade grau 3')
else:
    print('Calculo de IMC invalido')
