from tkinter import *
from time import sleep

def calcular_viscosidade_cinematica():
    """
    Função para calcular a viscosidade cinematica
    """
    
    #Pegando dados passados pelo usuário
    viscosidade_dinamica_valor = float(en_viscosidade_dinamica.get().replace(',', '.'))
    viscosidade_dinamica_unidade = str(vviscosidade_dinamica.get())

    massa_especifica_valor = float(en_massa_especifica.get().replace(',', '.'))
    massa_especifica_unidade = str(vmassa_especifica.get())

    #Dicionarios de conversão de unidades
    conversão_unidades_viscosidade_dinamica = {'Pa.s': 1}
    conversão_unidades_massa_especifica = {'kg/m3': 1}

    #Aplicando formula
    viscosidade_cinematica = round((viscosidade_dinamica_valor / conversão_unidades_viscosidade_dinamica[viscosidade_dinamica_unidade]) / (massa_especifica_valor / conversão_unidades_massa_especifica[massa_especifica_unidade]), 4)

    #Alterando campo de resposta
    viscosidade_cinematica = str(viscosidade_cinematica).replace('.', ',')
    sa_viscosidade_cinematica['text'] = f'{viscosidade_cinematica} m2/s'


def gui_viscosidade_cinematica():
    """
    Função que cria tela de interação para o calculo da viscosidade cinematica
    """

    #Criando janela
    sleep(0.1)
    janela = Toplevel()
    janela.title('Viscosidade Cinemática')
    janela.geometry('600x480+610+153')
    janela.maxsize(600, 480)
    janela.minsize(600, 480)

    #Trazendo imagens
    img_fundo = PhotoImage(file='Funcionalidades\\imagens\\ViscosidadeCinematica_fundo.png')
    img_botao_calcular = PhotoImage(file='Funcionalidades\\imagens\\botao_calcular.png')
    img_botao_voltar = PhotoImage(file='Funcionalidades\\imagens\\botao_voltar.png')

    #Criando fundo
    label_fundo = Label(janela, image=img_fundo)
    label_fundo.pack()

    #Criando campos de entrada de dados
    global en_viscosidade_dinamica
    en_viscosidade_dinamica = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_viscosidade_dinamica.place(width=82, height=39, x=361, y=167)

    global en_massa_especifica
    en_massa_especifica = Entry(janela, bd=2, font=('Century Gothic', 12), justify=CENTER)
    en_massa_especifica.place(width=82, height=39, x=361, y=245)

    #Criando menu de unidades de medidas 
    unidades_viscosidade_dinamica = ['Pa.s']
    global vviscosidade_dinamica
    vviscosidade_dinamica = StringVar()
    vviscosidade_dinamica.set(unidades_viscosidade_dinamica[0])
    opcoes_viscosidade_dinamica= OptionMenu(janela, vviscosidade_dinamica, *unidades_viscosidade_dinamica)
    opcoes_viscosidade_dinamica.place(width=82, height=39, x=445, y=167)

    unidades_massa_especifica = ['kg/m3']
    global vmassa_especifica
    vmassa_especifica = StringVar()
    vmassa_especifica.set(unidades_massa_especifica[0])
    opcoes_massa_especifica = OptionMenu(janela, vmassa_especifica, *unidades_massa_especifica)
    opcoes_massa_especifica.place(width=82, height=39, x=445, y=245)

    #Criando campo de resposta
    global sa_viscosidade_cinematica
    sa_viscosidade_cinematica = Label(janela, text='-', bd=2, font=('Century Gothic', 12), justify=CENTER)
    sa_viscosidade_cinematica.place(width=164, height=39,x=361, y=332)

    #Criando botão para chamar a função de calcular
    botao_calcular = Button(janela, bd=0, image=img_botao_calcular, command=calcular_viscosidade_cinematica)
    botao_calcular.place(width=126, height=39, x=386, y=380)

    #Criando botão para retornar para a tela principal
    botao_voltar = Button(janela, bd=0, image=img_botao_voltar, command=janela.destroy)
    botao_voltar.place(width=62, height=47, x=9, y=14)

    janela.mainloop()