"""
Propriedades da POO
    1. Abstração: Modelo reduzido;
    2. Encapsulamento: Restringe o acesso a métodos e atributos em uma classe. Em Python, isso é obtido usando métodos
        ou atributos privados usando sublinhado como prefixo, ou seja, "_" simples ou "__" duplo;
    3. Herença: Permite definir uma classe que herda todos os métodos e atributos de outra classe.
    4. Polimorfismo: Permite usar uma única interface com diferentes formas.

    1. Exemplo:
                class Pessoa:
                    def __init__(self, nome, ender):
                        self.set_nome(nome)
                        self.set_ender(ender)

                    def set_nome(self, nome):
                        self.nome = nome

                    def set_ender(self, ender):
                        self.ender = ender

                    def get_nome(self):
                        return self.nome

                    def get_ender(self):
                        return self.ender

                pessoa1 = Pessoa("Maria", "Rua 01234")
                pessoa2 = Pessoa("João", "Rua 56478")

                print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')
                print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}')

    Conceitos e pilares de programação orientada a objetos:

        A Programação Orientada a Objetos (POO) é uma abordagem de programação que revolucionou a estruturação dos
        programas de computador, permitindo a modelagem de problemas do mundo real de forma mais abstrata e próxima à
        realidade.

        A POO permite que os mesmos conceitos e notações sejam usados durante todo o processo de desenvolvimento de
        software, eliminando a necessidade de traduzir conceitos de análise de projetos para a implementação dos
        projetos. Isso é feito através da interação de objetos modelados computacionalmente, que incorporam tanto a
        estrutura quanto o comportamento dos dados.

        Essa abordagem contrasta com a programação convencional, onde a estrutura e o comportamento dos dados são
        geralmente separados. Os modelos baseados em objetos correspondem mais de perto ao mundo real, tornando-os mais
        adaptáveis às mudanças e evoluções dos sistemas.

    Pilares da orientação a objetos:

        Objetos:
            Um objeto em programação orientada a objetos é uma representação de um elemento do mundo real. Ele tem
            características e operações que alteram seu estado. A relevância de um objeto e suas características
            dependem do problema que o sistema está tentando resolver. Por exemplo, para um sistema acadêmico, a
            formação de uma pessoa pode ser relevante, enquanto para um sistema de academia, a altura e o peso podem ser
            mais importantes.

        Atributos:
            São propriedades do mundo real que descrevem um objeto. Cada objeto possui as respectivas propriedades desse
            mundo, as quais, por sua vez, possuem valores. A orientação a objetos define as propriedades como atributos.
            Já o conjunto de valores dos atributos de um objeto define o seu estado naquele momento (RUMBAUGH, 1994).

        Operações:
            Uma operação é uma função ou transformação que pode ser aplicada a objetos ou dados pertencentes a um objeto
            É importante dizer que todo objeto possui um conjunto de operações, as quais, aliás, podem ser chamadas por
            outros objetos com o propósito de colaborarem entre si.

                Esse conjunto de operações é conhecido como interface.

            Exemplo:
                Classe empresa = Contratar_Funcionario, Despedir_Funcionario;
                Classe janela = Abrir, fechar, ocultar.

            O desenvolvimento de um sistema orientado a objetos consiste em realizar um mapeamento conforme o
            apresentado na imagem a seguir.

                OBJETO NO MUNDO REAL  ->  OBJETO COMPUTACIONAL
                    Características         Atributos
                    Comportamento           Operações

            Basicamente, deve-se analisar o mundo real e identificar quais objetos precisam fazer parte da solução do
            problema. Para cada objeto identificado, levantam-se os atributos, que descrevem as propriedades dos objetos
            e as operações, que podem ser executadas sobre tais objetos.

    O conceito de classe:
        A classe descreve as características e os comportamento de um conjunto de objetos. De acordo com a estratégia de
        classificação, cada objeto pertence a uma única classe e possui os atributos e as operações definidos na classe.

        Durante a execução de um programa orientado a objetos, são instanciados os objetos a partir da classe. Assim, um
        objeto é chamado de instância de sua classe.

        A classe é o bloco básico para a construção de programas orientados a objetos (OO), aponta Costa (2015).

    Atenção!
    Cada nome de atributo é único dentro de uma classe; no entanto, essa premissa não é verdadeira quando se consideram
    todas as classes. Por exemplo, as classes Pessoa e Empresa podem ter um atributo comum chamado de Endereço.


"""
