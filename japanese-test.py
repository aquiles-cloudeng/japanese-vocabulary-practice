import random
import sys
def unidaduno():
    listaunidaduno = {'わたし' : 'yo', 'わたしたち' : 'nosotros'}
    keys = list(listaunidaduno.keys())
    random.shuffle(keys)
    x = True
    for x in keys:
        print("¿Que significa: " + x + "?")
        res = input()
        if res == listaunidaduno[x]:
            print("Correcto!")
        else:
            print("Incorrecto, la respuesta correcta era: " + listaunidaduno[x])

print("Elegí un número de unidad para practicar")
uni = int(input())
if uni == 1:
    unidaduno()
else:
    print("la unidad todavía no está programada!")