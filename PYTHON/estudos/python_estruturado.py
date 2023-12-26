# Estruturas de decisão

# As estruturas de decisão if, if-else e elif
# if <condição 1>:
#     Bloco de código que será executado caso condição seja True
#  elif <condição 2>:
#    Bloco de código que será executado caso condição 1 seja False e condição 2 seja True
#  else:
#     Bloco de código que será executado caso condição 1 seja False e condição 2 seja False
#  Instrução fora do if


# Estruturas de repetição for:

# As listas do tipo range()
# Ao chamar o método range(), Python cria uma sequência de números inteiros, desde uma maneira simples até a mais
# complexa. Observe:

# Simples:
# Ela pode ser chamada de maneira simples, tendo apenas com um argumento.
# Nesse caso, a sequência começará em 0 e será incrementada de uma unidade até o limite do parâmetro passado (exclusive)
# Exemplo: range(3) cria a sequência (0, 1, 2).

# Não iniciadas em 0:
# Para que a sequência não comece em 0, pode-se informar o início e o fim como parâmetros.
# Lembre-se de que o parâmetro fim não entra na lista (exclusive o fim).
# O padrão é incrementar cada termo em uma unidade. Ou seja, a chamada range(2, 7) cria a sequência (2, 3, 4, 5, 6).

# Indicando início, fim e passo
# Também é possível criar sequências mais complexas indicando, na ordem, os parâmetros de início, fim e passo.
# O passo é o valor que será incrementado de um termo para o próximo. Exemplo: range(2, 9, 3) cria a sequência (2, 5, 8)


# A sintaxe da estrutura for

# for <variável> in <sequência>:
#      Bloco que será repetido para todos os itens da sequência
#  Instrução fora do for


# O laço for com uma string
# nome = input("Entre com seu nome: \n")
# for letra in nome:
#     print(letra)

# As instruções auxiliares break, continue e pass

# A instrução break:
# while True:
#     print('Você está no primeiro laço.')
#     opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
#     if opcao1 == 'SIM':
#         break  # este break é do primeiro laço
#     else:
#         while True:
#             print('Você está no segundo laço.')
#             opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
#             if opcao2 == 'SIM':
#                 break  # este break é do segundo laço
#         print('Você saiu do segundo laço.')
# print('Você saiu do primeiro laço')

# A instrução continue:
# for num in range(1, 10):
#     if num == 5:
#         continue
#     else:
#         print(num)
# print('Laço encerrado')

# A instrução pass (print todos número impar)
# for num in range(1, 11):
#     if num % 2 == 0:
#         pass
#     else:
#         print(num)
# print('Laço encerrado')

