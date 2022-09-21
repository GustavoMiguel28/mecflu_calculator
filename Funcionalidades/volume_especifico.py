from tkinter import *
from time import sleep

def calcular_volume_especifico():
    """
    Função para calcular o volume específico
    """
    
    #Pegando dados passados pelo usuário
    volume_valor = float(en_volume.get().replace(',', '.'))
    volume_unidade = str(vvolume.get())

    massa_valor = float(en_massa.get().replace(',', '.'))
    massa_unidade = str(vmassa.get())

    #Dicionarios de conversão de unidades
    conversão_unidades_volume = {'cm3': 1000000, 'm3': 1, 'km3': 0.000000001}
    conversão_unidades_massa = {'g': 1000, 'kg': 1, 't': 0.001}

    #Aplicando formula
    volume_especifico = round((volume_valor / conversão_unidades_volume[volume_unidade]) / (massa_valor / conversão_unidades_massa[massa_unidade]), 4)

    #Alterando campo de resposta
    volume_especifico = str(volume_especifico).replace('.', ',')
    sa_volume_especifico['text'] = f'{volume_especifico} m3/kg'


def gui_volume_especifico():
    """
    Função que cria tela de interação para o calculo do volume específico
    """

    #Criando janela
    sleep(0.1)
    janela = Toplevel()
    janela.title('Volume Específico')
    janela.geometry('600x480+610+153')
    janela.maxsize(600, 480)
    janela.minsize(600, 480)

    #Trazendo imagens
    img_fundo = PhotoImage(file='Funcionalidades\\imagens\\VolumeEspecifico_fundo.png')
    img_botao_calcular = PhotoImage(file='Funcionalidades\\imagens\\botao_calcular.png')
    img_botao_voltar = PhotoImage(file='Funcionalidades\\imagens\\botao_voltar.png')

    #Criando fundo
    label_fundo = Label(janela, image=img_fundo)
    label_fundo.pack()

    #Criando campos de entrada de dados
    global en_volume
    en_volume = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_volume.place(width=102, height=39, x=361, y=167)

    global en_massa
    en_massa = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_massa.place(width=102, height=39, x=361, y=245)

    #Criando menu de unidades de medidas 
    unidades_volume = ['cm3', 'm3', 'km3']
    global vvolume
    vvolume = StringVar()
    vvolume.set(unidades_volume[1])
    opcoes_volume = OptionMenu(janela, vvolume, *unidades_volume)
    opcoes_volume.place(width=62, height=39, x=465, y=167)

    unidades_massa = ['g', 'kg', 't']
    global vmassa
    vmassa = StringVar()
    vmassa.set(unidades_massa[1])
    opcoes_massa = OptionMenu(janela, vmassa, *unidades_massa)
    opcoes_massa.place(width=62, height=39, x=465, y=245)

    #Criando campo de resposta
    global sa_volume_especifico
    sa_volume_especifico = Label(janela, text='-', bd=2, font=('Century Gothic', 12), justify=CENTER)
    sa_volume_especifico.place(width=164, height=39,x=361, y=332)

    #Criando botão para chamar a função de calcular
    botao_calcular = Button(janela, bd=0, image=img_botao_calcular, command=calcular_volume_especifico)
    botao_calcular.place(width=126, height=39, x=386, y=380)

    #Criando botão para retornar para a tela principal
    botao_voltar = Button(janela, bd=0, image=img_botao_voltar, command=janela.destroy)
    botao_voltar.place(width=62, height=47, x=9, y=14)

    janela.mainloop()