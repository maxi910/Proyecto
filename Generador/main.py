import random
from Asignaturas.Bloques import cant_alumnos, prioridad_aleatoria, indispensable, tipo_bloque, bloques_restriccion, gen, union, matriz, recortada, dummy
from Salas.Salas import capacidad_salas, gens
from DZN.generar_dzn import matrizdzn 

 
def main():
    num_asignaturas = 40
    num_salas = gens(3)

    asignaturas = gen(num_asignaturas)

    indispensables = indispensable(asignaturas)
    prioridad = prioridad_aleatoria(asignaturas, indispensables)
    cantidadalumnos = cant_alumnos(asignaturas)
    capacidadsala = capacidad_salas(num_salas)
    tipobloque = tipo_bloque(asignaturas)
    restriccionesbloques = bloques_restriccion(asignaturas, tipobloque)
    diccionario = union(prioridad,cantidadalumnos,tipobloque,restriccionesbloques)
    matrix = matriz(diccionario)
    recortadad = recortada(matrix)
    DUM = dummy(recortadad)
    matrizdzn(matrix, filename="matriz.dzn")
    matrizdzn(recortadad, filename="Matrizrecortada.dzn")
    matrizdzn(DUM, filename="Matrizdisponibilidad.dzn")


    print("Archivos instancia.dzn generado exitosamente.")

if __name__ == "__main__":
    main()
