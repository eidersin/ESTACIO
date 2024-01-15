def calculaDelta(coef1, coef2, coef3):
    #delta da eq2º grau: b^2-4.a.c
    delta = coef2 * coef2 - 4 * coef1 * coef3
    return delta

delta = 0

a = eval(input("Entre com o coeficiente a da equação: "))
b = eval(input("Entre com o coeficiente b da equação: "))
c = eval(input("Entre com o coeficiente c da equação: "))

delta = calculaDelta(a, b, c)
print(f'O valor calculado do delta foi {delta}')

# delta > 0 : euação tem 2 raízes reais
# delta == 0 : equação tem 1 raiz real
# delta < 0 : equação não tem raiz real

if delta > 0:
    print("A equação tem 2 raízes reais")
elif delta == 0:
    print("A equação tem 1 raiz real")
else:
    print("A equação não tem raiz real")