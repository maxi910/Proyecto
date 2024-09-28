import random
from Asignaturas import Bloques


def gens(s):
    salas = []
    for i in range(s):
        salas.append(f"sala_{i+1}")
    return salas

salas_generadas = gens(5)
x = salas_generadas #CONJSALAS
print(x)

def cant_salas(conjsala):
    cantidad_asignada = {}
    for sala in conjsala:
        cantidad_i = random.randint(45, 80)
        cantidad_asignada[sala] = cantidad_i
    return cantidad_asignada

b = cant_salas(x)
print(b)

w = cant_alumnos(y)
print(w)