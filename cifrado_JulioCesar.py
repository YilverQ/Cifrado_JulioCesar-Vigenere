#Python Cifrado de Julio Cesar

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class JulioCesar:
	def __init__(self):
		self.texto_plano = ""
		self.texto_cifrado = ""
		self.casillas_mover = 3


	def __str__(self):
		return f"Texto Plano: {self.texto_plano}\nTexto Cifrado: {self.texto_cifrado}\nCasillas: {self.casillas_mover}"


	def ingresar_texto(self):
		self.texto_plano = input("Ingresa el Texto a Cifrar: ").upper()


	def ingresar_casillas_mover(self):
		self.casillas_mover = int(input("Ingresa Numero de Casillas: "))


	def cifrar_descifrar(self, texto, funcion):
		texto_generado = ""

		for i in texto:
			if i in abecedario:
				posicion_letra = abecedario.find(i)
				nueva_posicion = funcion(posicion_letra)
				texto_generado += abecedario[nueva_posicion]
			else:
				texto_generado += i

		self.texto_cifrado = texto_generado
		return texto_generado


	def cifrar(self, posicion_letra):
		return (posicion_letra+self.casillas_mover) % len(abecedario)


	def descifrar(self, posicion_letra):
		return (posicion_letra - self.casillas_mover) % len(abecedario)


	def getTextoCifrado(self):
		return self.texto_cifrado


	def getTextoPlano(self):
		return self.texto_plano


	def setNumeroCasillas(self, numero):
		self.casillas_mover = numero