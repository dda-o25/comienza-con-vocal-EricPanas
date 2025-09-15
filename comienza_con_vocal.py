"""
Eric Fernando Panas López Dellamary

15/09/2025

Dada una palabra, determina si comienza con vocal o no.
"""

# Declaraciones
VOCALES = ("a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "ä", "ë", "ï", "ö","ü") 

# Entradas
palabra = input("Escribe una plabra: ")

# Proceso
palabra_minusculas =  palabra.lower()
if palabra_minusculas[0] in VOCALES:
    vocal = ""
else:
    vocal = "no " 

# Salidas
print("'" + palabra + "' " + vocal + "comienza con vocal")
