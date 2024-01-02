from tkinter import *

def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.pack()

pic = PhotoImage(file="image/logo.png")
logo = Label(master = janelaPrincipal, image = pic)
logo.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()