import re

# Podemos utilizar las expresiones regulares para la validación de URL

# Este serie el patron que sigue una URL
url = re.compile(r"^(https?://)?([da-z.-]+).([a-z.]{2,6})([/w .-]*)*/?$")

if url.search("http://pythondiario.com.co"):  # Comprobemos que esta es una URL valida
    print("URL Valida")
else:
    print("URL No Valida")
