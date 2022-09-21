from tkinter import *
from time import sleep

def calcular_massa_especifica():
    """
    Função para calcular a massa específica
    """
    
    #Pegando dados passados pelo usuário
    massa_valor = float(en_massa.get().replace(',', '.'))
    massa_unidade = str(vmassa.get())

    volume_valor = float(en_volume.get().replace(',', '.'))
    volume_unidade = str(vvolume.get())

    #Dicionarios de conversão de unidades
    conversão_unidades_massa = {'g': 1000, 'kg': 1, 't': 0.001}
    conversão_unidades_volume = {'cm3': 1000000, 'm3': 1, 'km3': 0.000000001}

    #Aplicando formula
    massa_especifica = round((massa_valor / conversão_unidades_massa[massa_unidade]) / (volume_valor / conversão_unidades_volume[volume_unidade]), 4)

    #Alterando campo de resposta
    massa_especifica = str(massa_especifica).replace('.', ',')
    sa_massa_especifica['text'] = f'{massa_especifica} kg/m3'


def gui_massa_especifica():
    """
    Função que cria tela de interação para o calculo da massa específica
    """

    #Criando janela
    sleep(0.1)
    janela = Toplevel()
    janela.title('Massa Específica')
    janela.geometry('600x480+610+153')
    janela.maxsize(600, 480)
    janela.minsize(600, 480)

    #Trazendo imagens
    img_fundo = PhotoImage(file='Funcionalidades\\imagens\\MassaEspecifica_fundo.png')
    img_botao_calcular = PhotoImage(file='Funcionalidades\\imagens\\botao_calcular.png')
    img_botao_voltar = PhotoImage(file='Funcionalidades\\imagens\\botao_voltar.png')

    #Criando fundo
    label_fundo = Label(janela, image=img_fundo)
    label_fundo.pack()

    #Criando campos de entrada de dados
    global en_massa
    en_massa = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_massa.place(width=102, height=39, x=361, y=167)

    global en_volume
    en_volume = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_volume.place(width=102, height=39, x=361, y=245)

    #Criando menu de unidades de medidas 
    unidades_massa = ['g', 'kg', 't']
    global vmassa
    vmassa = StringVar()
    vmassa.set(unidades_massa[1])
    opcoes_massa = OptionMenu(janela, vmassa, *unidades_massa)
    opcoes_massa.place(width=62, height=39, x=465, y=167)

    unidades_volume = ['cm3', 'm3', 'km3']
    global vvolume
    vvolume = StringVar()
    vvolume.set(unidades_volume[1])
    opcoes_volume = OptionMenu(janela, vvolume, *unidades_volume)
    opcoes_volume.place(width=62, height=39, x=465, y=245)

    #Criando campo de resposta
    global sa_massa_especifica
    sa_massa_especifica = Label(janela, text='-', bd=2, font=('Century Gothic', 12), justify=CENTER)
    sa_massa_especifica.place(width=164, height=39,x=361, y=332)

    #Criando botão para chamar a função de calcular
    botao_calcular = Button(janela, bd=0, image=img_botao_calcular, command=calcular_massa_especifica)
    botao_calcular.place(width=126, height=39, x=386, y=380)

    #Criando botão para retornar para a tela principal
    botao_voltar = Button(janela, bd=0, image=img_botao_voltar, command=janela.destroy)
    botao_voltar.place(width=62, height=47, x=9, y=14)

    janela.mainloop()