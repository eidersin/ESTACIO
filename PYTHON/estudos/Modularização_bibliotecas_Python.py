# Organização e reuso de software
"""
É extremamente útil organizar nosso código em partes menores quando o programa começa a crescer muito.
Isso ajuda a simplificar a manutenção do código e a sua compreensão. Veja a seguir algumas vantagens (HUNT, 2019):

    Simplicidade: Quebrar um grande problema em pedaços menores ajuda no desenvolvimento de soluções mais focadas,
    acarretando simplicidade na solução. A combinação das pequenas soluções leva à saída do problema como um todo.
    Se considerarmos que cada pequena solução é um módulo, teremos módulos mais simples

    Manutenibilidade: Facilitar a modificação de um módulo simples e até mesmo sua evolução, pois, por ter seus limites
    bem definidos, verificar se ele continua íntegro após algumas modificação é muito mais simples. A identificação
    de erros em códigos menores também é facilitada. Ou seja, a manutenção de módulos pequenos é mais fácil.

    Facilidade para testar: Resolver um problema específico. Por isso, cada módulo pode ser testado de forma isolada,
    mesmo que os demais módulos do programa não estejam prontos.

    Reuso: Definir módulos que realizam tarefas específicas facilita seu reuso em outros programas, visto que suas
    funcionalidades são bem definidas.

        Apesar dos benefícios, nem sempre a reutilização está inserida no contexto organizacional e gerencial.

    É importante especificar o tipo de reuso que se almeja. Nesse contexto, surgem os termos:
    reuso vertical e reuso horizontal. Veja cada um deles a seguir:

        Reuso vertical: Uma análise do domínio é iniciada para produzir uma arquitetura orientada ao reuso de
        desenvolvimentos de componentes, de forma cuidadosa e planejada, que pode proporcionar altos níveis de reuso,
        porém pode-se levar muitos anos para alcançar esse fim.

        Reuso horizontal: Os componentes são genéricos, mas que podem ser de utilidade para outras partes de uma
        organização. Os benefícios no reuso horizontal podem ser vistos em pouco tempo.

            Os programas de reuso mais efetivos se concentram em identificar e desenvolver componentes pequenos e úteis
            e garantir que os usuários (programadores) se sintam motivados e saibam como utilizá-los.

"""
# Desenvolvimento de sistemas em equipe
"""
    Etapa 01: Um arquivo com código-fonte é criado em nosso computador.
    Etapa 02: O arquivo é enviado para o servidor.
    Etapa 03: Um código é editado em nosso computador.
    Etapa 04: A modificação é enviada para o servidor.
    Etapa 05: O servidor compara com a versão armazenada e tenta unificar o código.
    Etapa 06: O desenvolvedor recebe uma mensagem solicitando que ele mesmo faça essa junção, caso o servidor não 
    consiga unificar o código devido a algum conflito.
    Etapa 07: O desenvolvedor, após resolver o conflito, envia novamente o arquivo para o servidor, que passa a ser a 
    última versão válida.
    Etapa 08: O código atualizado fica disponível para todos que têm acesso ao repositório.
    
        Algumas ferramentas, como o GitLab, permitem trabalhar com integração contínua. A cada modificação no código 
        enviada ao servidor, ele compila, testa e valida o novo código antes de efetivar a modificação no repositório. 
        Isso visa garantir a integridade do código fonte existente.
"""
# Tipos de testes de software
"""
Os testes são tão importantes que existem metodologias de desenvolvimento baseadas em teste, 
como o Test Driven Development (TDD) ou Desenvolvimento Guiado por Testes.

    Dica: Durante o desenvolvimento de programas, devemos constantemente testar nosso código, de forma a certificar 
    que não existam erros.
    
Nessa metodologia, as descrições dos testes são escritas antes mesmo do código, começando com o desenho e 
desenvolvimento dos testes para cada pequena funcionalidade do programa.

    O objetivo do TDD é fazer com que o código fique limpo, simples e livre de erros.

Quando rodamos nossa aplicação e verificamos as funcionalidades que acabamos de implementar estamos realizando.
Estamos realizando um tipo de teste chamado teste exploratório, que é uma das formas de realizar testes manualmente.

    Nos testes exploratórios, não temos um plano de testes a seguir, apenas estamos, como o próprio nome já diz, 
    explorando as funcionalidades da aplicação.

Os testes podem ser divididos em testes unitários (unit test) e testes de integração (integration test):
    Testes unitários: Verificam uma pequena parte da aplicação.
    Testes de integração: Verificam como os diversos componentes interagem entre si.
    
        Ambos os testes são suportados em Python.


"""
# Desenvolvimento e uso de funções em Python
"""
Visão geral:
    Funções em Python: A função é um bloco de instruções que executa uma determinada tarefa e, uma vez definida, pode 
    ser reutilizada em diferentes partes do programa.
    
    As funções permitem que o código fique mais modular, possibilitando executar a mesma tarefa diversas vezes sem a 
    necessidade de reescrever o código. A modularização facilita a manutenção e divisão das tarefas.

    Como exemplo de funções disponibilizadas pelo Python, temos o print, dir, help, entre outras.
"""
# Definição de funções
"""
Como definir uma função sem parâmetros:
    A forma mais simples de defini-la utiliza a seguinte sintaxe:
    
                def nome():
                    linha1
                    linha2
                    ...
                    linhaN
                    
    Utilizamos a palavra reservada def seguida do nome que desejamos dar à nossa função, 
    um par de parênteses e dois pontos.
    
    Esse nome será utilizado para chamar nossa função em um momento posterior e, assim como nome de variável, precisa 
    seguir algumas regras. Os nomes podem ser compostos por letras, underline (_) e números de 0 a 9, exceto o primeiro 
    caractere.
    
                Atenção!: Em Python, não utilizamos chaves para delimitar o corpo de uma função, como ocorre em outras 
                linguagens de programação.
                
    De acordo com a PEP8, basta indentar o código em 4 espaços e todas as linhas indentadas farão parte do corpo da 
    função.
    
    Para executar, ou chamar, uma função, escrevemos o nome dela seguido por um par de parênteses:
                
                def hello():
                print('Inicio do Programa')
                print('Hello', end=' ')
                print('World')
                hello()
                print('Término do Programa')
                
    Como definir uma função com parâmetros:
        Frequentemente, as funções executam suas tarefas utilizando informações do usuário. Como nem sempre sabemos 
        quais dados o usuário irá informar, precisamos de uma forma de passar essa informação para a função durante a
        execução do programa.
        
                Curiosidade: Na computação, os dados que uma função espera receber são chamados de parâmetros.
                
                def calcula_imc(peso, altura):
                    print('Parâmetro peso: ', peso)
                    print('Parâmetro Altura: ', altura)
                    imc = peso / altura ** 2
                    print('IMC: {:.2f}'.format(imc))
            
                print('Inicio do Programa')
                peso = float(input('Informe o peso: '))
                altura = float(input('Informe a altura: '))
                calcula_imc(peso, altura)
                print('Término do Programa')
        
                Dica: Quando utilizamos os nomes, podemos usar os parâmetros fora de ordem, pois o Python vai utilizar 
                esses nomes para combinar corretamente parâmetro e argumento.
"""
# Retorno de valores em funções
"""
Como receber os resultados de uma função:
    É muito comum na programação que as funções produzam algum valor que precise ser utilizado no decorrer do programa. 
    Nesses casos, dizemos que a função retorna um valor. O valor retornado, normalmente, é atribuído a alguma variável 
    para ser armazenado e utilizado posteriormente. Para retornar um valor, ao final da função, precisamos utilizar a 
    palavra reservada return seguida do valor ou variável que se deseja retornar (ou em branco, caso a função não 
    retorne valor algum).
    
            Relembrando: Lembre-se de que retornar um valor é diferente de imprimir um valor na tela!
            
                    def calcula_imc(peso, altura):
                        print('Parâmetro peso:', peso)
                        print('Parâmetro altura:', altura)
                        imc = peso / altura ** 2
                        return imc


                        print('Inicio do programa...')
                        indice = calcula_imc(altura=1.80, peso=70)
                        print(f'IMC: {indice:.2f}')
                        if indice < 18.5:
                            print('Abaixo do peso')
                        elif indice < 25:
                            print('Peso normal')
                        elif indice < 30:
                            print('Sobrepeso')
                        else:
                            print('Obesidade')
                        print('Término do Programa')
    
            Exemplo que utilizamos a palavra chave return seguida da variável imc. Isso indica que a função retornará o 
            valor contido na variável imc, que foi calculado.
            
    Isso é muito comum e, na prática, indica que a variável indice receberá o valor retornado pela função calcula_imc.
    
Funções de ordem superior (higher order definition):
                        def selecionador(seq, teste):
                            selecionados = []
                            for elemento in seq:
                                if teste(elemento):
                                    selecionados.append(elemento)
                            return selecionados
                        def verifica_par(num):
                            if num % 2 == 0:
                                return True
                            else:
                                return False
                        
                        def main():
                            lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                            numeros_pares = selecionador(lista, verifica_par)
                            for num in numeros_pares:
                                print(f' {num} -> par')
                        
                        if __name__ == '__main__':
                            main()
"""



