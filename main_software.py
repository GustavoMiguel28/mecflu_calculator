from tkinter import *
from time import sleep

from Funcionalidades.massa_especifica import *
from Funcionalidades.volume_especifico import *
from Funcionalidades.peso_especifico import *
from Funcionalidades.densidade_relativa import *
from Funcionalidades.vazao import *
from Funcionalidades.pressao import *
from Funcionalidades.pressao_hidrostatica import *

def gui_iniciar():
    janela_iniciar = Tk()
    janela_iniciar.title('MecFlu Calculator')
    janela_iniciar.geometry('600x480+610+153')
    janela_iniciar.maxsize(600, 480)
    janela_iniciar.minsize(600, 480)
    
    #Trazendo imagens
    img_botao_iniciar = PhotoImage(file='Funcionalidades\\imagens\\botao_iniciar.png')
    img_fundo_iniciar = PhotoImage(file='Funcionalidades\\imagens\\iniciar_fundo.png')

    #Criando fundo
    label_fundo_main = Label(janela_iniciar, image=img_fundo_iniciar)
    label_fundo_main.pack()

    #Criando botão iniciar
    botao_iniciar = Button(janela_iniciar, bd=0, image=img_botao_iniciar, command=gui_main)
    botao_iniciar.place(width=160, height=45, x=228, y=302)

    janela_iniciar.mainloop()


def gui_main():

    #Criando janela
    sleep(0.1)
    janela_main = Toplevel()
    janela_main.title('MecFlu Calculator')
    janela_main.geometry('600x480+610+153')
    janela_main.maxsize(600, 480)
    janela_main.minsize(600, 480)

    #Trazendo imagens
    img_fundo_main = PhotoImage(file='Funcionalidades\\imagens\\Main_fundo.png')
    img_botao_massaespecifica = PhotoImage(file='Funcionalidades\\imagens\\botao_MassaEspecifica.png')
    img_botao_volumeespecifico = PhotoImage(file='Funcionalidades\\imagens\\botao_VolumeEspecifico.png')
    img_botao_pesoespecifico = PhotoImage(file='Funcionalidades\\imagens\\botao_PesoEspecifico.png')
    img_botao_densidaderelativa = PhotoImage(file='Funcionalidades\\imagens\\botao_DensidadeRelativa.png')
    img_botao_vazao = PhotoImage(file='Funcionalidades\\imagens\\botao_Vazao.png')
    img_botao_voltar = PhotoImage(file='Funcionalidades\\imagens\\botao_voltar.png')

    #Criando fundo
    label_fundo_main = Label(janela_main, image=img_fundo_main)
    label_fundo_main.pack()

    #Criando botão para chamar as calculadoras
    botao_massaespecifica = Button(janela_main, bd=0, image=img_botao_massaespecifica, command=gui_massa_especifica)
    botao_massaespecifica.place(width=251, height=41, x=28, y=155)

    botao_volumeespecifico = Button(janela_main, bd=0, image=img_botao_volumeespecifico, command=gui_volume_especifico)
    botao_volumeespecifico.place(width=251, height=41, x=28, y=215)

    botao_pesoespecifico = Button(janela_main, bd=0, image=img_botao_pesoespecifico, command=gui_peso_especifico)
    botao_pesoespecifico.place(width=251, height=41, x=28, y=275)

    botao_densidaderelativa = Button(janela_main, bd=0, image=img_botao_densidaderelativa, command=gui_densidade_relativa)
    botao_densidaderelativa.place(width=251, height=41, x=28, y=335)

    botao_vazao = Button(janela_main, bd=0, image=img_botao_vazao, command=gui_vazao)
    botao_vazao.place(width=251, height=41, x=28, y=395)

    #Criando botão para retornar para a tela inicial
    botao_voltar = Button(janela_main, bd=0, image=img_botao_voltar, command=janela_main.destroy)
    botao_voltar.place(width=62, height=47, x=9, y=14)

    janela_main.mainloop()


if __name__ == "__main__":
    gui_iniciar()