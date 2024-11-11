import random
from Asignaturas.Bloques import cant_alumnos, prioridad_aleatoria, indispensable, tipo_bloque, bloques_restriccion, gen, union, matriz, recortada, dummy, encasillar
from Salas.Salas import capacidad_salas, gens
from DZN.generar_dzn import matrizdzn, capacidaddzn, cant_alumnosdzn, prioridaddzn, tipobloquedzn

 
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
    orden = encasillar(recortadad)
    DUM = dummy(orden)

    matrizdzn(matrix, filename="matriz.dzn")
    matrizdzn(recortadad, filename="Matrizrecortada.dzn")
    matrizdzn(orden, filename="Ordenada.dzn")
    matrizdzn(DUM, filename="Matrizdisponibilidad.dzn")
    capacidaddzn(capacidadsala, filename = "Capacidad_salas.dzn")
    cant_alumnosdzn(cantidadalumnos, filename = "cant_alumnos.dzn")
    prioridaddzn(prioridad, filename="prioridad.dzn")
    tipobloquedzn(tipobloque, filename= "tipobloque.dzn")


    print("Archivos instancia.dzn generado exitosamente.")

if __name__ == "__main__":
    main()
