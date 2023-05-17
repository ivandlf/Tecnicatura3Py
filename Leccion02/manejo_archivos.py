# Declaramos una variable

try:
    archivo = open('prueba.txt', 'w', encoding='utf8')  # La w es de write que significa escribir
    archivo.write('programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Con esto terminamos')
    archivo.write('los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción')
except Exception as e:
    print(e)
finally:  # siempre se ejecuta
    archivo.close()  # con esto se debe cerrar el archivo
#archivo.write('Todo quedo perfecto'): este es un error