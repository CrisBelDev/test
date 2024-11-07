import sys
import urllib.request
import os

def descargar(url):
	nombreArch = url.split("/")[-1]
	
	try:
		print("Descargando el archivo...")
		urllib.request.urlretrieve(url, nombreArch)
		print("Archivo se descargo correctamente")
	except Exception as e:
		print("Error: ",e)

url = sys.argv[1]	# HACE REFERENCIA AL ARGUMENTO DE LA URL

descargar(url)
