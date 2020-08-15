#JulioCesar-Vinegre

### Importar Script para Encriptar ###
from cifrado_Vinegre import *
from cifrado_JulioCesar import *


##Objetos##
julio = JulioCesar()
vigenere = Vigenere()


###Class Menu###
class Menu:
	def __init__(self):
		self.textoPlano = ""
		self.textoCifrado = ""


	def setTextoPlano(self):
		self.textoPlano = input("Ingresar Texto Plano: ").upper()


	def setTextoCifrado(self):
		self.textoCifrado = input("Ingresa el Texto Cifrado: ").upper()


	def setNumeroCasillas(self):
		numero = int(input("Ingresar el Numero de Casillas: "))
		julio.setNumeroCasillas(numero) 


	def setPalabraClave(self):
		palabra_clave = input("Ingresar Palabra Clave: ").upper()
		vigenere.setPalabra_Clave(palabra_clave) 


	def cifrar_secuencia(self):
		textoCifrado = self.textoPlano
		for i in range(2):
			textoCifrado = julio.cifrar_descifrar(textoCifrado, julio.cifrar)
			textoCifrado = vigenere.cifrar_descifrar(textoCifrado, vigenere.cifrar )
		return textoCifrado


	def descifrar_secuencia(self):
		textoCifrado = self.textoCifrado
		for i in range(2):
			textoCifrado = julio.cifrar_descifrar(textoCifrado, julio.descifrar)
			textoCifrado = vigenere.cifrar_descifrar(textoCifrado, vigenere.descifrar)
		return textoCifrado



menu = Menu()
### Menu Principal ###
def main():
	opcion = 1
	while opcion!=4:
		opcion = menu_opciones()
		if opcion>0 and opcion<=4:
			opcion = menu_ejecucion(opcion)
		else:
			print("Opcion Incorrecta, Intentelo De Nuevo!")


def menu_opciones():
	print("Elige una Opcion: ")
	return int(input("1. Cifrar\n2. Descifrar\n3. Cambiar Opciones\n4. Salir\n|: "))


def menu_ejecucion(opcion):
	if opcion == 1:
		menu.setTextoPlano()
		print(menu.cifrar_secuencia())
		return 1
	elif opcion == 2:
		menu.setTextoCifrado()
		print(menu.descifrar_secuencia())
		return 2
	elif opcion == 3:
		print(cambiarOpciones())
		return 3
	else:
		print("Saliendo del Programa...")
		return 4


def cambiarOpciones():
	print("Ingresar Opciones: ")
	opciones = int(input("1. Numero de Casillas\n2. Palabra Clave\n|: "))
	if opciones>0 and opciones<=2:
		if opciones == 1:
			menu.setNumeroCasillas()
		else:
			menu.setPalabraClave()
		return "Opciones Modificadas!"
	else:
		return "Opcion no Valida"


if __name__ == "__main__":
	main()