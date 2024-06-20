ARCHIVO = "entrada.txt" #TERMINADO

#1
def fletter(linea):
    #Todas las letras y numeros para recorrer en las validaciones
    mayusculas, numeros = "QWERTYUIOPASDFGHJKLÑZXCVBNM", "0123456789"

    #Banderas
    #Primera letra
    first_l = False
    #Primera letra numero impar
    first_lnum = False

    #Contadores
    #Cantidad de palabras que cumplen con la condición
    cfirst_l = 0

    #Recorremos la lista que ingresa
    for l in linea:

    #Si no hay espacio o punto estamos dentro de la palabra
        if l != " " and l != ".":
            #Si primera letra es falso
            if not first_l:
                first_l = True

                if l.isdigit() and int(l) % 2 != 0:
                    first_lnum = True

                
            else:
                if l in mayusculas or l in numeros:
                    first_lnum = False

        #Al ser espacio o punto estamos fuera de la palabra
        else:
            if first_lnum:
                cfirst_l += 1

            first_l = False
            first_lnum = False

    return cfirst_l
#2
def longvocal(linea):
    #Guardamos las vocales en una variable tipo str
    vocales = "aeiouAEIOU"

    #Banderas
    #Primera letra
    first_l = False
    #Primera vocal
    first_vocal = False
    b = False

    #Contadores
    #Cantidad de caracteres que contiene cada palabra
    long = None
    letras = 0

    #Recorremos la linea que ingresa como parametro letra por letra
    for l in linea:

        #Si no es espacio o punto esta dentro de la palabra
        if l != " " and l != ".":
            if not first_l:
                first_l = True
                
                #Si la letra es una vocal se suma una letra a long
                if l in vocales:
                    first_vocal = True
                    letras += 1
            
                               
            else:
                letras += 1

                #Si la letra es b o B
                if l == "b" or l == "B":
                    b = True


        
        else:
            #Si la primera letra es vocal y tiene b
            if b and first_vocal:
                #Si longitud es none o menor que las letras que ingresaron
                if long == None or letras > long:
                    long = letras
            
            #Reseteo contadores y banderas
            letras = 0
            first_l = False
            first_vocal = False
            b = False
            

    return long
#3
def promchar(linea):

    consonantes = "qwrtypsdfghjklñzxcvbn"
    vocales = "eiou"

    #Banderas
    tiene_am = False

    #Contador
    cont_consonantes = 0
    cont_vocales = 0
    char = 0
    sum_char = 0
    total_palabras = 0

    for l in linea:
        #Si no es espacio o punto estoy dentro de la palabra
        if l != " " and l != ".":

            #Sumamos todas las letras
            char += 1

            #Si es consonante suma al contador de consonantes
            if l.lower() in consonantes:
                cont_consonantes += 1
            
            #Si es vocal suma al contador de vocales
            elif l.lower() in vocales:
                cont_vocales += 1

            
            else:
                #Si la letra es a o m levanta la bandera
                if l.lower() == "a" or l.lower() == "m" or l.isdigit():
                    tiene_am = True

            

        else:
            #Si am es false y tiene mas consonantes que vocales
            if not tiene_am and cont_consonantes > cont_vocales:
                total_palabras += 1
                sum_char += char

            #Reseteamos banderas y contadores para nueva palabra
            tiene_am = False
            cont_consonantes = 0
            cont_vocales = 0
            char = 0

    prom = sum_char // total_palabras



    return prom
#4
def expresion_d(linea):

    vocales = "aeiou"

    #Banderas
    letra_d = False
    vocal = False
    ultima_vocal = False
    #Contadores
    cant_d = 0
    ultima_letra = ""
    palabras_d = 0

    for l in linea:
        #Dentro de la palabra
        if l != " " and l != ".":
            #Si la letra que ingresa es d, se levanta la bandera
            if l.lower() == "d":
                letra_d = True

            elif letra_d:
                if l.lower() in vocales:
                    cant_d += 1
                    letra_d = False
                else:
                    letra_d = False

            
            ultima_letra = l
        else:
            if cant_d >= 2:
                if ultima_letra in vocales:
                    palabras_d += 1
            
            #Resteamos contadores
            letra_d = False
            cant_d = 0

    return palabras_d        
    
#Funcion principal
def main():
    #Contadores
    cfirst_l = 0

    #Paso 1, abrir el archivo
    archivo = open(ARCHIVO, "rt", encoding = "utf-8")
    
    #Paso 2, leer la linea 
    linea = archivo.readline()

    cfirst_l = fletter(linea)
    longitud = longvocal(linea)
    promedio = promchar(linea)
    palabras_d = expresion_d(linea)
    
    #Paso 
    archivo.close()

    return cfirst_l, longitud, promedio, palabras_d

r1, r2, r3, r4= main()
print(f"Primer resultado: {r1}")
print(f"Segundo resultado: {r2}")
print(f"Tercer resultado: {r3}")
print(f"Cuarto resultado: {r4}")




if __name__ == "__main__":
    main()