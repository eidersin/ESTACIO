def dividir():
    try:
        resultado = x / y
        print(resultado)
    except ZeroDivisionError:
        print('Divisão por zero')


x = int(input('Digite primeiro número: '))
y = int(input('Digite segundo número: '))
dividir()
