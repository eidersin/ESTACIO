# CALCULO PRIMO
def eh_primo(n):
    if n < 2:
        return False
    i = n // 2
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True
def imprimir_resultado(numero, resultado):
    mensagem = f'O número {numero} NÃO é primo'
    if (resultado):
        mensagem = f'O número {numero} é primo'
    return mensagem

numero = eval(input('Digite um numero: '))
resultado = eh_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)
