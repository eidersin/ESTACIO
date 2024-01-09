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
