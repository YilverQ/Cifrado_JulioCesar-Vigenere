#Python Cifrado de Vigenère

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Vigenere:
	def __init__(self):
		self.palabra_clave = "PYTHON"
		self.texto_plano = ""
		self.texto_cifrado = ""


	def __str__(self):
		return f"Texto Plano: {self.texto_plano}\nTexto Cifrado: {self.texto_cifrado}\nPalabra Clave: {self.palabra_clave}"

	def ingresar_texto(self):
		self.texto_plano = input("Ingresar Texto a Cifrar: ").upper()


	def ingresar_clave(self):
		self.palabra_clave = input("Ingresa Clave").upper()


	def letra_clave(self,iterador):
		return self.palabra_clave[iterador]


	def cifrar_descifrar(self, texto, funcion):
		texto_generado = ""
		iterador = 0

		for i in texto:
			if iterador>len(self.palabra_clave)-1:
				iterador = 0
		
			if i in abecedario:
				posicion_letra = abecedario.find(i)
				posicion_clave = abecedario.find(self.letra_clave(iterador))
				nueva_posicion = funcion(posicion_letra, posicion_clave)
				texto_generado += abecedario[nueva_posicion]
				iterador += 1
			else:
				texto_generado += i

		self.texto_cifrado = texto_generado
		return texto_generado


	def cifrar(self, posicion_letra, posicion_clave):
		return (posicion_letra + posicion_clave) % len(abecedario)


	def descifrar(self, posicion_letra, posicion_clave):
		return (posicion_letra - posicion_clave) % len(abecedario)


	def getTextoCifrado(self):
		return self.texto_cifrado


	def getTextoPlano(self):
		return self.texto_plano

	def setPalabra_Clave(self, texto):
		self.palabra_clave = texto