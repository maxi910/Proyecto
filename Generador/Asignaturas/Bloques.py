import random
import numpy as np

def gen(n):
    asignaturas = []
    for i in range(n):
        asignaturas.append(f"asignatura_{i}")
    return asignaturas 

#asignaturas_generadas = gen(40)
#y = asignaturas_generadas #CONJASIGNATURA
#print(y)

def indispensable(conjasignatura): #RETORNA UNA LISTA DE LARGO len(conjasignatura//5)
    indispensable = random.sample(conjasignatura, len(conjasignatura)//5)
    return indispensable 

#t = indispensable(y)
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

#w = cant_alumnos(y)
#print(w)

def tipo_bloque(conjasignatura): #POR CONVENCION NUESTRA 0 ES SIMPLE Y 1 ES DOBLE!!
    doble_simple = {}
    for asignatura in conjasignatura:
        tipo_i = random.choices([0, 1], weights=[65, 35])[0]
        doble_simple[asignatura] = tipo_i
    return doble_simple

#j = tipo_bloque(y) 
#print(j)

def ordenar_prioridad(conjprioridadasignada):
    if conjprioridadasignada is None:
        print("Error: conjprioridadasignada es None")
        return {}
    
    ordenar = dict(sorted(conjprioridadasignada.items(), key=lambda item: item[1], reverse=True))
    return ordenar

#k = ordenar_prioridad(z) #OJO ES Z NO Y 
#print(k)

def conjprioridad(conjprioridad): #Esta funcion deberia funcionar me da paja arreglar el tema con mi compu pero demas corre
    dic_conjprioridad = {}
    for clave, valor in conjprioridad.items():
        if valor >= 6:
            dic_conjprioridad[clave] = valor  
    return dic_conjprioridad

#l = conjprioridad(k)
#print(l)

def bloques_restriccion(conjasignatura, tipo):
    dias = list(range(1, 36))  
    restricciones = {} 

    for asignatura in conjasignatura:
        if tipo[asignatura] == 1:
            dias_disponibles = [dia for dia in dias if dia % 7 != 0]
        else:

            dias_disponibles = dias

        num_dias = random.randint(7, 21)

        restricciones[asignatura] = random.sample(dias_disponibles, min(num_dias, len(dias_disponibles)))

    return restricciones

#f = bloques_restriccion(y, j)
#print(f)

def disponibles(conjasignaturasrestringidas): #funcion en construccion
    Permitidos = {}
    dias = [1, 2, 3, 4, 5]
    bloques_completos = [(dia, bloque) for dia in dias for bloque in range(1, 8)]
    for ramo, bloques_restringidos in conjasignaturasrestringidas.items():
        Permitidos[ramo] = [bloque for bloque in bloques_completos if bloque not in bloques_restringidos]
    
    return Permitidos

#q = disponibles(f)
#print(q)
   

def union(prioridad,cantidad,tipo,restriccion): #Se le ingresa 4 diccionarios con la misma llave y hara que devuelva un nuevo diccionario = {Asignatura : prioridad, cantindad, tipo, tupla}
    diccionario__asignatura = {}
    for asignatura in prioridad.keys():
        diccionario__asignatura[asignatura] = (prioridad[asignatura], cantidad[asignatura], tipo[asignatura], restriccion[asignatura])
    return diccionario__asignatura

#s = union(k,w,j,f)
#print(s)

#SI QUIERO SOLO LOS INDISPENSABLES entonces hago este

#a = union(l,w,j,f)
#print(a)

#PRIORIDAD>TIPO>CANTIDAD

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

#v = asignaciones(q, j)
#print(v)

def matriz(diccionario):
    num_asignaturas = len(diccionario)
    matriz = np.zeros((num_asignaturas, 38), dtype=int) 
    for i, (key, asignatura_data) in enumerate(diccionario.items()):
        matriz[i, 0] = asignatura_data[0]  
        matriz[i, 1] = asignatura_data[1] 
        matriz[i, 2] = asignatura_data[2] 
        restricciones = asignatura_data[3]
        limite_restricciones = min(len(restricciones), 35)
        matriz[i, 3:3 + limite_restricciones] = restricciones[:limite_restricciones]

    return matriz

#qq = matriz(s)
#print(qq)

def recortada(matrix):
    A = np.delete(matrix, [0,1,2], axis = 1)
    return A

def dummy(recortada):
    return np.where(recortada == 0, 1, 0)

def encasillar(recortada):
    matriz_encasillada = np.zeros_like(recortada)
    for i in range(recortada.shape[0]):
        for num in recortada[i]:
            if 1 <= num <= 35:
                matriz_encasillada[i, num - 1] = num  
    
    return matriz_encasillada