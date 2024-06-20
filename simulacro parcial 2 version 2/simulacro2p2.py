ARCHIVO = "entrada.txt"

#1
def long_par(linea):

    vocales = "aeiou"
    consonantes = "qwrtypsdfghjklñzxcvbnm"

    #Contadores
    validas = 0
    long = 0
    cont_vocales = 0
    cont_consonantes = 0

    for l in linea:

        if l != " " and l != ".":
            #Cantidad de caracteres
            long += 1

            #Si la letra es vocal
            if l.lower() in vocales:
                cont_vocales += 1

            #Si la letra es consonante
            if l.lower() in consonantes:
                cont_consonantes += 1

        else:
            #Si es valida suma uno
            if long % 2 == 0 and (cont_consonantes == cont_vocales):
                validas += 1

            #Reseteo contadores
            long = 0
            cont_vocales = 0
            cont_consonantes = 0

    return validas

#2
def long_p_long(linea):

    digitos = "0123456789"

    #Flags
    digito = False
    letter_p = False

    #Contadores
    chars = 0
    long = None

    for l in linea:
        if l != " " and l != ".":
            #Sumamos todas las letras dentro de la palabra
            chars += 1

            if l in digitos:
                digito = True

            if l.lower() == "p":
                letter_p = True


        else:
            if digito and not letter_p:
                if long == None or  chars > long:
                    long = chars

            digito = False
            letter_p = False
            chars = 0

    return long




    
    pass

#3
def prom_entero(linea):

    #Flags
    letter_s = False

    #Contadores
    validas = 0
    chars = 0
    sum_letter = 0

    for l in linea:

        if l != " " and l != ".":
            chars += 1
            if l.lower() == "s":
                letter_s = True

                
        else:
            if chars > 2 and letter_s:
                validas += 1
                sum_letter += chars
            #Reseteo
            letter_s = False
            chars = 0

    promedio = sum_letter // validas

    return promedio

#4
def expresion_ra(linea):

    vocales = "aeiou"

    #Flags
    letra_r = False
    vocal = False
    ra = False
    
    #Contadores
    char = 0
    total = 0

    for l in linea:

        if l != " " and l != ".":
            #Sumamos siempre un caracter para comprobar la vocal en los primeros 2
            char += 1

            #Si la letra es vocal y esta en el caracter 1 o 2 vocal True
            if l.lower() in vocales and (0 < char < 3):
                vocal = True

            #Si la letra es r, levantamos flag de r
            if l.lower() == "r":
                letra_r = True
            
            #Si ya paso por r y ahora es a, levantamos flag ra, sino reseteamos r
            elif l.lower() == "a":
                if letra_r:
                    ra = True
                else:
                    letra_r = False 

        else:
            #Si ra es true y vocal tambien, sumamos una palabra
            if ra and vocal:
                total += 1 
            #Reseteo
            letra_r = False
            ra = False
            vocal = False
            char = 0
            
    return total


def main():

    archivo = open(ARCHIVO, "rt", encoding="utf-8")

    linea = archivo.readline()

    long = long_par(linea)
    longp = long_p_long(linea)
    promedio = prom_entero(linea)
    expr_ra = expresion_ra(linea)


    archivo.close()

    return long, longp, promedio, expr_ra

long, longp, promedio, expr_ra = main()

print(f"Primer resultado: {long}")
print(f"Segundo resultado {longp}")
print(f"Tercer resultado: {promedio}")
print(f"Cuarto resultado {expr_ra}")

if __name__ == "__main__":
    main()