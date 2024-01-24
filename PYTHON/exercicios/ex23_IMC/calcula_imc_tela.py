from tkinter import *
from tkinter import Button, Entry, Label, messagebox, PhotoImage
import modulo_imc


def acao():
    print('Botão pressionado!!')
    indice = modulo_imc.calcula_imc(peso=peso.get(), altura=altura.get())
    classificacao = modulo_imc.mostra_imc(indice)
    msg = messagebox.showinfo('Classificação IMC', classificacao)


principal = Tk()

# CÓDIGO DA INTERFACE
# Logo
imagem = PhotoImage(file='10481308.png')
logo = Label(principal, image=imagem, anchor=CENTER, width=50, height=50)
logo.image = imagem
logo.grid(row=0, column=0, rowspan=2)

# Etiqueta e caixa de entrada da Altura
etiqueta_altura = Label(principal, text='Altura: ')
etiqueta_altura.grid(row=0, column=1)

altura = Entry(principal)
altura.grid(row=0, column=2)

# Etiqueta e caixa de entrada do Peso
etiqueta_peso = Label(principal, text='Peso: ')
etiqueta_peso.grid(row=1, column=1)

peso = Entry(principal)
peso.grid(row=1, column=2)

# Botão para calcular
botao = Button(principal, text='Calcular', command=acao)
botao.grid(row=2, column=2)

principal.mainloop()
