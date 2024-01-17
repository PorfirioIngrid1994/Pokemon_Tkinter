from tkinter import *
from tkinter import Tk, ttk, Frame, Label, PhotoImage, Button
from tkinter import HORIZONTAL
from PIL import Image, ImageTk
from Dados import Pokemon


# Cores:
cor0 = "#444466"  # Preto
cor1 = "#feffff"  # Branco
cor2 = "#6f9fbd"  # Azul
cor3 = "#38576b"  # Valor
cor4 = "#403d3d"  # Letra
cor5 = "#ef5350"  # Vermelho

# Criar janela:
janela = Tk()
janela.title('Pokedex')
janela.geometry('550x510')
janela.configure(bg=cor1)

# Icone da janela:
icone = PhotoImage(file="C:\\Users\\Ingrid Porfirio\\Documents\\Pokemon-Python\\Imagens\\pokebola.png")
janela.iconphoto(False, icone)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use('clam')

# Criando frame:
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def trocar_pokemon(i):
    global Image_pokemon, pok_image

    #Trocar o fundo: 

    frame_pokemon['bg'] = Pokemon[i]['Tipo'][3]


    # Tipo de pokemon:
    pok_nome['text'] = i
    pok_nome['bg'] = Pokemon[i]['Tipo'][3]
    pok_id['text']= Pokemon[i]['Tipo'][0]
    pok_id['bg'] = Pokemon[i]['Tipo'][3]
    pok_tipo['text'] = Pokemon[i]['Tipo'][1]
    pok_tipo['bg'] = Pokemon[i]['Tipo'][3]
    Image_pokemon = Pokemon[i]['Tipo'][2]

    # Imagem do Pokemon:
    Image_pokemon = Image.open(Image_pokemon)
    Image_pokemon = Image_pokemon.resize((238, 238))
    Image_pokemon = ImageTk.PhotoImage(Image_pokemon)

    pok_image = Label(frame_pokemon, image=Image_pokemon, relief='flat', bg= Pokemon[i]['Tipo'][3], fg=cor1)
    pok_image.place(x=60, y=50)

    #Status:

    pok_categoria['text'] = Pokemon[i]['Status'][0]
    pok_altura['text'] = Pokemon[i]['Status'][1]
    pok_peso['text'] = Pokemon[i]['Status'][2]
    pok_habilidade['text'] = Pokemon[i]['Status'][3]

    #Principais Ataques e Fraquezas:

    pok_ataques['text'] = Pokemon[i]['Principais Ataques e Fraquezas'][0]
    pok_fraquezas['text'] = Pokemon[i]['Principais Ataques e Fraquezas'][1]

    pok_id.lift()

# Nome:
pok_nome = Label(frame_pokemon, text='', relief='flat', anchor="center", font=('Fixedsys 20'), bg=cor1, fg=cor1)
pok_nome.place(x=12, y=15)

# Tipo:
pok_tipo = Label(frame_pokemon, text='Fogo', relief='flat', anchor="center", font=('Ivy 10 bold'), bg=cor1, fg=cor1)
pok_tipo.place(x=12, y=50)

# id:
pok_id = Label(frame_pokemon, text='', relief='flat', anchor="center", font=('Ivy 10 bold'), bg=cor1, fg=cor1)
pok_id.place(x=12, y=75)

# Status:
pok_status = Label(janela, text='Status', relief='flat', anchor="center", font=('Verdana 16'), bg=cor1, fg=cor4)
pok_status.place(x=15, y=310)

# Categoria:
pok_categoria = Label(janela, text='Categoria: Lagarto', relief='flat', anchor="center", font=('Verdana 10'), bg=cor1, fg=cor4)
pok_categoria.place(x=15, y=360)

# Altura:
pok_altura = Label(janela, text='Altura: 2.00', relief='flat', anchor="center", font=('Verdana 10'), bg=cor1, fg=cor4)
pok_altura.place(x=15, y=385)

# Peso:
pok_peso = Label(janela, text='Peso: 18.7', relief='flat', anchor="center", font=('Verdana 10'), bg=cor1, fg=cor4)
pok_peso.place(x=15, y=410)

# Habilidade:
pok_habilidade = Label(janela, text='Habilidade: Chamas', relief='flat', anchor="center", font=('Verdana 10'), bg=cor1, fg=cor4)
pok_habilidade.place(x=15, y=435)

# Ataques e fraquezas
pok_ataques_titulo = Label(janela, text='Principais Ataques e Fraquezas', relief='flat', anchor="center", font=('Verdana 16'), bg=cor1, fg=cor4)
pok_ataques_titulo.place(x=180, y=310)

# Principais ataques:
pok_ataques = Label(janela, text='Ataques: Brasas, Arranhão e Ira do Dragão', relief='flat', anchor="center", font=('Verdana 10'), bg=cor1, fg=cor4)
pok_ataques.place(x=195, y=360)

# Fraquezas:
pok_fraquezas = Label(janela, text='Fraquezas: Água, Rocha e Terra', relief='flat', anchor="center", font=('Verdana 10'), bg=cor1, fg=cor4)
pok_fraquezas.place(x=195, y=410)


# Botões - 1 - Charmander:
Image_bt1 = Image.open('Imagens/Charmander02.png')
Image_bt1 = Image_bt1.resize((40, 40))
Image_bt1 = ImageTk.PhotoImage(Image_bt1)

bt_pok_image1 = Button(janela, command=lambda:trocar_pokemon('Charmander'), image=Image_bt1, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
bt_pok_image1.place(x=375, y=10)

# Botões - 2 - Vulpix:
Image_bt2 = Image.open('Imagens/Vulpix02.png')
Image_bt2 = Image_bt2.resize((40, 40))
Image_bt2 = ImageTk.PhotoImage(Image_bt2)

bt_pok_image2 = Button(janela, command=lambda:trocar_pokemon('Vulpix'), image=Image_bt2, text='Vulpix', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
bt_pok_image2.place(x=375, y=65)

# Botões - 3 - Growlithe:
Image_bt3 = Image.open('Imagens/Growlithe02.png')
Image_bt3 = Image_bt3.resize((40, 40))
Image_bt3 = ImageTk.PhotoImage(Image_bt3)

bt_pok_image3 = Button(janela, command=lambda:trocar_pokemon('Growlithe'), image=Image_bt3, text='Growlithe', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
bt_pok_image3.place(x=375, y=120)

# Botões - 4 - Cyndaquil:
Image_bt4 = Image.open('Imagens/Cyndaquil02.png')
Image_bt4 = Image_bt4.resize((40, 40))
Image_bt4 = ImageTk.PhotoImage(Image_bt4)

bt_pok_image4 = Button(janela, command=lambda:trocar_pokemon('Cyndaquil'), image=Image_bt4, text='Cyndaquil', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
bt_pok_image4.place(x=375, y=175)

# Botões - 5 - Magby:
Image_bt5 = Image.open('Imagens/Magby02.png')
Image_bt5 = Image_bt5.resize((40, 40))
Image_bt5 = ImageTk.PhotoImage(Image_bt5)

bt_pok_image5 = Button(janela, command=lambda:trocar_pokemon('Magby'), image=Image_bt5, text='Magby', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
bt_pok_image5.place(x=375, y=230)

import random
pok_lista = ['Charmander', 'Vulpix', 'Growlithe', 'Cyndaquil', 'Magby']

pok_escolhido = random.sample(pok_lista, 1)

trocar_pokemon(pok_escolhido[0])


janela.mainloop()
