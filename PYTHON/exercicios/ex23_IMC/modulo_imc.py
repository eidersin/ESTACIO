def calcula_imc(peso, altura):
    print('\nInício, seu IMC')
    print(f'Parâmetro peso: {peso}')
    print(f'Parâmetro altura: {altura}')
    imc = float(peso) / float(altura) ** 2
    return imc

def mostra_imc(imc):
    if imc < 16.9:
        return 'Muito abaixo do peso'
    elif 17 <= imc < 18.4:
        return 'Abaixo do peso normal'
    elif 18.5 <= imc < 24.9:
        return 'Peso normal'
    elif 25 <= imc < 29.9:
        return 'Acima do peso normal'
    elif 30 <= imc < 34.9:
        return 'Obesidade grau 1'
    elif 35 <= imc < 40:
        return 'Obesidade grau 2'
    elif imc >= 40:
        return 'Obesidade grau 3'
    else:
        return 'Calculo de IMC invalido'