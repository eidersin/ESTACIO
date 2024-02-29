"""Visão geral

Introdução:
    Desde o século XVII, as ciências experimentais e teóricas são reconhecidas pelos cientistas como os paradigmas básicos de pesquisa para entender a natureza. De umas décadas para cá, a simulação computacional de fenômenos complexos evoluiu, criando o terceiro paradigma, a ciência computacional.

    A ciência computacional fornece ferramentas necessárias para tornar possível a exploração de domínios inacessíveis à teoria ou experimento.

    Com o aumento das simulações e experimentos, mais dados são gerados e um quarto paradigma emerge, que são as tecnologias e técnicas associadas à Ciência de Dados.

    A Ciência de Dados é uma área de conhecimento que envolve a utilização de dados para gerar impactos em uma instituição, seja uma universidade, uma empresa, um órgão federal etc., de forma a resolver um problema real utilizando os dados.

    Em 1996, Fayyad apresentou a definição clássica do processo de descoberta de conhecimento em bases de dados, conhecido por KDD (Knowledge Discovery in Databases):

            “KDD é um processo, de várias etapas, não trivial, interativo e iterativo, para identificação de padrões compreensíveis, válidos, novos e potencialmente úteis a partir de grandes conjuntos de dados”.



    As técnicas de KDD (FAYYAD, 1996), também conhecidas como mineração de dados, normalmente se referem à extração de informações implícitas, porém úteis, de uma base de dados.

    Essas aplicações, tipicamente, envolvem o uso de mineração de dados para descobrir um novo modelo, e então os analistas utilizam esse modelo em suas aplicações.

    O processo de KDD é basicamente composto por três grandes etapas:

            | Pré-processamento   ----------  Mineração de dados  ----------  Pós-processamento |



    A primeira etapa do processo de KDD, conhecida como pré-processamento, é responsável por selecionar, preparar e transformar os dados que serão utilizados pelos algoritmos de mineração.


        Algumas atividades envolvidas no pré-processamento são:

            - Coleta e integração:
                Quando é necessário que dados provenientes de diversas fontes sejam consolidados em uma única base de dados. Essa atividade é bastante encontrada na construção de data warehouses.

            - Codificação:
                Significa transformar a natureza dos valores de um atributo. Isso pode acontecer de duas diferentes formas: uma transformação de dados numéricos em categóricos — codificação numérico-categórica –, ou o inverso — codificação categórico-numérica.

            - Construção de atributos:
                Pode ser necessário criar colunas em uma tabela, por exemplo, refletindo alguma transformação dos dados existentes em outras colunas, após a coleta e integração dos dados

            - Limpeza de dados
                Pode ser subdividida em complementação de dados ausentes, detecção de ruídos e eliminação de dados inconsistentes.

            - A partição dos dados:
                Consiste em separar os dados em dois conjuntos disjuntos. Um para treinamento (abstração do modelo de conhecimento) e outro para testes (avaliação do modelo gerado).




    A segunda etapa do KDD, conhecida como mineração de dados, é a aplicação de um algoritmo específico para extrair padrões de dados. Hand (2001), define a etapa de mineração de dados da seguinte forma:

                    " Mineração de dados é a análise de (quase sempre grandes) conjuntos de dados observados para descobrir relações escondidas e para consolidar os dados de uma forma tal que eles sejam inteligíveis e úteis aos seus donos. "

        Esta etapa, normalmente, é a que atrai maior atenção, por ser ela que revela os padrões ocultos nos dados.

        Os algoritmos de mineração podem ser classificados como supervisionados e não supervisionados. Nos primeiros, os algoritmos “aprendem” baseados nos valores que cada dado já possui. Os algoritmos são treinados (ajustados), aplicando uma função e comparando o resultado com os valores existentes.

        Já nos não supervisionados, os dados não foram classificados previamente e os algoritmos tentam extrair algum padrão por si só.

        JA seguir, apresentaremos alguns algoritmos que podem ser realizados durante a etapa de mineração de dados.

        Não supervisionados:
            Regras de associação:
                Uma das técnicas de mineração de dados mais utilizada para comércio eletrônico, cujo objetivo é encontrar regras para produtos comprados em uma mesma transação. Ou seja, a presença de um produto em um conjunto implica a presença de outros produtos de outro conjunto; com isso, sites de compras nos enviam sugestões de compras adicionais, baseado no que estamos comprando.

            Agrupamento:
                Reúne, em um mesmo grupo, objetos de uma coleção que mantenham algum grau de afinidade. É utilizada uma função para maximizar a similaridade de objetos do mesmo grupo e minimizar entre elementos de outros grupos.

        Supervisionados:
            Classificação:
                Tem como objetivo descobrir uma função capaz de mapear (classificar) um item em uma das várias classes predefinidas. Se conseguirmos obter a função que realiza esse mapeamento, qualquer nova ocorrência pode ser também mapeada, sem a necessidade de conhecimento prévio da sua classe.

            Regressão linear:
                É uma técnica para se estimar uma variável a partir de uma função. A regressão, normalmente, tem o objetivo de encontrar um valor que não foi computado inicialmente.



    A última etapa do KDD, o pós-processamento, tem como objetivo transformar os padrões dos dados obtidos na etapa anterior, de forma a torná-los inteligíveis, tanto ao analista de dados quanto ao especialista do domínio da aplicação (SOARES, 2007).


Conceitos

    Apresentaremos algumas situações de forma a explicar alguns algoritmos de mineração e como eles podem ser implementados em Python.

    Utilizaremos a biblioteca Pandas para realizar a leitura de dados, a biblioteca Scikit-Learn para realizar o treinamento e utilização dos algoritmos de mineração de dados e a biblioteca Matplotlib para gerar a visualização de resultados.

        Algoritmos supervisionados:

            Supervisionado – regressão linear:

            Algoritmos supervisionados/Script Regressão.Py

"""
""" # EXERCICIO 1:
# Regressão Linear
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([5, 10, 15, 20, 25, 30]).reshape((-1, 1))
y = np.array([6, 12, 14, 23, 27, 32])

model = LinearRegression().fit(x, y)

y_pred = model.predict(x)
print('Dados do teste: ', y, sep='\n')
print('Dados da predição: ', y_pred, sep='\n')

plt.scatter(x, y, c='Blue')
plt.plot(x, y_pred, c='red')
plt.legend(['Predição', 'Real'])
plt.show() """

""" # EXERCICIO 2:

from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt


digitos = load_digits()

print('Shape dos dados de imagens:{}'.format(digitos.data.shape))
print('Shape dos dados rotulados: {}'.format(digitos.target.shape))

plt.figure(figsize=(14,4))
for index, (imagem, rotulo) in enumerate(zip(digitos.data[0:5], digitos.target[0:5])):
    plt.subplot(1, 5, index+1)
    plt.imshow(np.reshape(imagem, (8, 8)), cmap=plt.cm.gray)
    plt.title('Treinamento: {}\n'.format(rotulo, fontsize=15))
plt.show() """

"""from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits

digitos = load_digits()
x_treino, x_teste, y_treino, y_teste = train_test_split(digitos.data, digitos.target, test_size=0.25,
                                                        random_state=0)

pipe = make_pipeline(StandardScaler(), LogisticRegression())
pipe.fit(x_treino, y_treino)

previsto = pipe.predict(x_teste[0].reshape(1, -1))
real = y_teste[0]
print('previsto: {}, real: {}'.format(previsto[0], real))"""


"""import numpy as np
import matplotlib.pyplot as plt

# Dados para o gráfico
x = np.linspace(1, 5, 5)  # Dias
y_alimentacao = [100, 0, 0, 150, 0]  # Despesas de alimentação
y_vestuario = [0, 25, 50, 0, 50]  # Despesas de vestuário
y_transporte = [0, 0, 100, 300, 50]  # Despesas de transporte

# Traçando as linhas
plt.plot(x, y_alimentacao, label='Alimentação', color='lightblue', marker='o', markerfacecolor='blue')
plt.plot(x, y_vestuario, label='Vestuário', color='red', marker='o', markerfacecolor='blue')
plt.plot(x, y_transporte, label='Transporte', color='green', marker='o', markerfacecolor='blue')

# Configurações do gráfico
plt.title('Gráficos de Despesas')
plt.xlabel('Dia')
plt.ylabel('Despesas em R$')
plt.legend()

# Exibindo o gráfico
plt.show()"""

