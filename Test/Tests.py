

"""

import math
from FuncionesCrafteo import CantidadFabricar, MaterialSinFoco, MaterialConFoco, LlenadoDeLibros, CostoMaterial, PlataParaCraftear, GastoEnLibros, TotalInvertir, TotalPlataGanadaPorElCrafteo, GananciaLibros, GananciaFinal

foco = int(input('Cuanto te cuesta el foco por unidad: '))
cantFoco = int(input('Cuanto foco tienes: '))
cantItemxFoco =  CantidadFabricar(foco, cantFoco)
cantMaterial = int(input('Cuanto material gasta x Item Sin devolucion: '))
totalMaterialSFoco = MaterialSinFoco(cantItemxFoco, cantMaterial)
tasaDev = int(input('Taza de Devolucion de Material: '))
TotalMaterialCFoco = MaterialConFoco(totalMaterialSFoco, tasaDev)
famaItem =int(input("Cuanta fama te da al craftear 1 item: ")) 
famaLibro = int(input('Con cuanta fama se llena el libro: '))
LlenadoLibros = LlenadoDeLibros(famaItem, famaLibro, cantItemxFoco)
CostMaterial = int(input('Cual es el valor de Material Unitariamente: '))
CstMaterial = CostoMaterial(CostMaterial, TotalMaterialCFoco)
PCrafteo = int(input('Cual es el valor al crafear un item: '))
PlataCraftear = PlataParaCraftear(cantItemxFoco, PCrafteo)
ValItem = int(input('Cual es el valor del Item crafteado a vender:'))
TotalPlataGanadaxElCrafteo = TotalPlataGanadaPorElCrafteo(cantItemxFoco, ValItem)
PLibroVacio = int(input('Cuanto cuesta el libro Vacio: '))
GastLibros = GastoEnLibros(LlenadoLibros, PLibroVacio)
Inversion = TotalInvertir(CstMaterial, PlataCraftear, GastLibros)
PreLibroLleno = int(input('Valor del Libro lleno:'))
GanLibros = GananciaLibros(PreLibroLleno, LlenadoLibros, GastLibros)
Total = GananciaFinal(TotalPlataGanadaxElCrafteo, GanLibros, Inversion)
# ---------------------------------------------------------------------------------------------------------
print('------------------------------------------------------------------------------')
print('Tu inversion sera de: ',Inversion)
print('Tu ganancia en Libros sera de: ',GanLibros)
print('Tu ganancia final es de: ',Total)
# ---------------------------------------------------------------------------------------------------------
print('------------------------------------------------------------------------------')
print(cantItemxFoco)
print(totalMaterialSFoco)
print(TotalMaterialCFoco)
print(LlenadoLibros)
print(CstMaterial)
print(PlataCraftear)
print(TotalPlataGanadaxElCrafteo)
print(GastLibros)
print(Inversion)
print(GanLibros)
print(Total)
"""

'''
print('Selecciono Capuchas')
foco = int(input('Cuanto te cuesta el foco por unidad: '))
cantFoco = int(input('Cuanto foco tienes: '))
cantItemxFoco = math.floor(cantFoco / foco)
cantMaterial = int(input('Cuanto material gasta x Item Sin devolucion: '))
totalMaterialSFoco = math.floor(cantItemxFoco * cantMaterial)
tasaDev = float(input('Taza de Devolucion de Material: '))
TotalMaterialCFoco = math.ceil((totalMaterialSFoco * ((100-math.floor(tasaDev))/100)))

print(cantItemxFoco)
print(totalMaterialSFoco)
print(TotalMaterialCFoco)
'''
import math
from FunciAndClass import Tela

enca=0
print(enca)

enca = int(input('¿Vas a craftear con material Encantado?\n1) Si\n2) No\n'))
if enca == 1:
    punto = int(input("¿Que nivel de encantamiento es tu material?\n1) Punto 1\n2) Punto 2\n3) Punto 3\n"))
else:
    enca = 2
    punto = 0   
    

tier = int(input("¿Que tier vas a craftear?:\n1) T4\n2) T5\n3) T6\n4) T7\n"))
print('encantamiento 1 si 2 no:\n',enca)
print('punto a encantar:\n',punto)
print('tier a encantar 1) T4 2) T5 3) T6 4) T7:\n',tier)


#cantidad = Tela.Sandalias(enca,punto,tier,32)
#cantidad2 = Tela.Sandalias(enca,punto,tier,20)
#cantidad3 = Tela.Sandalias(enca,punto,tier,22)
cantidad4 = Tela.Sandalias(enca,punto,tier,25)

print(cantidad4)


#print(math.ceil(cantidad))
#print(math.ceil(cantidad2))
#print(math.ceil(cantidad3))
#print(math.ceil(cantidad4))