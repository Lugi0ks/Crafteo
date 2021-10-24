
from tkinter import ttk
from tkinter import *
from typing import ValuesView


class produc:
    def __init__(self,window):
        self.wind = window
        self.wind.title('Calculadora de Crafteo')
        op =IntVar()
        #Cuadrado para meter elementos
        frame = LabelFrame(self.wind, text='Iniciemos a calcular')
        frame.grid(row=0, column=0, columnspan=3, pady=6)
        #Titulos 
        Label(frame, text='Precio de foco x Unidad:').grid(pady=3, row=1, column=0, sticky=W)
        Label(frame, text="Tier a Craftear:").grid(pady=3 ,row=2, column=0, sticky=W)
        Label(frame, text="Nivel de encantamiento del paterial:").grid(pady=3 ,row=3, column=0, sticky=W)
        #Valores    
        # 
        # Precio del Foco    
        self.FocoxUnidad= Entry(frame)
        self.FocoxUnidad.grid(padx=5 ,row=1, column=1, sticky=W)
        #
        #Tier a Craftear
        cboTier = ttk.Combobox(frame, state='readonly', values =['Tier 4', 'Tier 5', 'Tier 6', 'Tier 7', 'Tier 8'])
        cboTier.grid(padx=5 ,row=2, column=1, sticky=W)
        #
        #Punto del material
        cboEncatamiento = ttk.Combobox(frame,state='readonly', values=[ 'Punto 0', 'Punto 1', 'Punto 2', 'Punto 3'])
        cboEncatamiento.grid(padx=5, row=3, column=1)
        """
        self.combo = ttk.Combobox(self, state='readonly')
        Label(frame, text='Tier a Craftear:').grid(row=2,column=1)
        self.combo.grid(row=3,column=1)
        self.combo["values"]=['Tier 4', 'Tier 5', 'Tier 6', 'Tier 7', 'Tier 8']
        """
        #Introduccion de los datos importantes
        frame2 = LabelFrame(self.wind, text='Introduce los valores')
        frame2.grid(row=1, column=0 ,columnspan=3 ,pady=20, sticky=NW)
        #labels de precios
        Label(frame2, text='Precio del Material: ').grid(pady=5 ,row=1, column=0)
        self.PrecioMaterial= Entry(frame2)
        self.PrecioMaterial.grid(pady=5 ,row=1, column=1)

        

if __name__ == '__main__':
    window= Tk()
    produc(window)
    window.mainloop()