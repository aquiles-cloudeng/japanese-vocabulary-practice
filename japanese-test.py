import random
import sys

listaunidad1 = {'わたし' : 'yo', 'わたしたち' : 'nosotros'}
listaunidad2 = {'これ' : 'esto', 'それ' : 'ese', 'あれ' : 'aquello'}


def ejercicio(uniraw):
    unidad = eval("listaunidad" + uniraw)
    keys = list(unidad.keys())
    random.shuffle(keys)
    x = True
    for x in keys:
        print("¿Que significa: " + x + "?")
        res = input()
        if res == unidad[x]:
            print("Correcto!")
        else:
            print("Incorrecto, la respuesta correcta era: " + unidad[x]) #agregar una lista donde guarda los errores
        #opcion de guardar el archivo al final

def inicio():
    print("Elegí un número de unidad para practicar")
    uniraw = input()
    if uniraw.isdecimal():
        try:
            ejercicio(uniraw)
        except:
            print("La unidad " + uniraw + " aun no está codeada")
    else:
        print("Por favor ingresar el número de unidad en decimal: (1, 2, 3, etc)")
        inicio()

inicio()

