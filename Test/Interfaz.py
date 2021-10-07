
from tkinter import ttk
from tkinter import *
from typing import ValuesView

def sel():
    seleccion= str(op.get())



class produc:
    def __init__(self,window):
        self.wind = window
        self.wind.title('Calculador Crafteo')
        op =IntVar()
        #Cuadrado para meter elementos
        frame = LabelFrame(self.wind, text='Iniciemos a calcular')
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        #Labels 
        Label(frame, text='Precio de foco x Unidad:').grid(row=1,column=0)
        self.FocoxUnidad= Entry(frame)
        self.FocoxUnidad.grid(row=1, column=1)
        #Combobox
        Label(frame, text="Tier a Craftear:").grid(row=2, column=0)
        combo = ttk.Combobox(frame, state='readonly')
        combo.grid(row=2,column=1)
        combo['values'] = ('Tier 4', 'Tier 5', 'Tier 6', 'Tier 7', 'Tier 8')
        combo.current(0)
        #Checkbox
        Label(frame, text='El Material es encantado:').grid(row=3,column=0)
        check= Radiobutton(frame, text='Si', variable=op, value=1, command=sel).grid(row=3,column=1)
        check= Radiobutton(frame, text='No', variable=op, value=2, command=sel).grid(row=3,column=2)
        """
        self.combo = ttk.Combobox(self, state='readonly')
        Label(frame, text='Tier a Craftear:').grid(row=2,column=1)
        self.combo.grid(row=3,column=1)
        self.combo["values"]=['Tier 4', 'Tier 5', 'Tier 6', 'Tier 7', 'Tier 8']
        """


if __name__ == '__main__':
    window= Tk()
    produc(window)
    window.mainloop()