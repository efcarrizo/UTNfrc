import random
random.seed(20)
#Archivo de Clase y Funciones

#Creacion de la clase de servicios de limpieza con sus atributos en el metodo constructor
class Limpieza():
    
    def __init__(self, id , descripcion, tipo, monto, personal):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.monto = monto 
        self.personal = personal
        
    def __str__(self):
        return f"ID: {self.id}, descripcion: {self.descripcion}, tipo: {self.tipo}, monto: {self.monto}, personal involucrado: {self.personal}"
    
#Definimos el menu de opciones en una función
def menu():
    
    print("1- Cargue el arreglo con n Trabajos solicitados.")
    print("2- Mostrar el listado de trabajos de menor a mayor.")
    print("3- Mostrar trabajo con la mayor cantidad de personal afectado.")
    print("4- Buscar trabajo por descripción.")
    print("5- Mostrar cantidad de trabajos por tipo.")
    print("0- Salir del programa")
    
    op = int(input("Ingrese la opcion deseada: "))
    
    return op

#Funcion para hacer la carga de objetos a los registros
def cargar_trabajos(vector):
    
    #Lista de Trabajos para seleccionar por medio de Choise automatico
    #Son ejemplos de trabajo
    trabajos_limpieza = [
    "Estación de servicio",
    "Oficina corporativa",
    "Hospital",
    "Escuela",
    "Edificio residencial",
    "Restaurante",
    "Centro comercial",
    "Gimnasio",
    "Fábrica",
    "Hotel"
    ]
    
    n = int(input("Ingrese la cantidad de trabajos a realizar: "))
    
    #Dependiendo los trabajos creamos cada solicitud de trabajo
    for i in range(n):
        
        id = random.randint(0,100)
        trabajo = random.choice(trabajos_limpieza)
        tipo = random.randint(0,3)
        monto = round(random.uniform(150000.00, 700000.00), 2)
        personal = random.randint(1,20)
        
        t1 = Limpieza(id,trabajo,tipo,monto,personal)
        
        vector.append(t1)
    
    #Devolvemos el vector con todos los objetos ingresados
    return vector

def ordenamiento(vector):
    #Ordenamiento, nos paramos sobre el primer elemento
    for i in range(len(vector)-1):
        #Nos paramos sobre el siguiente caracter 
        for j in range(i+1, len(vector)):
            #Comparamos ambos montos para intercambiarlos el siguiente es mayor
            if vector[i].monto < vector[j].monto:
                vector[i], vector[j] = vector[j], vector[i]

def mayor_personal(vector):
    #Creamos la variable para el mayor y para guardar el objeto
    mayor = 0
    trabajo_mayor = None
    #Recorremos el vector elemento a elemento para ver cual es el mayor
    for elem in vector:
        if elem.personal > mayor:
            mayor = elem.personal
            trabajo_mayor = elem
            
    return trabajo_mayor

def busqueda(vector, d):
    #Tipo de busqueda secuencial va buscando 1 x 1
    #Sirve si no esta ordenado el vector
    resultado = None
    #Recorremos los elementos del vector
    for elem in vector:
        #Si la busqueda ingresada es igual al elemento
        if d.capitalize() == elem.descripcion:
            resultado = elem
            break
            
    return resultado

def busqueda_binaria(vector, d):
    
    resultado = None
    
    #Definimos el numero n
    n = len(vector)
    #Posicionadores de los extremos
    izq = 0
    der = n-1
    #Mientras el derecho no sea menor o igual que el izquierdo
    while izq <= der:
        #Para posicionarnos en la mitad
        c = (der + izq)//2
        #Si la mitad es lo mismo que lo que ingresamos
        if vector[c].descripcion == d.capitalize():
            resultado = vector[c]
            break
        
        #Si es menor nos corremos un lugar a la derecha desde donde estaba c
        if d < vector[c].descripcion:
            der = c - 1
        #Si no corremos el izquierdo uno mas de la donde estaba c
        else:
            izq = c + 1
            
    return resultado

def vector_conteo(vector):
    #Generamos un vector de conteo vacio
    vec_cont = 4 * [0]
    #Dependiendo que tipo sea cual le sumamos
    for elem in vector:

        if elem.tipo == 0:
            vec_cont[0] += 1
            
        elif elem.tipo == 1:
            vec_cont[1] += 1
        
        elif elem.tipo == 2:
            vec_cont[2] += 1
            
        else:
            vec_cont[3] += 1
            
    return f"Interior: {vec_cont[0]}, Exterior: {vec_cont[1]}, Piletas: {vec_cont[2]}, Tapizados: {vec_cont[3]}"
        