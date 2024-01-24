import math
import meu_modulo
delta = 0

a = eval(input("Entre com o coeficiente a da equação: "))
b = eval(input("Entre com o coeficiente b da equação: "))
c = eval(input("Entre com o coeficiente c da equação: "))

delta = meu_modulo.calculaDelta(a, b, c)
print(f'O valor calculado do delta foi {delta}')

# delta > 0 : euação tem 2 raízes reais
# delta == 0 : equação tem 1 raiz real
# delta < 0 : equação não tem raiz real

if delta > 0:
    print("A equação tem 2 raízes reais")
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'As raízes são {raiz1}, {raiz2}')
elif delta == 0:
    print("A equação tem 1 raiz real")
    raiz = (-b + math.sqrt(delta)) / 2 * a
    print(f'A raiz é {raiz}')
else:
    print("A equação não tem raiz real")
