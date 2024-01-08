# Sub-rotinas
"""
Uma sub-rotina possui os seguintes objetivos:
- Dividir e estruturar um algoritmo em partes logicamente coerentes.
- Facilidade em testar os trechos em separado.
- Aumentar a legibilidade de um programa.
- Evitar que uma certa sequência de comandos necessária em vários locais de um programa tenha que ser
escrita repetidamente nestes locais, diminuindo também, o código fonte.


Uma sub-rotina possui as seguintes vantagens:
- Clareza e legibilidade no algoritmo.
- Construção independente.
- Testes individualizados.
- Simplificação da manutenção.
- Reaproveitamento de algoritmos.
"""
# DECOMPOSIÇÃO DE PROBLEMAS
"""
A utilização do método top-down permite que seja realizada uma divisão de problemas em refinamentos sucessivos, da 
seguinte forma:

    01 - Divida o problema em suas partes principais.
    02 - Analise a divisão obtida para garantir corência.
    03 - Se alguma parte ainda estiver complexa, voltar para a primeira etapa
    04 - Analise o resultado para garantir entendimento e coerência
    
Cada divisão obtida com a técnica de refinamentos sucessivos pode ser convertida uma parte do algoritmo. 
Essas partes são conhecidas como módulos ou sub-algoritmos.
"""
# DECLARAÇÃO
"""
Uma sub-rotina é um bloco contendo início e fim, sendo identificada por um nome, pelo qual será referenciada em 
qualquer parte e em qualquer momento do programa.

Como uma sub-rotina é um programa, ela poderá efetuar diversas operações computacionais, como entrada,
 processamento e saída, da mesma forma que são executadas em um programa.

A sintaxe genérica de uma sub-rotina é a seguinte:

    sub-rotina < nome_da_sub-rotina > [(tipo dos parâmetros : < sequência de declarações de parâmetros >)] 
    : < tipo de retorno >
    
    var
        < declaração de variáveis locais >;
    
    Início
            comandos que formam o corpo da sub-rotina
        retorne(< valor >) ; /* ou retorne; ou nada */
    Fim sub-rotina
  """
# CHAMADA DE SUB-ROTINA
"""
Uma sub-rotina pode ser acionada de qualquer ponto do algoritmo principal ou de outra sub-rotina. 
O acionamento de uma sub-rotina é conhecido por chamada ou ativação.
"""

"""
A estratégia para a definição de um algoritmo deve se basear nas seguintes atividades:

1. Especificar um algoritmo através das suas propriedades.
2. Definir sua arquitetura através das suas estruturas de dados.
3. Definir sua complexidade considerando o tempo de execução e espaço ocupado na memória.
4. Implementação em uma linguagem de programação.
5. Execução de testes caixa-branca para submeter entradas e verificar se as saídas obtidas estão de acordo com as 
propriedades especificadas de forma que se prove a corretude do algoritmo.

Segundo Moacir (2002), um algoritmo definido para um problema deve possuir as seguintes características:
Desempenho - Crucial para qualquer software.
Simplicidade - Menor chance de gerar erros na implementação.
Clareza - Escrito de forma clara e documentada para facilitar a manutenção.
Segurança - Deve ser seguro para manipulação de dados.
Funcionalidades - Implementar as funcionalidades requeridas.
Modularidade - Permite manutenção e reuso.
Interface amigável - Importante para a usabilidade dos usuários.

Os passos básicos se referem às operações primitivas utilizadas pela máquina para realizar uma determinada atividade. 
As atividades básicas são:

    Operações aritméticas.
    Comparações.
    Atribuições.
    Resolver um ponteiro ou referência.
    Indexação em um arranjo.
    Chamadas e retornos de funções e métodos.
    
A análise da complexidade de um algoritmo se baseia em dois tipos de complexidade:

    Espacial - Este tipo de complexidade representa, por exemplo, o espaço de memória usado para executar o algoritmo.
    Temporal - Este tipo de complexidade é o mais usado e pode ser dividido em dois grupos:
    Tempo (real) necessário à execução do algoritmo.
    Número de instruções necessárias à execução.
"""