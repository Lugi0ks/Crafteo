from tkinter import ttk, messagebox
from tkinter import *
from typing import ValuesView
    
def segundopaso():
    messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")



class Inicio():
    def __init__(self,Ventana):
        #Titulo de la ventana
        self.win = Ventana
        self.win.title('Calculador Crafteo')
        
        #Titulo del las opciones
        frame = LabelFrame(self.win, text='Seleccion')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        #Leabels

        #Tipo de Material
        Label(frame,text='¿Que tipo de material usaras?: ').grid(row=1, column=0)
        cboMaterial = ttk.Combobox(frame, state='readonly')
        cboMaterial.grid(row=1,column=1)
        cboMaterial['values'] = ('Hierro', 'Tela', 'Cuero')
        cboMaterial.current(0)

        #Tier
        Label(frame, text='¿Que Tier vas a craftear?: ').grid(row=2, column=0)
        cboTier = ttk.Combobox(frame,state='readonly')
        cboTier.grid(row=2, column=1)
        cboTier['values'] = ('Tier 4', 'Tier 5', 'Tier 6', 'Tier 7', 'Tier 8')
        cboTier.current(0)

        #Nivel de encantamiento
        Label(frame,text='Nivel de encantamiento: ').grid(row=4, column=0)
        cboNivel = ttk.Combobox(frame, state='readonly')
        cboNivel.grid(row=4, column=1)
        cboNivel['values'] = ('Punto 0', 'Punto 1', 'Punto 2', 'Punto 3')
        cboNivel.current(0)

        #Boton Segundo paso

        

        btnCalcu = ttk.Button(frame, text='A calcular', command=segundopaso).grid(row=7, column=1)


"""
class Calculadora():

    def __init__(self, Calculadora):
        self.calc = Calculadora()
        self.calc.title('Ingreso de Valores')

    div = LabelFrame(self.calc, text='Ingresa los valores')
    div.grid(row=0, column=0, columnspan=3, pady=20)

    Label(div, text='Foco que gastas por Unidad: ').gird(row=1, colum=1)
    self.focoxunidad = Entry(div)
    self.FocoxUnidad.grid(row=1, column=1)

    if __name__ == '__main__':
    Cal = Tk()
    Inicio(Cal)
    Cal.mainloop()

"""



if __name__ == '__main__':
    Ventana= Tk()
    Inicio(Ventana)
    Ventana.mainloop()


