"""
- Tkinter:
É o framework GUI padrão do python. Sua sintaxe é simples, possui muitos componentes para interação com o usuário.
Além disso, seu código é aberto e é disponível sob a licença python. Caso ela não esteja instalada na sua versão do
python, basta digitar o comando:

        pip install tkinter

Para testar a instalação, basta escrever o seguinte código na linha de comando:

        import tkinter
        tkinter._test()

/////////////////////////////////////////////////////////////////////////////////
- Flexx
É um kit de ferramentas para o desenvolvimento de interfaces gráficas com o usuário implementado em python que faz uso
de tecnologia web para sua renderização. O Flexx pode ser usado para criar tanto aplicações de desktop como para web e
até mesmo exportar uma aplicação para um documento HTML independente. Para instalar o Flexx, basta digitar o comando:

        pip install flexx

Para testar a instalação, basta escrever o seguinte código na linha de comando:

        from flexx import flx
        class Exemplo(flx.Widget):

            def init(self):
                flx.Button(text='Olá')
                flx.Button(text='Mundo')

        if __name__ == '__main__':
            a = flx.App(Exemplo, title='Flexx demonstração')
            m = a.launch()
            flx.run()



/////////////////////////////////////////////////////////////////////////////////
- CEF python
É um projeto de código aberto voltado para o desenvolvimento de aplicações com integração ao Google Chrome. Existem
muitos casos de uso para CEF. Por exemplo, ele pode ser usado para criar uma GUI baseada em HTML 5, pode usá-lo para
testes automatizados, como também pode ser usado para web scraping, entre outras aplicações.

Para instalá-lo, basta digitar na linha de comando:

        pip install cefpython3

Para testar a instalação do CEF python, basta escrever o código abaixo na linha de comando, ou em um arquivo, e executar

        from cefpython3 import cefpython as cef
        import platform
        import sys
        def main():
            check_versions()
            sys.excepthook = cef.ExceptHook # To shutdown all CEF processes on error
            cef.Initialize()
            cef.CreateBrowserSync(url=" https://www.google.com/",window_title="Olá, mundo! Este é o primeiro exemplo do CEF python")
            cef.MessageLoop()
            cef.Shutdown()

        def check_versions():
            ver=cef.GetVersion()
            print("[hello_world.py] CEF python {ver}".format(ver=ver["version"]))
            print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
            print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
            print("[hello_world.py] python {ver}
            {arch}".format(ver=platform.python_version(),arch=platform.architecture()[0])) assert
            cef.__version__>= "57.0", "CEF python v57.0+ required to run this"


        if __name__ == '__main__':
            main()


/////////////////////////////////////////////////////////////////////////////////
Kivy
É um framework python de código aberto para o desenvolvimento de aplicações com interfaces de usuário e multitoque.
Ele é escrito em python e Cython, baseado em OpenGL ES 2, suporta vários dispositivos de entrada e possui uma extensa
biblioteca de componentes (widgets).

Com o mesmo código, a aplicação funciona para Windows, macOS, Linux, Android e iOS. Todos os widgets Kivy são
construídos com suporte multitoque.

Para instalá-lo, é necessário escrever na linha de comando:

        pip install Kivy


        from kivy.app import App
        from kivy.uix.button import Button

        class ExemploApp(App):
            def build(self):
                return Button(text='Olá, Mundo!')


/////////////////////////////////////////////////////////////////////////////////
Pyforms
É um framework python 3 para desenvolver aplicações que podem operar nos ambientes Desktop GUI, Terminal e Web. A
biblioteca é composta por três sub-bibliotecas, cada uma implementando a camada responsável por interpretar a aplicação
Pyforms em cada ambiente diferente:

        Pyforms-gui.
        Pyforms-web.
        Pyforms-terminal.

Essas camadas podem ser usadas individualmente ou em conjunto, dependendo da instalação do Pyforms. Para fazer a
instalação básica, é necessário escrever na linha de comando:

        pip install pyforms

Uma forma de testar a instalação é escrever e executar o programa:

        import pyforms
        from pyforms.basewidget import BaseWidget
        from pyforms.controls import ControlText
        from pyforms.controls import ControlButton

        class ExemploSimples(BaseWidget):

            def __init__(self):
                super(ExemploSimples,self).__init__('ExemploSimples')
                #Definition of the forms fields
                self._nome = ControlText('Nome', 'Default value')
                self._sobrename = ControlText('Sobrenome')
                self._nomeCompleto = ControlText('Nome completo')
                self._button = ControlButton('Pressione o Botão')


        #Execute the application
        if __name__ == " __main__":
            from pyforms import start_app
            start_app(ExemploSimples)


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Biblioteca Tkinter:

    Widgets Tkinter
O Tkinter possui diversos componentes (widgets), tais como botões, rótulos e caixas de texto usados para criar aplicações interativas com o usuário.

Os principais widgets do Tkinter, de acordo com Meier (2015), são:

- Botão (Button)	É usado para exibir os botões na aplicação. São usados, por exemplo, para confirmar uma ação de
    salvar os dados.
- Telas (Canvas)	É usado para desenhar formas, como linhas, ovais, polígonos e retângulos.
- Botão de verificação (Checkbutton)	É usado para exibir várias opções como caixas de seleção. O usuário pode
    selecionar várias opções ao mesmo tempo.
- Entrada de texto (Entry)	É usado para exibir uma caixa de texto de linha única para que o usuário digite valores de
    entrada.
- Quadros (Frame)	É usado como um widget de contêiner, isso significa que outros componentes são adicionados a ele com
    o objetivo de organizar outros widgets.
- Rótulo (Label)	É usado para fornecer uma legenda de linha única para outros widgets. Também pode conter imagens.
- Caixa de listagem (Listbox)	É usado para fornecer uma lista de opções para um usuário.
- Menubutton	É usado para exibir opções no menu.
- Menu	É usado para fornecer várias possibilidades de comandos a um usuário.
- Esses comandos estão contidos no Menubutton.
- Mensagem (Message)	É usado para exibir uma mensagem de texto e um botão para o usuário confirmar uma ação/td>
- Botão de rádio (Radiobutton)	É usado para exibir várias opções, como botões de rádio. O usuário pode selecionar
    apenas uma opção por vez.
- Escala (Scale)	É usado para fornecer um widget de controle deslizante.
- Barra de rolagem (Scrollbar)	É usado para adicionar capacidade de rolagem a vários widgets.
- Texto (Text)	É usado para exibir texto em várias linhas.
- Toplevel	É usado para fornecer um contêiner de janela separado.
- Spinbox	É uma variante do widget Entry padrão. Ele é usado para selecionar um número fixo de valores.
- PanedWindow	É um widget de contêiner que pode conter qualquer número de painéis, organizados horizontalmente ou verticalmente.
- LabelFrame	É um widget de contêiner simples. Seu objetivo principal é atuar como um espaçador, ou contêiner para layouts de janela.
- tkMessageBox	Este módulo é usado para exibir caixas de mensagens.

Vamos apresentar exemplos dos componentes:

- Widget Window (tk.Tk())
import tkinter as tk
janela = tk.Tk()
janela.title(" Aplicação GUI")
janela.mainloop()

- Widget Label
import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
janela.title(" Aplicação GUI com o Widget Label")
ttk.Label(janela, text="Componente Label" ).grid(column=0, row=0)
janela.mainloop()

- Widget Button
import tkinter as tk
contador = 0
def contador_label(lblRotulo):
   def funcao_contar():
      global contador
      contador = contador + 1
      lblRotulo.config(text=str(contador))
      lblRotulo.after(1000, funcao_contar)
      funcao_contar()
janela = tk.Tk()
janela.title("Contagem dos Segundos")
lblRotulo = tk.Label(janela, fg="green")
lblRotulo.pack()
contador_label(lblRotulo)
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
btnAcao.pack()
janela.mainloop()

- Widget Entry
import tkinter as tk
def mostrar_nomes():
   print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))
janela = tk.Tk()
janela.title("Aplicação GUI com o Widget Entry")
tk.Label(janela,text="Nome").grid(row=0)

tk.Label(janela,text="Sobrenome").grid(row=1)
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(janela, text='Sair',command=janela.quit).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.mainloop()

- Widget Radiobutton
import tkinter as tk
janela = tk.Tk()
v = tk.IntVar()
tk.Label(janela,text=(#Escolha uma linguagem de programação:),justify = tk.LEFT, padx = 20).pack()
tk.Radiobutton(janela,text="python",padx = 25,variable=v,value=1).pack(anchor=tk.W)
tk.Radiobutton(janela,text="C++",padx = 25,variable=v,value=2).pack(anchor=tk.W)
janela.mainloop()

- Widget Text
import tkinter as tk
janela = tk.Tk()
T = tk.Text(janela, height=2, width=30)
T.pack()
T.insert(tk.END, "Este é um texto\ncom duas linhas\n")
tk.mainloop()

- Widget Message
import tkinter as tk
janela = tk.Tk()
mensagem_para_usuario = "Esta é uma mensagem.\n(Pode ser bastante útil para o usuário)"
msg = tk.Message(janela, text = mensagem_para_usuario)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
janela.mainloop()

- Widget Slider
import tkinter as tk
from tkinter import ttk
def mostrar_valores():
   print (w1.get(), w2.get())
janela = tk.Tk()
w1 = ttk.Scale(janela, from_=0, to=50)
w1.pack()
w2 = ttk.Scale(janela, from_=0, to=100, orient=tk.HORIZONTAL)
w2.pack()
ttk.Button(janela, text='Mostrar a Escala', command=mostrar_valores).pack()
janela.mainloop()

- Widget Dialog
import tkinter as tk
from tkinter import messagebox as mb
def resposta():
   mb.showerror("Resposta", "Desculpe, nenhuma resposta disponível!")
def verificacao():
   if mb.askyesno('Verificar', 'Realmente quer sair?'):
      mb.showwarning('Yes', 'Ainda não foi implementado')
   else:
      mb.showinfo('No', 'A opção de Sair foi cancelada')
tk.Button(text='Sair', command=verificacao).pack(fill=tk.X)
tk.Button(text='Resposta', command=resposta).pack(fill=tk.X)
tk.mainloop()

- Widget Combobox
import tkinter as tk
from tkinter import ttk
# Criação de uma janela tkinter
janela = tk.Tk()
janela.title('Combobox')
janela.geometry('500x250')
# Componente Label
ttk.Label(janela, text = "Combobox Widget",background = 'green', foreground ="white",font = ("Times New Roman", 15)).grid(row = 0, column = 1)
# Componente Label
ttk.Label(janela, text = "Selecione um mês :",font = ("Times New Roman", 10)).grid(column = 0,row = 5, padx = 10, pady = 25)
# Componente Combobox
n = tk.StringVar()
escolha = ttk.Combobox(janela, width = 27, textvariable = n)
# Adição de itens no Combobox
escolha['values'] = (' Janeiro',' Fevereiro',' Março',' Abril',' Maio',' Junho',' Julho',' Agosto',' Setembro',' Outubro',' Novembro',' Dezembro')
escolha.grid(column = 1, row = 5)
escolha.current()
janela.mainloop()


"""
# cur.execute('''CREATE TABLE Agenda_teste(ID INT PRIMARY KEY NOT NULL, Nome TEXT NOT NULL, Telefone CHAR(12))''')
# cur.execute("""INSERT INTO public."AGENDA" ("id", "nome", "telefone") VALUES (1, 'Pessoa 1', '02199999999')""")
# cur.execute('''select * from public."AGENDA" where "id"=1''')
# cur.execute('''Update public."AGENDA" set "telefone"='021777777777' where "id"=1''')
# cur.execute('''Delete from public."AGENDA" where "id"=1''')

import psycopg2

conn = psycopg2.connect(database="AGENDA", user="postgres", password="derson123", host="127.0.0.1", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()

# SELECIONAR REGISTRO DA TABELA
cur.execute('''select * from public."AGENDA" where "id"=1''')
registro = cur.fetchone()

# ATUALIZAR REGISTRO DA TABELA
# cur.execute("""Update public."AGENDA" set "telefone"='021666666' where "id"=1""")
# conn.commit()
# print("Registro Atualizado com sucesso! ")
# cur = conn.cursor()
# print(" Consulta depois da atualização")
# cur.execute("""select * from public."AGENDA" where "id"=1""")
# registro=cur.fetchone()
# print(registro)
# conn.commit()

# EXCLUIR REGISTRO DA TABELA
# cur.execute("""Delete from public."AGENDA" where "id"=1""")
# conn.commit()
#cont=cur.rowcount
#print(cont, "Registro excluído com sucesso!")
#print("Exclusão realizada com sucesso!");

print(registro)
conn.close()