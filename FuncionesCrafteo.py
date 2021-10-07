import math

# Funcion cantidad a Fabricar
def CantidadFabricar(ValorFocoUnidad,FocoTotal):
    return math.floor((FocoTotal / ValorFocoUnidad))

# Funcion material sin foco
def MaterialSinFoco(CantidadFabricar, MaterialxItem):
    return(CantidadFabricar * MaterialxItem)

# Funcion Material con Foco
def MaterialConFoco(MaterialSinFoco, TasaDebolucion):
    return (math.ceil((MaterialSinFoco * ((100-math.floor(TasaDebolucion))/100))))

#--------------------------------------------------------------------------

# Funcion Calcular llenado de libros
def LlenadoDeLibros(FamaxItem, FamaTotalLibro, CantidadItem):
    return (math.ceil((FamaxItem / FamaTotalLibro) * CantidadItem))

#--------------------------------------------------------------------------

# Funcion Costo Material
def CostoMaterial(PrecioMaterial, MaterialConFoco):
    return (PrecioMaterial * MaterialConFoco)

# Funcion Plata para Craftear
def PlataParaCraftear(CantidadCraftear, PrecioPorCraftearItem):
    return (CantidadCraftear * PrecioPorCraftearItem)

# Funcion Gasto en Liabros
def GastoEnLibros(LlenadoDeLibros,ValorLibros):
    return (LlenadoDeLibros * ValorLibros)

# Funcion Total Invertir Materiales(con libros incluidos)
def TotalInvertir(CostoMaterial, PlataParaCraftear, GastoEnLibros):
    return (CostoMaterial + PlataParaCraftear + GastoEnLibros)

# Funcion para saber cuanto ganas solo crafteo sin libros
def TotalPlataGanadaPorElCrafteo(CantidadAFabricar, ValorItem):
    return (CantidadAFabricar * ValorItem)

# Funcion para saber la ganancia de los libros
def GananciaLibros(PrecioLibroLleno, LibrosLlenos, GastoEnLibros):
    return ((PrecioLibroLleno * LibrosLlenos)-GastoEnLibros)

# Funcion para saber cuanta plata se gana en total 
def GananciaFinal(TotalPlataGanadaPorElCrafteo,GananciaLibros,TotalInvertir):
    return ((TotalPlataGanadaPorElCrafteo + GananciaLibros)- TotalInvertir)

'''
# Funcion cantidad a Fabricar
def CantidadFabricar(ValorFocoUnidad,FocoTotal):
    return math.floor((FocoTotal / ValorFocoUnidad))

# Funcion material sin foco
def MaterialSinFoco(CantidadFabricar, MaterialxItem):
    return(CantidadFabricar * MaterialxItem)

# Funcion Material con Foco
def MaterialConFoco(MaterialSinFoco, TasaDebolucion):
    return (math.ceil((MaterialSinFoco * ((100-math.floor(TasaDebolucion))/100))))

#--------------------------------------------------------------------------

# Funcion Calcular llenado de libros
def LlenadoDeLibros(FamaxItem, FamaTotalLibro, CantidadItem):
    return (math.ceil((FamaxItem / FamaTotalLibro) * CantidadItem))

#--------------------------------------------------------------------------

# Funcion Costo Material
def CostoMaterial(PrecioMaterial, MaterialConFoco):
    return (PrecioMaterial * MaterialConFoco)

# Funcion Plata para Craftear
def PlataParaCraftear(CantidadCraftear, PrecioPorCraftearItem):
    return (CantidadFabricar * PrecioPorCraftearItem)

# Funcion Gasto en Liabros
def GastoEnLibros(LlenadoDeLibros,ValorLibros):
    return (LlenadoDeLibros * ValorLibros)

# Funcion Total Invertir Materiales(con libros incluidos)
def TotalInvertir(CostoMaterial, PlataParaCraftear, GastoEnLibros):
    return (CostoMaterial + PlataParaCraftear + GastoEnLibros)

# Funcion para saber cuanto ganas solo crafteo sin libros
def TotalPlataGanadaPorElCrafteo(CantidadAFabricar, ValorItem):
    return (CantidadAFabricar * ValorItem)

# Funcion para saber la ganancia de los libros
def GananciaLibros(PrecioLibroLleno, LibrosLlenos, GastoEnLibros):
    return ((PrecioLibroLleno * LibrosLlenos)-GastoEnLibros)

# Funcion para saber cuanta plata se gana en total 
def GananciaFinal(TotalPlataGanadaPorElCrafteo,GananciaLibros,TotalInvertir):
    return ((TotalPlataGanadaPorElCrafteo + GananciaLibros)- TotalInvertir)
'''

'''

x = CantidadFabricar(675,22200)
print(x)

y = MaterialSinFoco(x,16)
print(y)

d = MaterialConFoco(y,47.9)
print(d)

a = LlenadoDeLibros(22320,19200,32)
print(a)

def hola():
    return('Hola Mundo')

x = hola()
print(x)

'''