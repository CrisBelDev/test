import sys
import urllib.request
import os

def descargar(url, ruta):
	nombreArch = url.split("/")[-1]
	rutaFija = os.path.join(ruta, nombreArch)
	try:
		print("Descargando el archivo...")
		urllib.request.urlretrieve(url, rutaFija)
		print("Archivo se descargo correctamente")
	except Exception as e:
		print("Error: ",e)

url = sys.argv[1]	# HACE REFERENCIA AL ARGUMENTO DE LA URL
ruta = sys.argv[2]	# HACE REFERENCIA A LA RUTA DONDE SE DESCARGARA EL ARCHIVO
descargar(url, ruta)
