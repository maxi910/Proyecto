import random
from ..Asignaturas.Bloques import cant_alumnos, gen

def gens(s):
    salas = []
    for i in range(s):
        salas.append(f"sala_{i+1}")
    return salas

salas_generadas = gens(4)
x = salas_generadas #CONJSALAS
#print(x)

def cant_salas(conjsala):
    cantidad_asignada = {}
    for sala in conjsala:
        cantidad_i = random.randint(45, 80)
        cantidad_asignada[sala] = cantidad_i
    return cantidad_asignada

b = cant_salas(x)
#print(b)

asignaturas_generadas = gen(45)

y = asignaturas_generadas
#print(y)
w = cant_alumnos(y)
#print(w)