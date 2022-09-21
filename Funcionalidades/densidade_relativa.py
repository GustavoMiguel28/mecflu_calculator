from tkinter import *
from time import sleep

def calcular_densidade_relativa():
    """
    Função para calcular a densidade relativa
    """

    #Pegando dados passados pelo usuário
    densidade_valor = float(en_densidade.get().replace(',', '.'))
    densidade_unidade = str(vdensidade.get())

    #Dicionarios de conversão de unidades
    conversão_unidades_densidade = {'g/cm3': 1000, 'kg/m3': 1}

    #Valores da densidade a ser comparada
    densidade_comparativa = int(vdensidade_comp.get())

    #Aplicando a formula
    densidade_relativa = round((densidade_valor / conversão_unidades_densidade[densidade_unidade]) / densidade_comparativa, 4)

    #Alterando campo de resposta
    densidade_relativa = str(densidade_relativa).replace('.', ',')
    sa_densidade_relativa['text'] = f'{densidade_relativa}'


def gui_densidade_relativa():
    """
    Função que cria tela de interação para o calculo da massa específica
    """

    #Criando janela
    sleep(0.1)
    janela = Toplevel()
    janela.title('Densidade Relativa')
    janela.geometry('600x480+610+153')
    janela.maxsize(600, 480)
    janela.minsize(600, 480)

    #Trazendo imagens
    img_fundo = PhotoImage(file='Funcionalidades\\imagens\\DensidadeRelativa_fundo.png')
    img_botao_calcular = PhotoImage(file='Funcionalidades\\imagens\\botao_calcular.png')
    img_botao_voltar = PhotoImage(file='Funcionalidades\\imagens\\botao_voltar.png')

    #Criando fundo
    label_fundo = Label(janela, image=img_fundo)
    label_fundo.pack()

    #Criando campos de entrada de dados
    global en_densidade
    en_densidade = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_densidade.place(width=82, height=39, x=361, y=167)

    #Criando menu de unidades de medidas 
    unidades_densidade = ['g/cm3', 'kg/m3']
    global vdensidade
    vdensidade = StringVar()
    vdensidade.set(unidades_densidade[1])
    opcoes_densidade = OptionMenu(janela, vdensidade, *unidades_densidade)
    opcoes_densidade.place(width=82, height=39, x=445, y=167)

    #Criando opções de seleção para a densidade comparativa
    global vdensidade_comp
    vdensidade_comp = StringVar()
    vdensidade_comp.set(1)
    rd_densidade_agua = Radiobutton(janela, text='água', value=1000, variable=vdensidade_comp, justify=LEFT)
    rd_densidade_agua.place(width=70, x=364, y=245)

    rd_densidade_alcool = Radiobutton(janela, text='álcool', value=790, variable=vdensidade_comp, justify=LEFT)
    rd_densidade_alcool.place(width=70,x=454, y=245)

    rd_densidade_oleo = Radiobutton(janela, text='óleo', value=852, variable=vdensidade_comp, justify=LEFT)
    rd_densidade_oleo.place(width=70,x=364, y=275)

    rd_densidade_glicerina = Radiobutton(janela, text='glicerina', value=1250, variable=vdensidade_comp, justify=LEFT)
    rd_densidade_glicerina.place(width=70,x=454, y=275)

    #Criando campo de resposta
    global sa_densidade_relativa
    sa_densidade_relativa = Label(janela, text='-', bd=2, font=('Century Gothic', 12), justify=CENTER)
    sa_densidade_relativa.place(width=164, height=39,x=361, y=332)

    #Criando botão para chamar a função de calcular
    botao_calcular = Button(janela, bd=0, image=img_botao_calcular, command=calcular_densidade_relativa)
    botao_calcular.place(width=126, height=39, x=386, y=380)

    #Criando botão para retornar para a tela principal
    botao_voltar = Button(janela, bd=0, image=img_botao_voltar, command=janela.destroy)
    botao_voltar.place(width=62, height=47, x=9, y=14)

    janela.mainloop()