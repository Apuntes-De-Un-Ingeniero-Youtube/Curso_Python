import re

cadena = "Aprendiendo expresiones regulares"
textoBuscar = "Aprendiendo"

print('Texto encontrado' if re.search(".endien.", cadena, re.IGNORECASE)
      is not None else 'texto NO encontrado')

textoEncontrado = re.search(textoBuscar, cadena, re.IGNORECASE)
print("El texto encontrado inicia en el caracter: ", textoEncontrado.start())
print("El texto encontrado termina en el caracter: ", textoEncontrado.end())
print("El texto encontrado va desde los caracteres: ", textoEncontrado.span())
