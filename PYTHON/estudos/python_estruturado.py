"""
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

# A partir desse ponto, serão apresentados os principais aspectos dos seguintes módulos:

Math
Usado para operações matemáticas.

random
Usado para gerar números pseudoaleatórios.

smtplib
Usado para permitir envio de e-mails.

time
Usado para implementar contadores temporais.

tkinter
Usado para desenvolver interfaces gráficas.

Módulo math
Função          Retorno
sqrt(x)         Raiz quadrada de x
ceil(x)         Menor inteiro maior ou igual a x
floor(x)        Maior inteiro menor ou igual a x
cos(x)          Cosseno de x
sin(x)          Seno de x
log(x, b)       Logaritmo de x na base b
pi	            Valor de Pi (3.141592...)
e	            Valor de e (2.718281...)

Módulo random
Esse módulo implementa geradores de números pseudoaleatórios para várias distribuições.

Números inteiros
Para inteiros, existe:
- Uma seleção uniforme a partir de um intervalo.

Sequências
Para sequências, existem:
- Uma seleção uniforme de um elemento aleatório; - Uma função para gerar uma permutação aleatória das posições na lista;
Uma função para escolher aleatoriamente sem substituição.

random()                    Número de ponto flutuante no intervalo (00,0, 1,0)
uniform(a, b)               Número de ponto flutuante N tal que a ≤ N ≤ b
gauss(mu, sigma)            Distribuição gaussiana. mu é a média e sigma é o desvio padrão.
normalvariate(mu, sigma)	Distribuição gaussiana. mu é a média e sigma é o desvio padrão.

Funções para números inteiros:
Função              Retorno
randrange(stop)	    Um elemento selecionado aleatório de range(start, stop, step), mas sem construir um objeto range.
randrange(start, stop, [step])
randint(a, b)	    Número inteiro N tal que a ≤ N ≤ b

Funções para sequências:
Função                  Retorno
choice(seq)             Elemento aleatório de uma sequência não vazia seq.
shuffle(x[, random])	Embaralha a sequência x no lugar.
sample(pop, k)	        Uma sequência de tamanho k de elementos escolhidos da população pop, sem repetição.
                        usada para amostragem sem substituição.

Módulo time:
Função                  Retorno
time()                  Número de segundos passados desde o início da contagem (epoch). Por padrão, o início é 00:00:00
                        do dia 1 de janeiro de 1970.
ctime(segundos)	        Uma string representando o horário local, calculado a partir do número de segundos passado como
                        parâmetro.
gmtime(segundos)	    Converte o número de segundos em um objeto struct_time descrito a seguir.
localtime(segundos)	    Semelhante à gmtime(), mas converte para o horário local.
sleep(segundos)	        A função suspende a execução por determinado número de segundos

Índice	    Atributo	    Valores
0	        tm_year	        Por exemplo, 2020
1	        tm_mon	        range [1, 12]
2	        tm_mday	        range [1, 31]
3	        tm_hour	        range [0, 23]
4	        tm_min	        range [0, 59]
5	        tm_sec	        range [0, 61]
6	        tm_wday	        range [0, 6] Segunda-feira é 0
7	        tm_yday	        range [1, 366]
8	        tm_isdst	    0,1 ou -1
N/A	        tm_zone	        Abreviação do nome da timezone

Módulo tkinter
ex15_primeiraTela.py

# Pacotes externos
Usando pacotes externos
"""
# \Projects\exemplo_pacotes>pip install <nome_do_pacote>.

"""
Nome do módulo	    Pra que serve?
numpy	            Cálculos, operações matemáticas e simulações
pandas	            Manipulaçao de dados
scikit-learn	    Modelos de aprendizado de máquina
matplotlib	        Visualização de dados
requests	        Biblioteca de comandos de comunicação pelo protocolo HTTP
flask	            Construção de aplicações web
"""

# Erros em um programa Python
"""
Exceção	                Explicação
KeyboardInterrupt	    Levantado quando o usuário pressiona CTRL+C, a combinação de interrupção.
OverflowError	        Levantado quando uma expressão de ponto flutuante é avaliada como um valor muito grande.
ZeroDivisionError	    Levantado quando se tenta dividir por 0.
IOError	                Levantado quando uma operação de entrada/saída falha por um motivo relacionado a isso.
IndexError	            Levantado quando um índice sequencial está fora do intervalo de índices válidos.
NameError	            Levantado quando se tenta avaliar um identificador (nome) não atribuído.
TypeError	            Levantado quando uma operação da função é aplicada a um objeto do tipo errado.
ValueError	            Levantado quando a operação ou função tem um argumento com o tipo correto, mas valor incorreto.
    
    Em Python, as exceções são objetos. A classe Exception é derivada de BaseException, classe base de todas as classes
    de exceção. BaseException fornece alguns serviços úteis para todas as classes de exceção, mas normalmente 
    não se torna uma subclasse diretamente.

"""

# Tratamento de exceções e eventos
"""
Captura e manipulação de exceções:
Bloco try
O bloco try é executado primeiramente. Devem ser inseridas nele as instruções do fluxo normal do programa.

Bloco except
O bloco except só será executado se houver o levantamento de alguma exceção.

    Exemplo:
            try:
                num = eval(input("Entre com um número inteiro: "))
                print(num)
            except:
                print("Entre com o valor numérico e não letras")
                
O try representa o fluxo normal do programa. Caso uma exceção seja levantada, o except será executado,
 permitindo o tratamento adequado dela. Esse bloco 2 é chamado de manipulador de exceção.
 
 
 Captura de exceções de determinado tipo:
    Exemplo:
        try:
        num = eval(input("Entre com um número inteiro: "))
        print(num)
    except NameError:
        print("Entre com o valor numérico e não letras")
 
Captura de exceções de múltiplos tipos:
    Exemplo:
        try:
            num = eval(input("Entre com um número inteiro: "))
            print(num)
        except ValueError:
            print("Mensagem 1")
        except IndexError:
            print("Mensagem 2")
        except:
            print("Mensagem 3")
            
            
O tratamento completo das exceções:
    Exemplo:
        try:
          Bloco 1
        except Exception1:
          Bloco tratador para Exception1
        except Exception2:
          Bloco tratador para Exception1
        ...
        else:
          Bloco 2 – executado caso nenhuma exceção seja levantada
        finally:
          Bloco 3 – executado independente do que ocorrer
        Instrução fora do try/except

Tratamento de eventos:
    O tratamento de eventos é similar ao de exceções. Assim como no caso das exceções ocorridas em tempo de execução,
    podemos tratar os eventos criados por ações externas, como as interações de usuário realizadas por meio de uma 
    interface gráfica de usuário (GUI).

"""
minha_lista = [0, 5, 10, 15, 20, 25, 30]


def filtro(numero):
    if numero > 10:
        return True
    return False


minha_lista_filtrada = list(filter(filtro, minha_lista))

print(minha_lista_filtrada)