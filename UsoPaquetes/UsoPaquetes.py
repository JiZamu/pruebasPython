import Paquete.Modulo1
#para importar paquete y no colocar nombre del modulo
from Paquete.Modulo2 import Empleado

modulo1 = Paquete.Modulo1.Persona("Eduardo Ian")
modulo1.imprimir()

modulo2 = Empleado("Eduardo Jimenez", 22)
modulo2.imprimir()