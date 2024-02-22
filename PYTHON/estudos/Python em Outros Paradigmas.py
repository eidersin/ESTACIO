# Linguagem funcional no Python
"""
Relação entre funções puras e dados imutáveis:
    Funções puras:
        Funções puras são aquelas que geram uma saída baseada apenas nos parâmetros de entrada. Elas sempre retornam um
        resultado consistente para os mesmos parâmetros, seja um valor, objeto ou outra função.

        Exemplo 01:
        # script funcao1.py
        valor = 20

        def multiplica(fator):
            global valor
            valor = valor * fator
            print("Resultado", valor)

        def main():
            numero =int(input())
            multiplica(numero)
            multiplica(numero)

        # Quando um script python é executado, a variável reservada
        # NAME referente a ele tem valor igual à "__main__".
        # Nesse caso, a condição do IF a seguir será TRUE,
        # então o que está no corpo do IF será executado.
        # No caso, é um chamado ao método main do script

        if __name__ == "__main__":
            main()


        Exemplo 02:
        # script funcao2.py
        valor = 20

        def multiplica(valor, fator):
            valor = valor * fator
            return valor

        def main():
            numero = int(input())
            print("Resultado", multiplica(valor, numero))
            print("Resultado", multiplica(valor, numero))

        if __name__ == "__main__":
            main()


    Dados imutáveis:
        Na programação funcional, os dados são tratados como imutáveis, ou seja, não podem ser alterados após a criação.
        As funções puras, que são um conceito chave, usam apenas os parâmetros de entrada para gerar as saídas e não
        alteram variáveis fora de seu escopo.

        Em Python, quando passamos uma lista como argumento para uma função, estamos passando sua referência. Portanto,
        qualquer mudança na lista dentro da função também altera a lista original. Isso pode levar a resultados
        indesejáveis se a função for chamada mais de uma vez com o mesmo parâmetro.

        Para evitar isso, em vez de alterar a lista original, podemos criar uma cópia dela dentro da função. Assim, a
        lista original permanece inalterada e obtemos o mesmo resultado para chamadas de função repetidas.



Efeitos indesejáveis:
    Efeito colateral e estado da aplicação:
        Na programação funcional, funções puras e dados imutáveis são usados para evitar efeitos colaterais indesejados.
        Isso significa que o resultado de uma função depende apenas dos parâmetros de entrada, e não do estado do
        programa. Assim, a função sempre terá o mesmo comportamento, independentemente do estado da aplicação.

        Além disso, ao garantir que uma função só use os dados de entrada para gerar um resultado e que nenhuma variável
        fora do escopo da função seja alterada, podemos ter certeza de que não haverá efeitos colaterais escondidos em
        outras partes do código.

        O principal objetivo da programação funcional, portanto, não é apenas usar funções puras e dados imutáveis, mas
        evitar efeitos colaterais.



Boa prática de programação:
    Não utilizar loops:
        Outra regra, ou boa prática, da programação funcional é não utilizar laços (for e while), mas sim composição de
        funções ou recursividade.
        A função lambda exerce um papel fundamental nisso, como veremos a seguir.
        Para facilitar a composição de funções e evitar loops, o Python disponibiliza diversas funções e operadores.
        As funções internas mais comuns são map e filter.

    Maps:
        A função map é uma ferramenta que aplica uma função específica a cada item de uma lista ou outro tipo de
        conjunto de dados (como tuplas ou dicionários), criando um novo conjunto de dados com os resultados. Ela é
        considerada uma função pura e de ordem superior, pois seu comportamento depende apenas de seus parâmetros e ela
        aceita outra função como parâmetro.

        Em termos simples, map pega uma função e um conjunto de dados, aplica a função a cada item do conjunto de dados
        e retorna um novo conjunto de dados com os resultados.

        Por exemplo, se tivermos uma lista de números e quisermos triplicar cada número, podemos usar a função map para
        fazer isso de forma eficiente.

    Exemplos:
            # script funcao_iterable.py
            lista = [1, 2, 3, 4, 5]

            def triplica_itens(iterable):
                lista_aux = []
                for item in iterable:
                    lista_aux.append(item*3)
                return lista_aux

            def main():
                nova_lista = triplica_itens(lista)
                print(nova_lista)

            if __name__ == "__main__":
                main()



            # script funcao_map.py
            lista = [1, 2, 3, 4, 5]

            def triplica(item):
                return item * 3

            def main():
                nova_lista = map(triplica, lista)
                print(list(nova_lista))

            if __name__ == "__main__":
                main()



            # script funcao_map_lambda.py
            lista = [1, 2, 3, 4, 5]

            nova_lista = map(lambda item: item * 3, lista)# função lambda

            def main():
                print(list(nova_lista))

            if __name__ == "__main__":
                main()


    Filter:
        A função filter é usada para selecionar elementos de uma lista ou outro tipo de conjunto de dados com base em um
        critério definido por uma função. Essa função deve retornar verdadeiro ou falso para cada elemento.

        Em termos simples, filter pega uma função e um conjunto de dados, aplica a função a cada item do conjunto de
        dados e retorna um novo conjunto de dados contendo apenas os itens para os quais a função retornou verdadeiro.

        Por exemplo, se tivermos uma lista de números e quisermos selecionar apenas os números ímpares, podemos usar a
        função filter para fazer isso de forma eficiente.

        Exemplo:
            # script funcao_filtro_iterable.py
            lista = [1, 2, 3, 4, 5]

            def impares(iterable):
                lista_aux = []
                for item in iterable:
                    if item % 2 != 0:
                        lista_aux.append(item)
                return lista_aux

            def main():
                nova_lista = impares(lista)
                print(nova_lista)

            if __name__ == "__main__":
                main()


            # script funcao_filter.py
            lista = [1, 2, 3, 4, 5]

            def impar(item):
                return item % 2 != 0

            def main():
                nova_lista = filter(impar, lista)
                print(list(nova_lista))

            if __name__ == "__main__":
                main()


            # script funcao_filter_lambda.py
            lista = [1, 2, 3, 4, 5]

            nova_lista = filter(lambda item: item % 2 != 0, lista)

            def main():
                print(list(nova_lista))

            if __name__ == "__main__":
                main()


"""



