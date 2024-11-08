import random

#ESTA PARTE DEL CODIGO GENERA LAS ASIGNATURAS Y PARTICIONA EL CONJUNTO DE ASIGNATURAS EN INDISPENSABLES Y DISPENSABLES, LAS RESTRICCIONES HAN DE IR EN OTRO LADO!!
#PARA VER Q MIERDA HACE EL CODIGO SIMPLEMENTE HAY QUE PRINTEAR LO ULTIMO, el codigo al final ordena las asiganturas por prioridad
def gen(n):
    asignaturas = []
    for i in range(n):
        asignaturas.append(f"asignatura_{i}")
    return asignaturas 

asignaturas_generadas = gen(1)

y = asignaturas_generadas #CONJASIGNATURA
#print(y)

def indispensable(conjasignatura): #RETORNA UNA LISTA DE LARGO len(conjasignatura//5)
    indispensable = random.sample(conjasignatura, len(conjasignatura)//5)
    return indispensable 
t = indispensable(y)
#print(t)

def prioridad_aleatoria(conjasignatura, indispensable): #RECIBE LA LISTA DE ASIGNATURAS Y LA DE ASIGNATURAS INDISPENSABLES
    prioridad_asignada = {}
    for asignatura in conjasignatura:
        if asignatura not in indispensable:
            prioridad_asignada[asignatura]= random.randint(1,5)
        else:
            prioridad_asignada[asignatura] = random.randint(6,10)  
    return prioridad_asignada #RETORNA UN DICCIONARIO

z = prioridad_aleatoria(y,t)
#print(z) 

def cant_alumnos(conjasignatura):
    cantidad_asignada = {}
    for asignatura in conjasignatura:
        cantidad_i = random.randint(40, 80)
        cantidad_asignada[asignatura] = cantidad_i
    return cantidad_asignada # retorna dic de llave asignatura_i : cantindad de alumnos

w = cant_alumnos(y)
#print(w)

def tipo_bloque(conjasignatura): #POR CONVENCION NUESTRA 0 ES SIMPLE Y 1 ES DOBLE!!
    doble_simple = {}
    for asignatura in conjasignatura:
        tipo_i = random.choices([0, 1], weights=[35, 65])[0]
        doble_simple[asignatura] = tipo_i
    return doble_simple

j = tipo_bloque(y) 
#print(j)


def ordenar_prioridad(conjprioridadasignada):
    if conjprioridadasignada is None:
        print("Error: conjprioridadasignada es None")
        return {}
    
    ordenar = dict(sorted(conjprioridadasignada.items(), key=lambda item: item[1], reverse=True))
    return ordenar

k = ordenar_prioridad(z) #OJO ES Z NO Y 
#print(k)

def conjprioridad(conjprioridad): #Esta funcion deberia funcionar me da paja arreglar el tema con mi compu pero demas corre
    dic_conjprioridad = {}
    for clave, valor in conjprioridad.items():
        if valor >= 6:
            dic_conjprioridad[clave] = valor  
    return dic_conjprioridad

l = conjprioridad(k)
#print(l)

def bloques_restriccion(conjasignatura):
    bdia = 7
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    Bloques = []
    for dia in dias:
        for i in range(bdia):
            Bloques.append((dia, i + 1))
    
    restricciones = {}
    for asignatura in conjasignatura:
        num_bloques = random.randint(7, 21)
        restricciones[asignatura] = random.sample(Bloques, min(num_bloques, len(Bloques)))
    
    return restricciones
    
f = bloques_restriccion(y)
#print(f)

def disponibles(conjasignaturasrestringidas): #funcion en construccion
    Permitidos = {}
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    bloques_completos = [(dia, bloque) for dia in dias for bloque in range(1, 8)]
    for ramo, bloques_restringidos in conjasignaturasrestringidas.items():
        Permitidos[ramo] = [bloque for bloque in bloques_completos if bloque not in bloques_restringidos]
    
    return Permitidos

q = disponibles(f)
#print(q)

def union(prioridad,cantidad,tipo,restriccion): #Se le ingresa 4 diccionarios con la misma llave y hara que devuelva un nuevo diccionario = {Asignatura : prioridad, cantindad, tipo, tupla}
    diccionario__asignatura = {}
    for asignatura in prioridad.keys():
        diccionario__asignatura[asignatura] = (prioridad[asignatura], cantidad[asignatura], tipo[asignatura], restriccion[asignatura])
    return diccionario__asignatura

s = union(k,w,j,f)
print(s)
#si tipo[asignatura]==1:
    #no puede tomar el bloque 7

#SI QUIERO SOLO LOS INDISPENSABLES entonces hago este

a = union(l,w,j,f)
#print(a)

#falta decir q la wea de bloque no pase del 7 al 1 del dia sgte y asignar prioridad a la asignacion de salas, esto es: PRIORIDAD>TIPO>CANTIDAD

def asignaciones(Permitidos, tipo): 
    asignaciones = {}
    for asignatura in tipo:
        if tipo[asignatura] == 1:
          b = 7
          while b == 7:
            d,b = random.choice(Permitidos[asignatura])
          asignaciones[asignatura]=[d,b,b+1]
        else:
          asignaciones[asignatura]=[random.choice(Permitidos[asignatura])]
    return asignaciones

v = asignaciones(q, j)
#print(v)