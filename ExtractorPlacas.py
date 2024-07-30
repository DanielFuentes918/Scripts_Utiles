import re

# Los datos de la columna de texto que proporcionaste
datos = """
#N/D
P-PCO-TCG1234
TP-HBE1234 VR29 TRA5213
"""

# Definimos una expresión regular para encontrar las placas
expresion_regular = r'\b[A-Z]{2}\d{3}\b'

# Buscamos todas las coincidencias en los datos
placas_encontradas = re.findall(expresion_regular, datos)

# Imprimimos las placas encontradas
for placa in placas_encontradas:
    print(placa)
