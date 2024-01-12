#  Classificação das estruturas de dados
"""
Definição:
    Trata-se de uma forma de armazenar e organizar informações para facilitar o acesso e sua modificação.

Características:
    As estruturas de dados podem ser classificadas de acordo com as seguintes características: lineares ou não lineares,
     homogêneas ou não homogêneas, estáticas ou dinâmicas.

    - Lineares ou não lineares:
        Lineares: Estruturas de dados lineares contêm seus dados organizados de forma cronológica ou sequencial,
        isto é, em que um item é adicionado de forma adjacente ao outro.
            Exemplo: A -> B -> C -> D
            Cada item está conectado apenas aos seus vizinhos: o item A só está conectado ao item B (sucessor)
            o item B conectado aos itens A (antecessor) e C (sucessor) e assim por diante.

        Não lineares: As estruturas de dados não lineares, por sua vez, não são organizadas sequencialmente.
            Exemplo:                    A
                                    B   E   F
                                  C   D
            o primeiro item (A) está conectado simultaneamente a três outros itens: B, E e F. Nesse tipo de estrutura
            de dados, não é possível determinar se há uma seqência entre os itens nem quem vem antes ou depois.


    - Homogêneas ou não homogêneas:
        Elas podem ser de:
        Mesmo tipo: Estruturas de dados homogêneas contêm todos os dados do mesmo tipo (inteiro, decimal, caractere etc)

        Tipos diferentes: Estruturas de dados não homogêneas podem conter dados de tipos diferentes.

    - Estáticas e dinâmicas:
        Tamanho fixo: Estruturas de dados estáticas têm seu tamanho fixo, que é definido durante a escrita do código.
        Uma vez alocada a memória para a estrutura, ela não pode ser alterada durante a execução do programa, porém,
        quando ele é iniciado, o espaço alocado para ela é garantido.

        Tamanho variado: Estruturas de dados dinâmicas podem variar de tamanho durante a execução do programa,
        sendo capazes de aumentar ou diminuir. Apesar de tais estruturas serem mais flexíveis, a alocação de memória
        não é garantida; além disso, o aumento descontrolado dessa estrutura pode “estourar” a memória do seu
        computador, fazendo com que seu programa pare.
"""

# Vetores e matrizes
"""
Vetor:
    Os vetores e matrizes são estruturas de dados:
    - Homogêneas: Contêm todos os seus elementos do mesmo tipo (inteiro, decimal, caracteres etc.).
    - Estáticas: Têm seu tamanho delimitado ao longo de sua declaração e continuam fixas durante a execução do programa.
    - Lineares: Têm seus dados organizados de forma sequencial.
    
    As matrizes podem ter várias dimensões. Quando a matriz só possui uma dimensão, ela ganha o nome de vetor.
    
    A imagem a seguir mostra um vetor de números inteiros denominado meu_vetor composto por cinco elementos: 
        meu_vetor:      10, 20, 30, 40, 50. -> Elemento
                        0   1   2   3   4.  -> Índice
                    
    Definindo um vetor:
        from numpy import array
        nome = array([elementos], dtype=tipo)
    
        Nesse caso, nome é o nome da variável; elementos, os itens separados por vírgula que vão compor o vetor; 
        e tipo, o tipo do elemento que será armazenado no vetor como int, float e str. O tamanho do vetor é definido 
        automaticamente pelo número de elementos.
            Exemplo: notas_real = array([2, 5, 10, 20, 50, 100], dtype=int)
    
    Acessando os dados do vetor:
        Em NumPy, podemos acessar um elemento de um vetor da seguinte forma: 
            >>> nome[indice]
        Nesse caso, indice é um número inteiro que representa a posição do elemento no vetor. 
        Em NumPy, o índice começa em 0 (zero).
            Dado:       2   5   10   20   50   100
            Índice:     0   1   2    3    4    5  
            
                Código exemplo:
                from numpy import array
                notas_real = array([2, 5, 10, 20, 50, 100], dtype=int)
                print(notas_real[5])
    
                Exemplo 02:
                from numpy import array
                def main():
                    idades = array([10, 30, 45, 62, 74], dtype=int)
                    print(f"vetor antes da insercao: {idades}")
                    indice = eval(input('Qual índice? ')) # recebe o índice
                    elemento = eval(input(f'Qual novo valor do índice {indice}: ')) # recebe o novo elemento
                    # inserindo o novo elemento escolhido
                    idades[indice] = elemento
                    print(f"vetor depois da insercao: {idades}: ")
                
                # Teste lógico __name__ == "__main__"
                # __name__ é uma variável especial do Python
                # __name__ terá o valor  “__main__” quando o script é executado diretamente
                # (nosso caso, quando o botão Executar do emulador for pressionado)
                # __name__ terá como valor o nome do script (sem o .py) em caso de importação do script como módulo por 
                um outro script
                if __name__ == "__main__":
                    main()
                    
    Iterando o vetor:
    Para percorrer um vetor, utiliza-se a sintaxe: -> for elemento in vetor:
    Nesse caso, elemento é o nome da variável que conterá o valor de cada elemento; vetor, o nome da variável que 
    desejamos percorrer; e (código), o trecho de código que será repetido pelo laço.
    
    Veja o exemplo a seguir. Nele, vamos imprimir todos os elementos do vetor notas_real.
        from numpy import array
        notas_real = array([2, 5, 10, 20, 50, 100], dtype=int)
        for elemento in notas_real:
            print(elemento, end=' - ')
            
            
Matrizes:
    Definindo um matriz: 
    A declaração de matrizes é muito semelhante à de um vetor. Declaramos uma matriz de duas dimensões da seguinte forma
    
        nome = array([ [vetor1], [vetor2], [vetor3], ... ], dtype=tipo)
        
    Nesse caso, nome é o nome da variável, vetor1, vetor2 e vetor3 representam as linhas da matriz e tipo é o tipo do 
    elemento que será armazenado na matriz como int, float e str. O número de colunas será determinado pelo número de 
    elementos dos vetores.
    
    Para representarmos essa tabela como uma matriz, vamos declarar uma variável chamada cadeiras, que é uma matriz com
     elementos do tipo str (caracteres). 
     Teremos dois elementos na primeira dimensão (linha) e três na segunda dimensão (coluna):
    
    cadeiras = array([[“Português”, “Matemática”, “Química”], [“História”, “Geografia”, “Física”]], dtype=str)
    
    Exemplo:
        array = ["Português", "Matemática", "Química"], ["História", "Geografia", "Física"]
        cadeiras = array
        print(cadeiras[1][2])
        cadeiras[1][2] = 'Cálculo'
        print(cadeiras[1][2])
    
    Iterando a matriz:
        from numpy import array
        
        
        def itera_matriz(matriz):
            for linha in matriz:
                print('Início de uma nova linha')
                for elemento in linha:
                    print(elemento)
        
        
        def altera_matriz(matriz, elemento, i, j):
            matriz[i][j] = elemento
            return matriz
        
        
        def main():
            matriz = array([["Português", "Matemática", "Química"], ["História", "Geografia", "Física"]], dtype=str)
            matriz = altera_matriz(matriz, "Teste01", [1][0], [1])
            itera_matriz(matriz)
        
        if __name__ == '__main__':
            main()
        
        
from numpy import array

matriz = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=int)
aux_linha = 0
aux_coluna = 0
for linha in matriz:
    for elemento in linha:
        if aux_linha == aux_coluna:
            print(elemento)
        aux_coluna += 1
    aux_linha += 1
    aux_coluna = 0

"""
# LISTAS
"""
Introdução:
    Algumas estruturas de dados são muito semelhantes, diferindo principalmente na forma como são empregadas. 
    Esse é o caso das listas, pilhas e filas. Neste módulo, falaremos sobre as listas.
    
    Quanto às suas características, as listas são estruturas de dados que podem ser:
        Lineares:
            Têm seus dados organizados de forma sequencial.
        Não homogêneas:
            Podem conter elementos de diferentes tipos (inteiro, decimal, caracteres etc.).
        Dinâmicas:
            Seus tamanhos podem variar durante a execução do programa quando inserimos e removemos elementos.
            
Conceitos de lista:
    Conceitos:
        Em Python, a classe responsável por implementar as listas se chama list. O list é um dos tipos sequenciais 
        básicos do Python, assim como tuple e range. Ele é um tipo de dado interno ao Python e não precisa ser importado

        As listas possuem diversos métodos que podem ser utilizados para realizar diversas ações, como inserir ou buscar 
        elemento, além de inverter e ordenar, entre outros.
    
    Definindo uma lista:
        Para declararmos um objeto do tipo list, podemos proceder de diversas formas:
            Utilizar apenas os colchetes para declarar uma lista vazia: 
                lista = []
            Utilizar os colchetes com os elementos separados por vírgula: 
                lista = [a, b, c]
            Utilizar o construtor list(), que aceita como parâmetro outras coleções:
                lista = list()
                lista = list([1, 2, 3])
    Os elementos de uma lista em Python podem ser de diferentes tipos, incluindo outra lista.
    Exemplo: >>> lista = [1, 'Hello', [1, 2]]
    
    É importante considerar que as listas são sequências mutáveis.
        "Elas podem ser alteradas durante a execução do programa."
    
    Acessando os dados da lista:
        A forma de acessar um elemento da lista é muito similar à das matrizes. Precisa-se apenas do índice do elemento.
    Exemplo: >>> lista = ['a', 'b', 'c', 'b']
             >>> item = lista[1]
             >>> print(item)
            'b'
            
        O método index, que retorna o índice do elemento procurado.    
                lista = ['a', 'b', 'c', 'b']
                indice_c = lista.index('c')
                print(indice_c)
                indice_b = lista.index('b')
                print(indice_b)
        
        Assim como nas matrizes, podemos utilizar o índice de um elemento para alterá-lo.
                lista = ['avião', 'helicóptero', 'carro', 'navio']
                indice_carro = lista.index('carro')
                print(indice_carro)
                print(lista)
                lista[indice_carro] = 'moto'
                print(lista)
        
    Alterando a lista:
        Por ser dinâmico (ou mutável, no linguajar Python), o objeto do tipo list contém um conjunto de métodos que
        permite alterar seus elementos.
        
        Quando precisamos inserir um novo elemento na lista, podemos utilizar os métodos append ou insert. 
        Esses métodos executam as inserções da seguinte forma:
        
            Append: O método append insere o elemento passado como parâmetro no final da lista
            Insert: O método insert insere o elemento na posição indicada no parâmetro.
            Exemplo:
                        lista = list()
                        lista.append('carro')
                        lista.append('moto')
                        lista.append('avião')
                        lista.insert(1, 'bicicleta')
                        print(lista)
                        
        Em algumas ocasiões, precisamos juntar duas listas. Para isso, usamos o método extend, em que passamos 
        uma lista como parâmetro.
            Exemplo:
                        lista_a = [1, 2, 3]
                        lista_b = [4, 5, 6]
                        lista_a.append(lista_b)
                        print(lista_a) >>> [1, 2, 3, [4, 5, 6]]
                        lista_a = [1, 2, 3]
                        lista_a.extend(lista_b)
                        print(lista_a) >>> [1, 2, 3, 4, 5, 6]
                        
            Ao utilizar o método append, o elemento de índice 3 da lista_a passa a ser a lista_b inteira, [4, 5, 6].
            Quando utilizamos o método extend, obtemos o resultado desejado.
            
        O método remove é utilizado para tirar o elemento passado como parâmetro, enquanto o clear remove todos os 
        elementos da lista.
        
        Para usarmos o método remove, não utilizaremos o índice, e sim o valor do elemento:
            Exemplo:
                        lista = ['carro', 'bicicleta', 'moto', 'avião']
                        print(lista) >>> ['carro', 'bicicleta', 'moto', 'avião']
                        lista.remove('bicicleta')
                        print(lista) >>> ['carro', 'moto', 'avião']
                        lista.clear()
                        print(lista) >>> []
                        
        Outras funções da lista:
             .sort >>> para ordenar a lista
             .reverse >>> para inverter os elementos dela.
             Ambos alteram a própria lista!
             Exemplo:
                        lista = [3, 2, 1, 6, 9]
                        print(lista) >>> [3, 2, 1, 6, 9]
                        lista.sort()
                        print(lista) >>> [1, 2, 3, 6, 9]
                        lista.reverse()
                        print(lista) >>> [9, 6, 3, 2, 1]
                        
        Algumas funções internas do Python podem ser aplicadas às listas:
            len() >>> retornam o tamanho da lista
            min() >>> retorna o menor elemento da lista
            max() >>> retorna o maior elemento da lista
            sum() >>> retorna a soma dos elementos da lista
            Exemplo:
                        lista = [3, 7, 2, 6]
                        print(lista) >>> [3, 7, 2, 6]
                        print(len(lista)) >>> 4
                        print(min(lista)) >>> 2
                        print(max(lista)) >>> 7
                        print(sum(lista)) >>> 18
                        
        Também podemos combinar essas funções para alcançar novos objetivos. 
        Exemplo: Vamos calcular a média dos números de uma lista sem percorrê-la apenas utilizando as funções sum e len:
                        lista = [1, 3, 5, 7, 9]
                        print(lista) >>> [1, 3, 5, 7, 9]
                        print(sum(lista)) >>> 25
                        print(len(lista)) >>> 5
                        media = sum(lista) / len(lista)
                        print(media) >>> 5.0
        
        Operadores nas listas:
        Alguns operadores do Python, como os de pertinência (in e not in), 
        equivalência (==), concatenação (+) e multiplicação (*), também podem ser aplicados aos objetos do tipo list.
        
        Todos esses operadores retornam algum objeto, seja um booleano (True ou False), que pode ser utilizado em 
        condicionantes if, seja uma nova lista, como acontece com o operador concatenação (+).
        
            "Todos esses operadores retornam algum objeto, seja um booleano (True ou False), que pode ser utilizado em 
            condicionantes if, seja uma nova lista, como acontece com o operador concatenação (+)."
        Exemplo:
                        lista1 = [1, 2, 3]
                        lista2 = [1, 2, 3]
                        lista3 = [4, 5, 6]
                        print(lista1 == lista2) >>> True
                        print(lista1 == lista3) >>> False
                        if 3 in lista1:
                            print('Achei o 3!!!') >>> Achei o 3!!!
                        nova_lista = lista1 + lista3
                        print(nova_lista) >>> [1, 2, 3, 4, 5, 6]
                        lista_repetida = lista1 * 4
                        print(lista_repetida) >>> [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
        
        Mais sobre as listas:
        Uma funcionalidade muito interessante e útil que o Python disponibiliza é a capacidade de criar listas e
        partir de outras listas de forma simplificada utilizando a chamada compreensão de listas:
        
            A compreensão de listas permite filtrar, transformar e aplicar funções aos elementos de uma lista. 
            Sua sintaxe é:
                Exemplo:
                        lista = [1, 2, 3]
                        print(lista) >>> [1, 2, 3]
                        nova_lista = [item*2 for item in lista]
                        print(nova_lista) >>> [2, 4, 6]
        Para adicionarmos um filtro, colocaremos a condicionante if após a lista. Sua sintaxe será:
            No exemplo adiante, vamos filtrar apenas os elementos pares de uma lista, 
            ou seja, cujo resto da divisão por dois seja zero (%2 == 0):
            Exemplo:    
                        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                        print(lista) >>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                        lista_par = [item for item in lista if item % 2 == 0]
                        print(f'Lista par: {lista_par}') >>> Lista par: [2, 4, 6, 8, 10]
                        lista_impar = [item for item in lista if item % 2 != 0]
                        print(f'Lista impar: {lista_impar}') >>> Lista impar: [1, 3, 5, 7, 9]
                        
        Criando cópias de listas (Shallow Copy versus Deep Copy):
            Exemplo:
                        import copy
                        lista1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                        lista2 = copy.copy(lista1)
                        lista1[2][2] = 10
                        print(f'Lista 01: {lista1}') 
                            >>> Lista 01: [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
                        print(f'Lista 02 com copy da lista1: {lista2}') 
                            >>> Lista 02 com copy da lista1: [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
                        
                        lista1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                        lista2 = copy.deepcopy(lista1)
                        lista1[2][2] = 10
                        print(f'Lista 01: {lista1}') 
                            >>> Lista 01: [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
                        print(f'Lista 02 com deepcopy da lista1: {lista2}') 
                            >>> Lista 02 com deepcopy da lista1: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            
            
"""
# Estrutura de dados Pilha
"""
Pilhas:
    Os elementos são inseridos ou removidos sempre a partir de um único ponto: o topo.
    Assim como as listas, as pilhas são não homogêneas, dinâmicas e lineares. O princípio de funcionamento de uma 
    pilha é o LIFO (do inglês last in, first out, ou seja, último a entrar, primeiro a sair).
    
    As operações de inserção e remoção de um item na pilha são normalmente chamadas de push e pop. Elas fazem as 
    Seguintes inserções:
        Operação push - 
            Insere um item no topo da pilha.
        Operação pop - 
            Remove o item do topo da pilha.
    
    O Python não contém uma classe específica para Pilha, porém a classe list contém dois métodos que fazem com que a 
    lista se comporte como uma pilha. Observe cada um deles:
        Append: Esse método inclui um elemento sempre ao final da lista. Ele faz o papel do push.
        Pop: Esse método retorna e remove o último elemento da lista. Ele faz o papel do próprio pop. 
        
Manipulando os dados da pilha:
                    pilha = []
                    pilha.append(1)
                    pilha.append(2)
                    pilha.append(3)
                    print(pilha) >>> [1, 2, 3]
                    pilha.append(4)
                    print(pilha) >>>  [1, 2, 3, 4]
                    pilha.pop()
                    print(pilha) >>> [1, 2, 3]
                    pilha.pop()
                    print(pilha) >>> [1, 2]

"""
# Estrutura de dados Fila
"""
Filas:
    Os elementos são inseridos sempre no final da fila, enquanto, para remover um elemento, é necessário fazê-lo pela
    frente da fila. O final de uma fila é aquele em que fica o último elemento inserido. Não temos como recuperar um
    lemento do meio da fila sem antes remover todos aqueles à sua frente.
    
    Incluindo e removendo elementos da fila:
        Assim como as listas, as filas são:
            Não homogêneas;
            Dinâmicas;
            Lineares.
            
        Atenção!
        O princípio de funcionamento de uma fila é o FIFO. As operações de inserção e remoção de um item na fila são 
        normalmente chamadas de enqueue e dequeue. 
            O enqueue insere um item no final da fila, 
            enquanto o dequeue o remove do início dela.
        
        Manipulando os dados da fila:
                    fila = []
                    fila.append(1)
                    fila.append(2)
                    fila.append(3)
                    print(fila) >>> [1, 2, 3]
                    fila.append(4)
                    print(fila) >>> [1, 2, 3, 4]
                    fila.pop(0)
                    print(fila) >>> [2, 3, 4]
                    fila.pop(0)
                    print(fila) >>> [3, 4]
            
"""
# Estrutura de dados Tupla
"""
Tuplas:
    Em Python, a classe responsável por implementar Tuplas se chama tuple.
    (É um dos tipos sequenciais básicos do Python, assim como list e range. Tipo de dado interno ao Python, 
    ela não precisa ser importada.
    
    Quanto às suas características, as Tuplas são não homogêneas, pois podem conter elementos de diferentes tipos 
    (inteiro, decimal, caracteres etc.); estáticas, porque seus tamanhos não podem variar durante a execução do programa
    e lineares, já que têm seus dados organizados de forma sequencial.
    
    Definindo uma tupla:
        Utilizar apenas os parênteses para iniciar uma tupla vazia : 
            a.tupla = ()
        
        Utilizar elementos separados por vírgula com ou sem parênteses: 
            a.tupla (a, b, c)
            b.tupla = a, b, c
        
        Para iniciar uma tupla de apenas um item, colocar uma vírgula após esse item 
            a.tupla (a,)
            b.tupla = a,
        
        Utilizar o construtor tuple(), que aceita como parâmetro outras coleções:
            a. tupla = tuple()
            b. tupla = tuple([1, 2, 3])
            c. tupla = tuple((1, 2, 3))
            
        Exemplo: tupla = (1, 'Hello', [1, 2], (3,4))
                 print(tupla) >>> (1, 'Hello', [1, 2], (3, 4))
                
        Diferentemente das listas, as Tuplas são sequências imutáveis.
            (Elas não podem ser alteradas durante a execução do programa.)
            
    Acessando os dados da Tupla:
        A forma de acessar um elemento da Tupla é igual à das listas: precisamos apenas do índice do elemento.
        No exemplo adiante, vamos imprimir o valor do elemento na posição 2, lembrando que o
        primeiro elemento da tupla tem índice 0:
        
                    tupla = ('a', 'b', 'c')
                    item = tupla[2]
                    print(item) >>> 'c'
                    
        Assim como nas listas, podemos utilizar o método index para encontrar o índice de um elemento.   
        
                    tupla = ('a', 'b', 'c')
                    indice_a = tupla.index('a')
                    print(indice_a) >>> 0
        
    Iterando a Tupla:
        As Tuplas são iteráveis (iterable), ou seja, capazes de retornar seus elementos um de cada vez. 
        Para percorrermos as Tuplas, utilizaremos a mesma sintaxe das listas
                    
                    tupla = ('a', 'b', [1, 2, 3], (1, 2, 3))
                    print(tupla) >>> ('a', 'b', [1, 2, 3], (1, 2, 3))
                    for elemento in tupla:
                        print(elemento) >>> a
                                        >>> b
                                        >>> [1, 2, 3]
                                        >>> (1, 2, 3)
                                        
    Alterar a Tupla:
        Como as Tuplas não podem ser alteradas, nenhum dos métodos apresentados para as listas que implicam alguma 
        modificação está presente nas Tuplas, incluindo o sort e o reverse.     
    
    Outras funções da Tupla:
        As funções internas do Python aplicadas às listas também se aplicam às Tuplas: len, min, max e sum, 
        assim como os operadores de pertinência (in e not in), equivalência (==), concatenação (+) e multiplicação (*), 
        também podem ser aplicados aos objetos do tipo tuple. Isso se dá porque todas essas funções e operadores 
        retornam um novo valor e não alteram a tupla.      
        
    Por fim, vamos comparar as Tuplas com as Listas:
        - As Tuplas são mais eficientes que as Listas;
        - As Tuplas podem ser utilizadas como chave para a estrutura de dados Hash implementada em Python, 
        como dicionário, classe dict;
        - As Tuplas podem ser incluídas em conjuntos (sets).
    
    Muitos desenvolvedores veem as Tuplas apenas como listas estáticas, mas os elementos delas normalmente têm um 
    significado. A alteração desses elementos, portanto, pode quebrar a semântica, como, por exemplo, armazenar o dia, 
    o mês e o ano de nascimento de uma pessoa.
    
"""
# Estrutura de dados Conjunto
"""
Conjuntos (Set):
    Em Python, a classe responsável por implementar os Conjuntos se chama Set.
        (Coleção não ordenada cujos elementos são únicos e imutáveis. Ela é um tipo de dado interno ao Python 
        e não precisa ser importada.)
        
        "Os Conjuntos podem ser utilizados para remover itens duplicados de outras sequências ou testes de pertinência e 
        computar operações matemáticas, como união e interseção, entre outras."
        
    Quanto às suas características, os Conjuntos são:
        - Não homogêneos: Pois podem conter elementos de diferentes tipos (inteiro, decimal, caracteres etc.).
        - Dinâmicos: Já que seus tamanhos podem variar durante a execução do programa quando inserimos 
          e removemos elementos.
        - Não lineares: Porque seus dados não são organizados de forma sequencial.
    
    Definindo um conjunto:
        Para inicializarmos um objeto do tipo Set, podemos proceder de duas formas:
            - Utilizar chaves com elementos separados por vírgula:
                    
                    a.conjunto = {1, 2, 3}
                    
            - Utilizar o construtor set(), que aceita como parâmetro outras coleções:
            
                    a.conjunto = set()
                    b.conjunto = ((1, 2, 3))
                    c.conjunto = ([1, 2, 3])
        
        Assim como nas Listas, os elementos de um conjunto podem ser de diferentes tipos, desde que o próprio elemento 
        e seus filhos sejam imutáveis, como no exemplo a seguir, em que temos como elementos um 
        número inteiro, uma string e uma tupla:
        
                    conjunto = {1, 'Hello', (3,4)}
                    print(conjunto) >>> {1, 'Hello', (3, 4)}
                
            Apesar de os elementos de um conjunto serem imutáveis, os Conjuntos são coleções mutáveis, ou seja, 
            eles podem ser alterados durante a execução do programa.
    
    Acessando os dados do Conjunto:      
        Como os Conjuntos não são organizados sequencialmente, eles não armazenam seus elementos em índices; com isso, 
        não podemos acessá-los diretamente pela sua posição, como fazemos nas listas. Para recuperarmos um elemento, 
        precisamos iterar sobre o conjunto ou utilizar o método pop, que será apresentado a seguir.
        
    Iterando o Conjunto: 
        Os Conjuntos, assim como as Listas, também são iteráveis (iterable), ou seja, capazes de 
        retornar seus elementos um de cada vez. Para percorrermos os Conjuntos, utilizamos a mesma sintaxe das Listas, 
        como se pode verificar no exemplo a seguir:
            
                    conjunto = {'a', 1, 2020, (28, 12), 'a'} <<< itens duplicados são automaticamente removidos
                    for elemento in conjunto:
                        print(elemento) >>> a
                                            1
                                            (28, 12)
                                            2020
                                            
        Como os Conjuntos não armazenam seus elementos de forma sequencial, eles são retornados de forma aleatória.
    
    Alterando o Conjunto:
        Quando precisamos inserir um novo elemento no Conjunto, utilizamos o método add. Esse método vai inserir o 
        elemento passado como parâmetro se ele ainda não existir no conjunto.
                    
                    " Lembre-se de que os Conjuntos não contêm objetos repetidos. "
        
                    conjunto = set()
                    print(conjunto) >>> set()
                    conjunto.add(1)
                    conjunto.add(2)
                    print(conjunto) >>> {1, 2}
                    conjunto.add(2) <<< por não conter itens duplicados, a inserção é ignorada
                    print(conjunto)>>> {1, 2}
        
        Além do método para adicionar, o objeto do tipo Set contém métodos para remover elementos do conjunto. 
        Utilizamos o método discard e remove para remover elementos do Set.
        
        Nos dois métodos, o elemento é passado como parâmetro. A diferença é que, caso o elemento não exista, 
        o remove lança um erro, enquanto o discard ignora o comando.

        Também podemos utilizar o método clear para remover todos os elementos do conjunto:
                    
                    conjunto = {1, 2, 3}
                    print(conjunto) >>> {1, 2, 3}
                    conjunto.discard(1)
                    print(conjunto) >>> {2, 3}
                    conjunto.remove(2)
                    print(conjunto) >>> {3}
                    conjunto.discard(5)
                    print(conjunto) >>> {3}
                    conjunto.remove(5)
                    print(conjunto) >>> ERRO
                    conjunto.clear()
                    print(conjunto) >>> 
                    {}
                    
        Podemos extrair itens de forma aleatória do Conjunto utilizando o método pop mediante a simulação de um sorteio.
         Confira no exemplo a seguir:
                    
                    conjunto = {'a', 1, 2, 3}
                    conjunto.pop()
                    print(conjunto) >>> {2, 3, 1} -> aleatorio dessa lista
                    conjunto.pop()
                    print(conjunto) >>> {3, 1} -> aleatorio dessa lista
    
    Outras funções do Conjunto:
    As funções internas do Python que se aplicam às Listas também se aplicam aos Conjuntos: len, min, max e sum.
    Os operadores de pertinência (in e not in) e equivalência (==) também podem ser aplicados aos objetos do tipo Set.
    
        Os objetos do tipo Set disponibilizam alguns métodos relacionados a operações matemáticas. No exemplo a seguir, 
        mostraremos a utilização de alguns deles: union (união), intersection (intercessão) e difference (diferença). 
        Todos esses métodos retornam um novo conjunto.
                    
                    conjunto_a = {1, 2, 3}
                    conjunto_b = {4, 5, 6}
                    conjunto_b = {3, 4, 5}
                    uniao = conjunto_a.union(conjunto_b)
                    print(uniao) >>> {1, 2, 3, 4, 5}
                    intersecao = conjunto_a.intersection(conjunto_b)
                    print(intersecao) >>> {3}
                    diferenca = conjunto_a.difference(conjunto_b)
                    print(diferenca) >>> {1, 2}
    
        O Python permite utilizar operadores para realizar essas mesmas operações:

            operador |: união;
            operador &: interseção;
            operador -: diferença.
                    
"""

