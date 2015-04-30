class Empleado:
	def __init__(self, nom, ed):
		self.__nombre = nom
		self.__edad = ed

	def especificar(self, nom, ed):
		self.__nombre = nom
		self.__edad = ed

	def imprimir(self):
		print "El nombre: "+self.__nombre
		print "La edad: "+str(self.__edad)

	def getNombre(self):
		return self.__nombre

	def getEdad(self):
		return self.__edad

	def setNombre(self, nom):
		self.__nombre = nom

	def setEdad(self, ed):
		self.__edad = ed

	#Uso de propiedades
	nombre = property(getNombre, setEdad)
	edad = property(getEdad, setEdad)

empleado1 = Empleado("Eduardo Jimenez", 20)
empleado1.imprimir()
print str(empleado1.getEdad())
print empleado1.nombre
