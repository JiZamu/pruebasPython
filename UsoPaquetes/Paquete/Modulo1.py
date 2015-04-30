class Persona:
	def __init__(self, nombre):
		self.__nombre = nombre

	def imprimir(self):
		print "En clase Persona"
		print "Nombre: "+self.__nombre