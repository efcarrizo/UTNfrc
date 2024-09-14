from support import *

def main():
    #Vector de conteo
    vector = []
    #Inicializador de opcion para entrar el el while
    op = -1
    while op != 0:
        
        #Invocamos el menu para interactuar
        op = menu()

        if op == 1:
            cargar_trabajos(vector)
            
        elif op == 2:
           ordenamiento(vector)
           
           for elem in vector:
               print(elem)
               
        elif op == 3:
            mayor = mayor_personal(vector)
            print(mayor)
            
        elif op == 4:
            
            d = input("Ingrese el trabajo que quiere buscar por descripsión: ")
            
            # resultado = busqueda(vector,d) Busqueda secuencial
            resultado = busqueda_binaria(vector,d)
            #Si hay resultado printearlo
            if resultado:
                print(resultado)
            else:
                print(f"Otro intento{resultado}")
                print("No se encontro ningun resultado")
        
        elif op == 5:
            
            totales = vector_conteo(vector)
            print(totales)
                        

        
if __name__ == "__main__":
    main()