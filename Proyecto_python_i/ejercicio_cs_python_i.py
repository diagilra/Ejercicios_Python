def msj_bienvenida():
    print("Bienvenido a ... ")
    print("""  __________________________     
            .__                        
    _____ |__| _____  ______ ______  
    /     \|  | \__  \ \____ \\____ \ 
    |  Y Y  \  |  / __ \|  |_> >  |_> >
    |__|_|  /__| (____  /   __/|   __/ 
        \/          \/|__|   |__|   

    """)

def ingresar_nombre():
    nombre = input("Para empezar, dime cómo te llamas: ")
    print()
    print(f"Hola {nombre}, bienvenido a mi app")
    print()
    return nombre

def ingresar_edad():
    edad = int(input("Dime cuántos años tienes? "))
    return edad

def ingresar_estatura():
    estatura = float(input("Dime cuál es tu estatura en metros (sólo número)? "))
    estatura_m = int(estatura)
    estatura_cm = int(estatura*100)
    return (estatura_m, estatura_cm)

def ingresar_num_amigos():
    num_amigos =  int(input("Ahora cuéntame ¿Cuántos amigos tienes? "))
    return num_amigos

def ingresar_ciudad():
    ciudad = input("¿En qué ciudad vives? ")
    return ciudad

def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, ciudad):
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centí­metros")
    print("Amigos:  ", num_amigos)
    print("Ciudad:  ", ciudad)
    print("--------------------------------------------------")
    print("Gracias por la información. Esperamos que disfrutes con Mi App")
    print()


# Escribir mensajes continuamente
def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion

def ingresar_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")

# Desde aquí comienza el programa principal
msj_bienvenida()
nombre = ingresar_nombre()
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()
edad = ingresar_edad()
(estatura_m, estatura_cm) = ingresar_estatura()
num_amigos = ingresar_num_amigos()
ciudad = ingresar_ciudad()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, ciudad)
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con Mi App")
print("--------------------------------------------------")

# Ingresamos al ciclo que permite ejecutar acciones
opcion = 1
while opcion != 0:
    # Mostramos el menu
    opcion = opcion_menu()

    #Código para la opción 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = ingresar_mensaje()
        mostrar_mensaje(nombre, None, mensaje)

    #Código para la opción 2. Publicar un mensaje a un grupo de personas.
    elif opcion == 2:
        mensaje = ingresar_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            mostrar_mensaje(nombre, nombre_amigo, mensaje)

    #Código para la opción 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, ciudad)

    #Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        nombre = ingresar_nombre()
        edad = ingresar_edad()
        (estatura_m, estatura_cm) = ingresar_estatura()
        num_amigos = ingresar_num_amigos()
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, ciudad)
    elif opcion == 0:
        print("Has decidido salir.")

print("Gracias por usar Mi App. ¡Hasta pronto!")
