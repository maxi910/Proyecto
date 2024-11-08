# main.py
import random
from Generador.Asignaturas.Bloques import cant_alumnos, gen  # Ajusta las importaciones según tu estructura
from Generador.DZN.generar_dzn import generar_dzn
 
def main():
    # Configuración inicial
    num_asignaturas = 10
    num_salas = 5

    # Generación de asignaturas y salas
    asignaturas = generar_asignaturas(num_asignaturas)
    salas = [f"sala_{i+1}" for i in range(num_salas)]

    # Generar datos asociados a las asignaturas
    indispensables = generar_indispensables(asignaturas)
    prioridad = prioridad_aleatoria(asignaturas, indispensables)
    cantidad_alumnos = generar_cantidad_alumnos(asignaturas)
    capacidad_salas = generar_capacidad_salas(num_salas)
    tipo_bloque = generar_tipo_bloque(asignaturas)
    restricciones_bloques = bloques_restriccion(asignaturas)

    # Crear el archivo .dzn con todos los datos generados
    generar_dzn(asignaturas, salas, cantidad_alumnos, capacidad_salas, tipo_bloque, prioridad, restricciones_bloques)

    print("Archivo instancia.dzn generado exitosamente.")

# Llamada al main
if __name__ == "__main__":
    main()
