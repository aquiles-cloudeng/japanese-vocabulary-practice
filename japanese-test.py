import random
import sys

listaunidad1 = {'わたし' : 'yo', 'わたしたち' : 'nosotros'}

listaunidad2 = {'これ' : 'esto', 'それ' : 'ese', 'あれ' : 'aquello'}

listaunidad3 = {'ここ'　: 'aqui', 'そこ' : 'ahi', 'あそこ'　: 'alla', 'どこ': 'donde', 'どちら'　: 'donde',
                'こちら'　: 'aqui', 'そちら'　: 'ahi', 'あちら' : 'alla', 'どちら'　: 'donde',
                'きょうしつ'　: 'aula', 'しょくどう'　: 'comedor', 'じむしょ' : 'oficina', 'かいぎしつ'　: 'sala de reuniones',
                'うけつけ'　: 'recepcion', 'ロビー'　: 'lobby', 'へや'　: 'habitacion', 'トイレ'　: 'baño', 'かいだん'　: 'escaleras',
                'エレベーター'　: 'ascensor', 'エスカレーター'　: 'escalera mecanica', 'くに'　: 'pais', 'かいしゃ'　: 'empresa',
                'うち' : 'casa', 'でんわ'　: 'telefono', 'くつ' : 'zapatos', 'ネクタイ'　: 'corbata', 'ワイン'　: 'vino', 'たばこ'　: 'cigarrillos', 'うりば'　: 'secciom' #hoja 1 unidad 3 termina aca

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

