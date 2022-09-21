from tkinter import *
from time import sleep

def calcular_pressao_hidrostatica():
    """
    Função para calcular a pressao hidrostatica
    """
    
    #Pegando dados passados pelo usuário
    densidade_valor = float(en_densidade.get().replace(',', '.'))
    densidade_unidade = str(vdensidade.get())

    fgravitacional_valor = float(en_fgravitacional.get().replace(',', '.'))
    fgravitacional_unidade = str(vfgravitacional.get())

    altura_valor = float(en_altura.get().replace(',', '.'))
    altura_unidade = str(valtura.get())

    #Dicionarios de conversão de unidades
    conversão_unidades_densidade = {'g/cm3': 1000, 'kg/m3': 1}
    conversão_unidades_fgravitacional = {'m/s2': 1}
    conversão_unidades_altura = {'cm': 100, 'm': 1, 'km': 0.001}

    #Aplicando formula
    pressao_hidrostatica = round((densidade_valor / conversão_unidades_densidade[densidade_unidade]) * (fgravitacional_valor / conversão_unidades_fgravitacional[fgravitacional_unidade]) * (altura_valor / conversão_unidades_altura[altura_unidade]), 4)

    #Alterando campo de resposta
    pressao_hidrostatica = str(pressao_hidrostatica).replace('.', ',')
    sa_pressao_hidrostatica['text'] = f'{pressao_hidrostatica} Pa'


def gui_pressao_hidrostatica():
    """
    Função que cria tela de interação para o calculo da pressao_hidrostatica
    """

    #Criando janela
    sleep(0.1)
    janela = Toplevel()
    janela.title('Pressão Hidrostática')
    janela.geometry('600x480+610+153')
    janela.maxsize(600, 480)
    janela.minsize(600, 480)

    #Trazendo imagens
    img_fundo = PhotoImage(file='Funcionalidades\\imagens\\Pressao_Hidrostatica_fundo.png')
    img_botao_calcular = PhotoImage(file='Funcionalidades\\imagens\\botao_calcular.png')
    img_botao_voltar = PhotoImage(file='Funcionalidades\\imagens\\botao_voltar.png')

    #Criando fundo
    label_fundo = Label(janela, image=img_fundo)
    label_fundo.pack()

    #Criando campos de entrada de dados
    global en_densidade
    en_densidade = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_densidade.place(width=82, height=27, x=361, y=163)

    global en_fgravitacional
    en_fgravitacional = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_fgravitacional.place(width=82, height=27, x=361, y=216)

    global en_altura
    en_altura = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_altura.place(width=82, height=27, x=361, y=269)

    #Criando menu de unidades de medidas 
    unidades_densidade = ['g/cm3', 'kg/m3']
    global vdensidade
    vdensidade = StringVar()
    vdensidade.set(unidades_densidade[1])
    opcoes_densidade = OptionMenu(janela, vdensidade, *unidades_densidade)
    opcoes_densidade.place(width=82, height=27, x=445, y=163)

    unidades_fgravitacional = ['m/s2']
    global vfgravitacional
    vfgravitacional = StringVar()
    vfgravitacional.set(unidades_fgravitacional[0])
    opcoes_fgravitacional = OptionMenu(janela, vfgravitacional, *unidades_fgravitacional)
    opcoes_fgravitacional.place(width=82, height=27, x=445, y=216)

    unidades_altura = ['cm', 'm', 'km']
    global valtura
    valtura = StringVar()
    valtura.set(unidades_altura[1])
    opcoes_altura = OptionMenu(janela, valtura, *unidades_altura)
    opcoes_altura.place(width=82, height=27, x=445, y=269)

    #Criando campo de resposta
    global sa_pressao_hidrostatica
    sa_pressao_hidrostatica = Label(janela, text='-', bd=2, font=('Century Gothic', 12), justify=CENTER)
    sa_pressao_hidrostatica.place(width=164, height=39,x=361, y=332)

    #Criando botão para chamar a função de calcular
    botao_calcular = Button(janela, bd=0, image=img_botao_calcular, command=calcular_pressao_hidrostatica)
    botao_calcular.place(width=126, height=39, x=386, y=380)

    #Criando botão para retornar para a tela principal
    botao_voltar = Button(janela, bd=0, image=img_botao_voltar, command=janela.destroy)
    botao_voltar.place(width=62, height=47, x=9, y=14)

    janela.mainloop()