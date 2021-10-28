import tkinter as tk
from tkinter.ttk import *
from typing import Text

class Ventana():

    #Cuerpo de la ventana
    def __init__(self):
        #Configuracion de la ventana
        self.ventana1 = tk.Tk()
        self.ventana1.title('Calculadora de Crafteo')
        #self.ventana1.config(bg="dark turquoise")
        self.ventana1.iconbitmap('D:\Python\Craft2\Test\Interfaz test\icons.ico')

        #Frame 1 y su contenido
        self.lf1 = LabelFrame(self.ventana1, text = 'Seleccion de Materiales')
        self.lf1.grid(column=0, row=0, padx=5, pady=10)
        self.Material()

        #Frame 2 y su contenido
        self.lf2 = LabelFrame(self.ventana1, text = 'Primeros datos')
        self.lf2.grid(column=0, row=1, padx=5, pady=10)
        self.Ppasos()

        #loop de la ventana
        self.ventana1.mainloop()

    #Contenido del primer LabelFrame
    def Material(self):

        self.LbTipoMaterial = Label(self.lf1, text = 'Material a Usar:')
        self.LbTipoMaterial.grid(column=0, row=0, padx=4, pady=4)
        self.CboMaterial = Combobox(self.lf1, state='readonly', values = ["Mineral", "Tela", "Cuero"])
        self.CboMaterial.grid(column=1, row=0, padx=4, pady=4)

        self.LbTier = Label(self.lf1, text = 'Tier a Craftear:')
        self.LbTier.grid(column=0, row=1, padx=4, pady=4)
        self.CboTier = Combobox(self.lf1, state='readonly', values = ['Tier 4', 'Tier 5', 'Tier 6', 'Tier 7', 'Tier 8'])
        self.CboTier.grid(column=1, row=1, padx=4, pady=4)

        self.LbEncantamiento = Label(self.lf1, text = 'Nivel de Encantamiento:')
        self.LbEncantamiento.grid(column=0, row=2, padx=4, pady=4)
        self.CboNivelEncantamiento = Combobox(self.lf1, state='readonly', values = [ 'Punto 0', 'Punto 1', 'Punto 2', 'Punto 3'])
        self.CboNivelEncantamiento.grid(column=1, row=2, padx=4, pady=4)

    #Contenido del segundo LabelFrame
    def Ppasos(self):
        self.LbGastoFoco = Label(self.lf2, text = 'Valor de Foco:')
        self.LbGastoFoco.grid(column=0, row=1, padx=4, pady=4)
        self.EgastoFoco = Entry(self.lf2)
        self.EgastoFoco.grid(column=1, row=1, pady=4)





ventana1= Ventana()
