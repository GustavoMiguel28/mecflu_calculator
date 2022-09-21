from tkinter import *
from time import sleep

def calcular_vazao():
    """
    Função para calcular a vazão
    """

    #Pegando dados passados pelo usuário
    vazao_valor = float(en_vazao.get().replace(',', '.'))
    tipo_vazao = str(vvazao.get())

    tempo_valor = float(en_tempo.get().replace(',', '.'))
    tempo_unidade = str(vtempo.get())

    #Dicionarios de conversão de unidades
    conversão_unidades_tempo = {'s': 1, 'min': 0.016666666667}

    #Aplicando formula
    vazao = round(vazao_valor / round((tempo_valor / conversão_unidades_tempo[tempo_unidade]),0), 4)

    #Alterando campo de resposta
    vazao = str(vazao).replace('.', ',')

    if tipo_vazao == 'm3':
        sa_vazao['text'] = f'{vazao} m3/s'
    
    elif tipo_vazao == 'kg':
        sa_vazao['text'] = f'{vazao} kg/s'

    else:
        sa_vazao['text'] = f'{vazao} N/s'


def gui_vazao():
    """
    Função que cria tela de interação para o calculo da vazao do fluido
    """

    #Criando janela
    sleep(0.1)
    janela = Toplevel()
    janela.title('Vazão do fluido')
    janela.geometry('600x480+610+153')
    janela.maxsize(600, 480)
    janela.minsize(600, 480)

    #Trazendo imagens
    img_fundo = PhotoImage(file='Funcionalidades\\imagens\\Vazao_fundo.png')
    img_botao_calcular = PhotoImage(file='Funcionalidades\\imagens\\botao_calcular.png')
    img_botao_voltar = PhotoImage(file='Funcionalidades\\imagens\\botao_voltar.png')

    #Criando fundo
    label_fundo = Label(janela, image=img_fundo)
    label_fundo.pack()

    #Criando campos de entrada de dados
    global en_vazao
    en_vazao = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_vazao.place(width=102, height=39, x=361, y=167)

    global en_tempo
    en_tempo = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_tempo.place(width=102, height=39, x=361, y=245)

    #Criando menu de unidades de medidas 
    tipos_vazao = ['m3', 'kg', 'N']
    global vvazao
    vvazao = StringVar()
    vvazao.set(tipos_vazao[0])
    opcoes_peso = OptionMenu(janela, vvazao, *tipos_vazao)
    opcoes_peso.place(width=62, height=39, x=465, y=167)

    unidades_tempo = ['s', 'min']
    global vtempo
    vtempo = StringVar()
    vtempo.set(unidades_tempo[0])
    opcoes_tempo = OptionMenu(janela, vtempo, *unidades_tempo)
    opcoes_tempo.place(width=62, height=39, x=465, y=245)

    #Criando campo de resposta
    global sa_vazao
    sa_vazao = Label(janela, text='-', bd=2, font=('Century Gothic', 12), justify=CENTER)
    sa_vazao.place(width=164, height=39,x=361, y=332)

    #Criando botão para chamar a função de calcular
    botao_calcular = Button(janela, bd=0, image=img_botao_calcular, command=calcular_vazao)
    botao_calcular.place(width=126, height=39, x=386, y=380)

    #Criando botão para retornar para a tela principal
    botao_voltar = Button(janela, bd=0, image=img_botao_voltar, command=janela.destroy)
    botao_voltar.place(width=62, height=47, x=9, y=14)

    janela.mainloop()