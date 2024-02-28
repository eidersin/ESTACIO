"""
Frameworks Full-stack
    Disponibilizam diversos recursos internamente, sem a necessidade de bibliotecas externas. Dentre os recursos,
    podemos citar:

        Respostas à requisição;
        Mecanismos de armazenamento (acesso ao banco de dados);
        Suporte a modelos (templates);
        Manipulação de formulários;
        Autenticação;
        Testes;
        Servidor para desenvolvimento, entre outros.
        O principal framework Python full-stack é o Django.


Frameworks não Full-Stack
    Oferecem os recursos básicos para uma aplicação Web, como resposta à requisição e suporte a modelos.
    Os principais frameworks dessa categoria são o Flask e o CherryPy.

    Normalmente, para aplicações maiores, são utilizados os frameworks full-stack, que também são um pouco mais
    complexos de se utilizar.

    Para este módulo, usaremos o Flask.

    OLÁ MUNDO:
                from flask import Flask

                app = Flask(__name__)


                @app.route('/')
                def ola_mundo():
                    return "Olá, mundo."


                if __name__ == '__main__':
                    app.run()


    Rotas e parâmetros:

        Aprimorando rotas:
            Para ilustrar melhor o uso de rotas, vamos alterar o exemplo anterior de forma que a rota (URL) para a
            função ola_mundo seja http://127.0.0.1:5000/ola.

            Observe o script flask2.py e compare com o anterior. Veja que o parâmetro do decorador @app.route da linha
            5 agora é ‘/ola’:

                from flask import Flask

                app = Flask(__name__)


                @app.route('/ola')
                def ola_mundo():
                    return "Olá, mundo."


                if __name__ == '__main__':
                    app.run()

            Vamos acertar nossa aplicação para criar, também, uma rota para a URL raiz da aplicação (@app.route(‘/’)).
            Vamos chamar a função dessa rota de index e criar essa rota conforme linhas 5 a 7. Veja o resultado no
            script flask3.py a seguir:

                from flask import Flask

                app = Flask(__name__)


                @app.route('/')
                def index():
                    return "Página principal."


                @app.route('/ola')
                def ola_mundo():
                    return "Olá, mundo."


                if __name__ == '__main__':
                    app.run()

        Recebendo parâmetros:
            O decorador de rota (route) também permite que sejam passados parâmetros para as funções. Para isso,
            devemos colocar o nome do parâmetro da função entre < e> na URL da rota.

                from flask import Flask

                app = Flask(__name__)


                @app.route('/')
                def index():
                    return "Página principal."


                @app.route('/ola/<nome>')
                def ola_mundo(nome):
                    return "Olá, " + nome


                if __name__ == '__main__':
                    app.run()

            Porém, se tentarmos acessar a URL http://127.0.0.1:5000/ola, receberemos um erro, pois removemos a rota
            para essa URL. Para corrigir esse problema, vamos adicionar uma segunda rota para a mesma função,
            bastando adicionar outro decorador @app.route para a mesma função ola_mundo, conforme o script flask5.py
            a seguir:

                from flask import Flask

                app = Flask(__name__)


                @app.route('/')
                def index():
                    return "Página principal."


                @app.route('/ola/')
                @app.route('/ola/<nome>')
                def ola_mundo(nome="mundo"):
                    return "Olá, " + nome


                if __name__ == '__main__':
                    app.run()


    Métodos HTTP e modelos:

        Métodos HTTP:

                from flask import Flask, request

                app = Flask(__name__)
                app.debug = True


                @app.route('/')
                def index():
                    return "Página principal."


                @app.route('/ola/')
                @app.route('/ola/<nome>')
                def ola_mundo(nome):
                    return "Olá, " + nome


                @app.route('/logar', methods=['GET', 'POST'])
                def logar():
                    if request.method == 'POST':
                        return "Recebeu post! Fazer login!"
                    else:
                        return "Recebeu get! Exibir FORM de login."


                if __name__ == '__main__':
                    app.run()

                ////////////////////////////////////////////////////////////////
                from flask import Flask, render_template

                app = Flask(__name__)


                @app.route('/')
                def index():
                    return render_template('indice.html')


                @app.route('/ola/')
                @app.route('/ola/<nome>')
                def ola_mundo(nome="mundo"):
                    return "Olá, " + nome


                if __name__ == '__main__':
                    app.run()
                //////////////////////////////////////////////////////////////////

                from flask import Flask, render_template

                app = Flask(__name__)

                @app.route('/')
                def index():
                    return render_template('ola.html')

                @app.route('/user/')
                def user():
                    return "Olá, Usuário"

                @app.route('/user/Usuário/')
                def user_usuario(nome = 'programadores'):
                    return "Olá " + nome + "!"

                @app.route('/ola/')
                @app.route('/ola/<nome>')
                def ola_mundo(nome="mundo"):
                    return "Olá, " + nome + "!"


                if __name__ == '__main__':
                    app.run()

"""
