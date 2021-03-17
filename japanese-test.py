import random
import sys

unidaduno = {'わたし' : 'yo', 'わたしたち' : 'nosotros'}
keys = list(unidaduno.keys())
random.shuffle(keys)
x = True
for x in keys:
    print("¿Que significa: " + x + "?")
    res = input()
    if res == unidaduno[x]:
        print("Correcto!")
    else:
        print("Incorrecto, la respuesta correcta era: " + unidaduno[x])