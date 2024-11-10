import random

def gens(s):
    salas = []
    for i in range(s):
        salas.append(f"sala_{i+1}")
    return salas

salas_generadas = gens(4)
x = salas_generadas #CONJSALAS
#print(x)

def capacidad_salas(conjsala):
    cantidad_asignada = {}
    for sala in conjsala:
        cantidad_i = random.randint(45, 80)
        cantidad_asignada[sala] = cantidad_i
    return cantidad_asignada

#a = gens(5)
#b = capacidad_salas(a)

#print(b)

