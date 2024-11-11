import random

def matrizdzn(matrix, filename="matrix_data.dzn"):
    with open(filename, 'w') as f:
        f.write("matrix = [|\n")
        for row in matrix:
            row_str = ", ".join(map(str, row))
            f.write(f"  {row_str} |\n")
        f.write("|];\n")

    print(f"El archivo se guardo '{filename}'")


def capacidaddzn(capacidad_sala, filename="Capacidad_salas.dzn"):
    with open(filename, 'w') as f:
        capacidades = list(capacidad_sala.values())
        f.write("capacidad salas= [")
        f.write(", ".join(map(str, capacidades)))
        f.write("];\n")


def cant_alumnosdzn(cant_alumnos, filename="cantidad_alumnos.dzn"):
    with open(filename, 'w') as f:
        cantidad = list(cant_alumnos.values())
        f.write("cant_alumnos = [")
        f.write(", ".join(map(str, cantidad)))
        f.write("];\n")

def prioridaddzn(prioridadd, filename="prioridad.dzn"):
    with open(filename, 'w') as f:
        prioridad = list(prioridadd.values())
        f.write("Prioridad = [")
        f.write(", ".join(map(str, prioridad)))
        f.write("];\n")

def tipobloquedzn(tipobloqueq, filename= "tipobloque.dzn"):
    with open(filename, 'w') as f:
        tbloque = list(tipobloqueq.values())
        f.write("TipoBloque = [")
        f.write(", ".join(map(str, tbloque)))
        f.write("];\n")
     