from tkinter import *
from time import sleep

def calcular_pressao():
    """
    Função para calcular a pressao
    """
    
    #Pegando dados passados pelo usuário
    forca_valor = float(en_forca.get().replace(',', '.'))
    forca_unidade = str(vforca.get())

    area_valor = float(en_area.get().replace(',', '.'))
    area_unidade = str(varea.get())

    #Dicionarios de conversão de unidades
    conversão_unidades_forca = {'kgf': 10, 'N': 1, 'dyn': 0.00001}
    conversão_unidades_area = {'cm2': 10000, 'm2': 1, 'km2': 0.000001}

    #Aplicando formula
    pressao = round((forca_valor / conversão_unidades_forca[forca_unidade]) / (area_valor / conversão_unidades_area[area_unidade]), 4)

    #Alterando campo de resposta
    pressao = str(pressao).replace('.', ',')
    sa_pressao['text'] = f'{pressao} Pa'


def gui_pressao():
    """
    Função que cria tela de interação para o calculo da pressao
    """

    #Criando janela
    sleep(0.1)
    janela = Toplevel()
    janela.title('Pressão')
    janela.geometry('600x480+610+153')
    janela.maxsize(600, 480)
    janela.minsize(600, 480)

    #Trazendo imagens
    img_fundo = PhotoImage(file='Funcionalidades\\imagens\\Pressao_fundo.png')
    img_botao_calcular = PhotoImage(file='Funcionalidades\\imagens\\botao_calcular.png')
    img_botao_voltar = PhotoImage(file='Funcionalidades\\imagens\\botao_voltar.png')

    #Criando fundo
    label_fundo = Label(janela, image=img_fundo)
    label_fundo.pack()

    #Criando campos de entrada de dados
    global en_forca
    en_forca = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_forca.place(width=102, height=39, x=361, y=167)

    global en_area
    en_area = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_area.place(width=102, height=39, x=361, y=245)

    #Criando menu de unidades de medidas 
    unidades_forca = ['kgf', 'N', 'dyn']
    global vforca
    vforca = StringVar()
    vforca.set(unidades_forca[1])
    opcoes_forca = OptionMenu(janela, vforca, *unidades_forca)
    opcoes_forca.place(width=62, height=39, x=465, y=167)

    unidades_area = ['cm2', 'm2', 'km2']
    global varea
    varea = StringVar()
    varea.set(unidades_area[1])
    opcoes_area = OptionMenu(janela, varea, *unidades_area)
    opcoes_area.place(width=62, height=39, x=465, y=245)

    #Criando campo de resposta
    global sa_pressao
    sa_pressao = Label(janela, text='-', bd=2, font=('Century Gothic', 12), justify=CENTER)
    sa_pressao.place(width=164, height=39,x=361, y=332)

    #Criando botão para chamar a função de calcular
    botao_calcular = Button(janela, bd=0, image=img_botao_calcular, command=calcular_pressao)
    botao_calcular.place(width=126, height=39, x=386, y=380)

    #Criando botão para retornar para a tela principal
    botao_voltar = Button(janela, bd=0, image=img_botao_voltar, command=janela.destroy)
    botao_voltar.place(width=62, height=47, x=9, y=14)

    janela.mainloop()