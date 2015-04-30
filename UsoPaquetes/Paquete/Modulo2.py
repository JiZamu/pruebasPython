class Empleado:
	def __init__(self, nom, ed):
		self.__nombre = nom
		self.__edad = ed

	def imprimir(self):
		print "En clase Empleado"
		print "Nombre: "+self.__nombre
		print "Edad: "+str(self.__edad)