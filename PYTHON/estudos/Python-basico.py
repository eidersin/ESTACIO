print(f'Exemplo - NÚMEROS')
print(f'1º Exemplo INT -  1_000_000 = {type(1_000_000)}')
print(f'2º Exemplo FLOAT -  50.0 = {type(50.0)}')
print(f'3º Exemplo INT -  2+3+1 = {type(2 + 3 + 1)}')
print(f'4º Exemplo FLOAT -  2+3+1.0 = {type(2 + 3 + 1.0)}')
x, y = 50_00, 100_00
print(f'5º Exemplo INT -  (x, y = 50_00, 100_00) = {type(x+y)}')
x, y = 50.00, 100.00
print(f'6º Exemplo FLOAT -  (x, y = 50.00, 100.00) = {type(x+y)}')
print(f'7º Exemplo POTENCIA INT -  2**3 = {2**3} {type(2**3)}')
print(f'7.1º Exemplo POTENCIA FLOAT -  2.0**3 = {2.0**3} {type(2.0**3)}')
z = 5/2
print(f'8º Exemplo DIV FLOAT -  5/2 = {z} {type(z)}')
print(f'9º Exemplo -  (21//2) = quociente {21//2}')
print(f'9.1º Exemplo -  (21%2) = resto {21 % 2}')
r = complex(2, 5)
print(f'10º Exemplo -  (complex(2,5)) = {r} {type(r)}')
print(f'11º Exemplo BOOL -  (2 < 3) = {2 < 3} {type(2 < 3)}')
print(f'11.1º Exemplo BOOL -  (2 > 3) = {2 > 3} {type(2 > 3)}')
print(f'12º Exemplo NOT BOOL -  (2 < 3) = {not (2 < 3)} {type(not (2 < 3))}')
print(f'12.1º Exemplo NOT BOOL -  (2 > 3) = {not (2 > 3)} {type(not (2 > 3))}')

# Soma                      +               -> 2.5 + 1.3 = 3.8
# Subtração	                -               -> 2.5 - 1.3 = 1.2
# Multiplicação	            *               -> 2.5 * 1.3 = 3.25
# Divisão	                /               -> 2.5/1.3 = 1.923076923076923
# Divisão inteira           //              -> 9//2 = 4
# Resto na divisão inteira  %               -> 9%2 = 1
# Valor absoluto	        abs(parâmetro)  -> abs(-2.5) = 2.5
# Exponenciação	            **              -> 2**4 = 16

# Resultado um valor booleano (True ou False)
#   <       Menor que
#   <=      Menor ou igual a
#   >	    Maior que
#   >=	    Maior ou igual a
#   ==	    Igual
#   !=	    Não igual

# OPERADORES BOOLEANOS
# Operador NOT
#   TRUE -> FALSE
#   FALSE -> TRUE
# Operador AND
#   TRUE + TRUE = TRUE
#   RESTO = FALSE
# Operador OR
#   FALSE + FALSE = FALSE
#   RESTO = TRUE

print('Exemplo - STRING')
curso = 'Ensino a Distância'
print(f'Exemplo: {curso}')
print(f'1º Exemplo UPPER - {curso.upper()}')
print(f'2º Exemplo LOWER - {curso.lower()}')
print(f'3º Exemplo SPLIT - {curso.split()}')

print('Exemplo - LISTAS')
# Listas são sequências mutáveis, normalmente usadas para armazenar coleções de itens homogêneos.
# Uma lista pode ser criada de algumas maneiras, tais como:

# []                          ->  Usando um par de colchetes para denotar uma lista vazia.
# [a], [a, b, c]              ->  Usando colchetes, separando os itens por vírgulas.
# [x for x in iterable]       ->  Usando a compreensão de lista.
# list() ou list(iterable)    ->  Usando o construtor do tipo list.
print(f'1º Exemplo LIST(ABC) - {list('abc')}')
print(f'2º Exemplo LIST(123) - {list('123')}')
print(f'3º Exemplo LIST() - {list('')}')

print('Exemplo - TUPLAS')
# Tuplas são sequências imutáveis, tipicamente usadas para armazenar coleções de itens heterogêneos.
# Elas são aplicadas também quando é necessário utilizar uma sequência imutável de dados homogêneos.
# Uma tupla pode ser criada de algumas maneiras, tais como:

# ()                          ->  Usando um par de parênteses para denotar uma tupla vazia.
# a, b, c ou (a, b, c)        ->  Separando os itens por vírgulas.
# tuple() ou tuple(iterable)  ->  Usando o construtor do tipo tuple.
print(f'1º Exemplo TUPLE(ABC) - {tuple('abc')}')
print(f'2º Exemplo TUPLE([1, 2, 3]) - {tuple([1, 2, 3])}')
print(f'3º Exemplo TUPLE() - {tuple()}')

print('Exemplo - RANGE')
# O tipo range representa uma sequência imutável de números e frequentemente é usado em loops de um número específico de
# vezes, como o for.
# Ele pode ser chamado de maneira simples, apenas com um argumento.
# Nesse caso, a sequência começará em 0 e será incrementada de uma unidade até o limite do parâmetro passado (exclusive)
# Por exemplo, range(3) cria a sequência (0, 1, 2).
# Para que a sequência não comece em 0, podemos informar o início e o fim como parâmetros, lembrando que o parâmetro fim
# não entra na lista (exclusive o fim).
# O padrão é incrementar cada termo em uma unidade. Ou seja, a chamada range(2, 7) cria a sequência (2, 3, 4, 5, 6).
exprange1 = list(range(3))
exprange2 = list(range(2, 7))
exprange3 = list(range(2, 9, 3))
print(f'1º Exemplo list(range(3)) - {exprange1}')
print(f'2º Exemplo list(range(2, 7)) - {exprange2}')
print(f'2º Exemplo list(range(2, 9, 3)) - {exprange3}')

print('Exemplo - OPERADORES SEQUENCIAIS COMUNS')
# Os operadores sequenciais permitem a manipulação dos tipos sequenciais, inclusive as strings.
# Vale ressaltar a sobrecarga dos operadores + e *,
# que realizam operações diferentes quando os operandos são numéricos ou sequenciais.

# Exemplo: O operador == verifica se as strings dos dois lados são iguais.
# Porém, os operadores < e > comparam as strings usando a ordem do dicionário.

# x in s        ->	True se x for um subconjunto de s
# x not in s    ->  False se x for um subconjunto de s
# s + t         ->  Concatenação de s e t
# n*s	        ->  Concatenação de n cópias de s
# s[i]	        ->  Caractere de índice i em s
# len(s)	    ->  Comprimento de s
# min(s)	    ->  Menor item de s
# max(s)	    ->  Maior item de s

print('Exemplo - DICIONÁRIOS')
# Os dicionários permitem que itens de uma sequência recebam índices definidos pelo usuário.
# Um dicionário contém pares de (chave, valor). O formato geral de um objeto dicionário é:

pessoas = {'111222333-44': ['João', 'Silva'], '222333444-55': ['Maria', 'Santos'], '333444555-66': ['Jorge', 'Silva']}
print(pessoas['111222333-44'], pessoas['222333444-55'], pessoas['333444555-66'])

print('Exemplo - RELAÇÃO DE PRECEDÊNCIA ENTRE OPERADORES')
# Ao escrever uma expressão algébrica, o programador pode utilizar a precedência de operadores existente em
# Python (implícita) ou explicitar a ordem em que ele deseja que a expressão seja avaliada.

# [expressões ...]	                    ->  Definição de lista
# x[ ], x[índice : índice]	            ->  Operador de indexação
# **	                                ->  Exponenciação
# +x, -x	                            ->  Sinal de positivo e negativo
# *, /, //, %	                        ->  Produto, divisão, divisão inteira, resto
# +, -	                                ->  Soma, subtração
# in, not in, <, <=,>, >=, <>, !=, ==	->  Comparações, inclusive a ocorrência em listas
# not x	                                ->  Booleano NOT (não)
# and	                                ->  Booleano AND (e)
# or	                                ->  Booleano OR (ou)
print(f'1º Exemplo 3+2*5 = {3+2*5} ')
print(f'2º Exemplo (3+2)*5 = {(3+2)*5} ')

print('Exemplo - CONVERSÕES DE TIPOS DE DADOS')
print(f'1º Exemplo 5(INT)+0.68(FLOAT) = {5+0.68} {type(5+0.68)}')
# O inteiro 5 é convertido pelo Python para o número de ponto flutuante 5.0 antes que a soma (de dois valores float)
# seja realmente efetuada.

# Uma conversão implícita não intuitiva é a dos valores booleanos True e False em inteiros,
# respectivamente, 1 e 0. Veja o exemplo:
true = 1
false = 0
print(f'2º Exemplo true+3(INT) = {true+3} {type(true+1)}')
print(f'3º Exemplo false+1(INT) = {false+1} {type(false+1)}')

# Com isso, podemos perceber a seguinte relação entre os tipos bool, int e float:
print(f'(float(int(bool)))')

# Conversões explícitas, quando ele força que o valor seja tratado como de determinado tipo:
print(f'4º Exemplo número 2(INT) forçado para 2.0(FLOAT) = {float(2)} {type(float(2))}')
print(f'4º Exemplo número 5.1(FLOAT) forçado para 5.0(INT) = {int(5.1)} {type(int(5.1))}')
# O int 2 pode ser tratado naturalmente como o float 2.0, basta acrescentar a parte decimal nula.
# Porém, ao tentar tratar um float como int, ocorre a remoção da parte decimal.
# Atenção! Fique atento, porque não é uma aproximação para o inteiro mais próximo, e sim o truncamento.

# Exemplos de exercícios
print(f'Exercícios')
print(f'Exercício 01')
a = ['10']
b = ['20']
c = ['30']
r = a+b+c
print(f'Qual o resultado da operação: a+b+c: r={r}')

print(f'Exercício 02')
a = ['10']
b = ['20']
c = ['30']
r = a*2+b*3+c*4
print(f'Qual o resultado da operação: a*2+b*3+c*4: r={r}')


print(f'Exercício 03')
# Obter a raiz da equação do primeiro grau
# f(x) = ax+b
a = 10
b = 5
r = -b/a
print(f'A raiz da equação do primeiro grau é: x={format(r)}')

# Atribuição simples
print(f'Atribuição simples')
x = 10
print(f'x=10 : {x}')

# Atribuição múltipla
print(f'Atribuição múltipla')
x, y = 2, 5
print(f'x, y = 2, 5 : {x}, {y}')

# Operadores de atribuição compostos
x = 10
x = x + 1
print(f'x=10, x=x+1 : {x}')
print(f'ou x=10, +=1 : {x}')

# Na tabela a seguir, estão os operadores compostos disponíveis em Python. Considere a variável x,
# com o valor inicial 10, para verificar os resultados:
# Mais igual	+=  -> x += 2  -> x passa a valer 12
x = 10
x += 2
print(f'ou x=10, +=1 : {x}')
# Menos igual	-=  -> x -= 2  -> x passa a valer 8
x = 10
x -= 2
print(x)
# Vezes igual	*=  -> x *= 2  -> x passa a valer 20
x = 10
x *= 2
print(x)
# Dividido igual /= ->	x /= 2 -> x passa a valer 5
x = 10
x /= 2
print(int(x))
# Módulo igual	%=	-> x %= 3  -> x passa a valer 1
x = 10
x %= 3
print(x)

# Troca de variáveis
a = 1
b = 2

# troca de variáveis usando variável auxiliar ‘temp’
temp = a
a = b
b = temp
print(f"O valor da variável a é: {a}")
print(f"O valor da variável b é: {b}")

# troca de variáveis através de atribuição múltipla
a, b = b, a
print(f"O valor da variável a é: {a}")
print(f"O valor da variável b é: {b}")