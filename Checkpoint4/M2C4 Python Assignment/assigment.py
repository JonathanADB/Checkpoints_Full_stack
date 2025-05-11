#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
from decimal import Decimal
import math

mi_lista = [1, 2, 3, 4, 5]
mi_tupla = (1, 2, 3, 4, 5)
mi_float = 3.14
mi_entero = 42
mi_decimal = Decimal('3.14')
mi_diccionario = {
    'nombre': 'Jhonny',
    'edad': 30,
    'ciudad': 'Bilbao'
}

#Exercise 2: Round your float up.
float_redondeado = math.ceil(mi_float)

#Exercise 3: Get the square root of your float.
raiz_cuadrada = math.sqrt(mi_float)

#Exercise 4: Select the first element from your dictionary.
primer_clave = next(iter(mi_diccionario))
primer_valor = mi_diccionario[primer_clave]

#Exercise 5: Select the second element from your tuple.
segundo_elemento = mi_tupla[1]

#Exercise 6: Add an element to the end of your list.
mi_lista.append(5)

#Exercise 7: Replace the first element in your list.
mi_lista[0] = 100

#Exercise 8: Sort your list alphabetically.
lista_palabra = ["banana", "manzana", "naranja", "kiwi"]
lista_palabra.sort()

#Exercise 9: Use reassignment to add an element to your tuple.
nueva_tupla = mi_tupla + (6,)