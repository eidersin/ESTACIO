num1 = int(input('Digite primeiro número: '))
num2 = int(input('Digite segundo número: '))
tabuada = input("Escolha qual função da tabuada você quer: [+, -, * ou /] \n")
if tabuada == "+":
    r = num1 + num2
    print('O resultado entre {} + {} vale {}'.format(num1, num2, r))

elif tabuada == "-":
    r = num2 - num1
    print('O resultado entre {} - {} vale {}'.format(num1, num2, r))

elif tabuada == "*":
    r = num1 * num2
    print('O resultado entre {} * {} vale {}'.format(num1, num2, r))
elif tabuada == "/":
    r = num2 / num2
    print('O resultado entre {} / {} vale {}'.format(num1, num2, r))
else:
    r = "Escolha invalida"
