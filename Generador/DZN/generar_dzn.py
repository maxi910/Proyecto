import random


def generar_dzn(diccionario_asignatura, salas, filename="instancia.dzn"):
    # Obtener los nombres de las asignaturas y de las salas
    asignaturas = list(diccionario_asignatura.keys())
    nombres_salas = list(salas.keys())

    with open(filename, "w") as f:

        f.write(f"num_asignaturas = {len(asignaturas)};\n")
        f.write(f"num_salas = {len(nombres_salas)};\n")

        f.write(f"prioridad = [{', '.join(str(diccionario_asignatura[asignatura][0]) for asignatura in asignaturas)}];\n")

        f.write(f"cantidad de alumnos = [{', '.join(str(diccionario_asignatura[asignatura][1]) for asignatura in asignaturas)}];\n")

        f.write(f"capacidad = [{', '.join(str(salas[sala]) for sala in nombres_salas)}];\n")
        

        f.write(f"tipo_bloque = [{', '.join(str(diccionario_asignatura[asignatura][2]) for asignatura in asignaturas)}];\n")


        f.write("bloques_restriccion = [|\n")
        for asignatura in asignaturas:
            restricciones = ", ".join(f"({dia}, {bloque})" for dia, bloque in diccionario_asignatura[asignatura][3])
            f.write(f" [{restricciones}],\n")
        f.write("|];\n")

    print(f"Archivo {filename} generado exitosamente.")



