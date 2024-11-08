import random

# Inserta aquí las funciones que ya has definido (gen, indispensable, prioridad_aleatoria, etc.)

def generar_dzn(filename="instancia.dzn"):
    with open(filename, "w") as f:
        # Número total de asignaturas y salas
        f.write(f"num_asignaturas = {len(asignaturas_generadas)};\n")
        f.write(f"num_salas = {len(salas_generadas)};\n")
        
        # Escribe la prioridad de cada asignatura
        f.write(f"prioridad = [{', '.join(str(z[asignatura]) for asignatura in y)}];\n")
        
        # Demanda de estudiantes por asignatura
        f.write(f"demanda = [{', '.join(str(w[asignatura]) for asignatura in y)}];\n")
        
        # Capacidad de cada sala
        f.write(f"capacidad = [{', '.join(str(b[sala]) for sala in x)}];\n")
        
        # Tipo de bloque de cada asignatura (0 para simple, 1 para doble)
        f.write(f"tipo_bloque = [{', '.join(str(j[asignatura]) for asignatura in y)}];\n")
        
        # Bloques restringidos para cada asignatura
        f.write("bloques_restriccion = [|\n")
        for asignatura in y:
            restricciones = ", ".join(f"({dia}, {bloque})" for dia, bloque in f[asignatura])
            f.write(f" [{restricciones}],\n")
        f.write("|];\n")
        
        # Bloques permitidos para cada asignatura (bloques en los que pueden ser asignados)
        f.write("bloques_disponibles = [|\n")
        for asignatura in y:
            permitidos = ", ".join(f"({dia}, {bloque})" for dia, bloque in q[asignatura])
            f.write(f" [{permitidos}],\n")
        f.write("|];\n")
        
        # Asignación de bloques inicial (puedes modificarlo según los requerimientos)
        f.write("asignacion_inicial = [|\n")
        for asignatura in y:
            asign = ", ".join(f"({d}, {b})" for d, b in v[asignatura])
            f.write(f" [{asign}],\n")
        f.write("|];\n")

# Llamada a la función para generar el archivo .dzn
generar_dzn("instancia.dzn")


