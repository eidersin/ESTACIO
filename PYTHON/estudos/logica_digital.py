# Portas lógicas e lógica booleana
"""
As operações que são realizadas por um computador digital (binário), vistas como complexas, podem ser compreendidas
como simples combinações de operações aritméticas e lógicas básicas, como visto a seguir:
    Somar bits
    Complementar bits
    Mover bits
    Comparar bits

Estas operações lógicas são implementadas através de circuitos eletrônicos denominados circuitos lógicos, os quais
também são conhecidos como gates ou portas lógicas.

Na lógica digital, há somente duas condições, 1 e 0, e os circuitos lógicos utilizam faixas de tensões predefinidas
para representar esses valores binários. Assim, é possível construir circuitos lógicos que possuem a capacidade de
produzir ações que irão permitir tomadas de decisões inteligentes, coerentes e lógicas.

Análise
A função de um circuito digital é descrita de acordo com a análise de um modo simplificado.

Projeto
A lógica booleana é utilizada para que seja desenvolvida uma implementação simplificada desta função, ao especificar uma determinada função de um circuito.

"""
# Operadores e portas lógicas básicas
"""
Portas lógicas
Uma porta lógica é um componente de hardware que terá um ou muitos sinais de entrada e, como consequência, produzirá um
 sinal de saída de acordo com a lógica estabelecida na construção do circuito em questão.

Os operadores booleanos básicos também denominados como funções lógicas básicas são:
OR
AND
NOT

O operador e a porta OR (OU):
    Em que o sinal (+) não representa uma soma, e sim a operação OR, cuja expressão é lida como:
    X é igual a A OR B.
    Em síntese, na tabela a seguir, estão representadas as combinações dos valores possíveis com a construção da 
    tabela-verdade para o operador OR com duas entradas:
    
    A   B   X
    0   0   0
    0   1   1
    1   0   1
    1   1   1

O operador e a porta AND (E):
    Em que o sinal ( · ) não representa uma multiplicação, e sim a operação AND e a expressão é lida como:
    X é igual a A AND B.
    Em síntese, na tabela a seguir estão representadas as combinações com dois valores de entrada e uma saída para a 
    da Tabela Verdade com o operador AND:
    
    A   B   X
    0   0   0
    0   1   0
    1   0   0
    1   1   1

O operador e a porta NOT (NÃO)
    Como exemplo, se uma variável A for submetida à operação de inversão, o resultado X pode ser expresso como:
        _
    X = A
    Em que a barra sobre o nome da variável representa a operação de inversão e a expressão é lida como:
    X é igual a NOT A ou X é igual a A negado ou X é igual ao inverso de A ou X é igual ao complemento de A.
    Em síntese, a representação da tabela-verdade para o operador NOT com uma entrada e uma saída é a seguir:
          _
    A   x=A
    0   1
    1   0    

# Outras portas lógicas fundamentais:
A porta NOR (Não OU)
    A expressão que representa a porta NOR é:
        _____
    X = A + B
    
    A tabela-verdade a seguir mostra que a saída da porta NOR é exatamente o inverso da saída da porta OR:
    
        OR      NOR
    A   B   X | A+B
    0   0   0 |  1
    0   1   1 |  0
    1   0   1 |  0
    1   1   1 |  0
    
A porta NAND (Não E)
    A expressão que representa a porta NAND é:
        _____
    X = A . B
    
    Em que a barra sobre o nome da variável representa a operação de inversão e a expressão é lida como:
    X é igual a NOT A ou X é igual a A negado ou X é igual ao inverso de A ou X é igual ao complemento de A.
    
    A tabela-verdade a seguir mostra que a saída da porta NAND é exatamente o inverso da saída da porta AND:
    
        AND    NAND
    A   B   X | A.B
    0   0   0 |  1
    0   1   0 |  1
    1   0   0 |  1
    1   1   1 |  0

A porta XOR (Ou exclusivo)
    A expressão que representa a porta NAND é:
    X = A ⊕ B
    
    A porta XOR que é uma abreviação do termo exclusive or, poderá ser considerada como um caso particular da função OR.
    Neste sentido, a porta XOR produzirá um resultado igual a 1 (VERDADEIRO), se pelo menos um dos valores das entradas 
    for diferente dos demais (exclusividade de valor da variável), isto é, a porta produzirá o resultado 0 (FALSO) 
    se — e somente se — todos os valores das entradas forem iguais, conforme é apresentado na tabela-verdade a seguir:
    
    A   B   X = A ⊕ B
    0   0   0
    0   1   1
    1   0   1
    1   1   0

A porta XNOR (coincidência)
    A expressão que representa a porta XNOR é:
    X = A ⊙ B
    
    A tabela-verdade da porta XNOR fica da seguinte forma:
    A   B   X = A ⊙ B
    0   0   1
    0   1   0
    1   0   0
    1   1   1
    
# Avaliação de uma expressão lógica
    Na avaliação de uma expressão lógica, uma ordem de precedência deverá ser seguida da mesma forma que é considerada 
    em uma expressão aritmética, de acordo com o definido a seguir:
    1. Avalie NOT;
    2. Avalie END;
    3. Avalie OR.
    
# Equivalência de funções lógicas
    Conceito: Duas funções lógicas são equivalentes se — e somente se — para a mesma entrada, produzirem iguais valores 
    de saída,  isto é, quando duas funções lógicas possuírem o mesmo resultado na sua tabela-verdade, esses circuitos
    serão considerados como equivalentes.
    
"""
"""
w = not(notB . a)
x = (notB . a) . (notB . w)

     ____   _____
       _        _    
x = (a.b) . w . b

          _____
       _
x =    B . W


(0 + 1 ⊕ 1) + (0 · 0) ⊕ 0.
   (1 ⊕ 1) + 0 ⊕ 0
      1 + 0 ⊕ 0
        1 ⊕ 0
          1

"""

