# main.py
import random
from Asignaturas.Bloques import cant_alumnos, prioridad_aleatoria, indispensable, tipo_bloque, bloques_restriccion, gen, union
from Salas.Salas import capacidad_salas, gens
from DZN.generar_dzn import generar_dzn

 
def main():
    num_asignaturas = 300
    num_salas = gens(18)

    asignaturas = gen(num_asignaturas)

    indispensables = indispensable(asignaturas)
    prioridad = prioridad_aleatoria(asignaturas, indispensables)
    cantidadalumnos = cant_alumnos(asignaturas)
    capacidadsala = capacidad_salas(num_salas)
    tipobloque = tipo_bloque(asignaturas)
    restriccionesbloques = bloques_restriccion(asignaturas, tipobloque)
    diccionario = union(prioridad,cantidadalumnos,tipobloque,restriccionesbloques)

    generar_dzn(diccionario, capacidadsala, filename="instancia.dzn")

    print("Archivo instancia.dzn generado exitosamente.")

if __name__ == "__main__":
    main()
