print("Bienvenido a ... ")
print("""  __________________________     
        .__                        
  _____ |__| _____  ______ ______  
 /     \|  | \__  \ \____ \\____ \ 
|  Y Y  \  |  / __ \|  |_> >  |_> >
|__|_|  /__| (____  /   __/|   __/ 
      \/          \/|__|   |__|   

""")

nombre = input("Para empezar, dime cómo te llamas: ")
print()
print(f"Hola {nombre}, bienvenido a mi app")
print()

edad = int(input("Dime cuántos años tienes? "))
print()

estatura = float(input("Dime cuál es tu estatura en metros (sólo número)? "))
estatura_m = int(estatura)
estatura_cm = int(estatura*100)

num_amigos =  int(input("Ahora cuéntame ¿Cuántos amigos tienes? "))
print()

ciudad = input("¿En qué ciudad vives? ")

print(f"Muy bien, {nombre}. Entonces podemos crear un perfil con estos datos.")
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
continuar = True
while continuar:
    escribir_mensaje = input("Deseas escribir un mensaje (S/N): ")
    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    #En caso que sea otra respuesta, vamos a decidir salir.
    elif escribir_mensaje == "N" or escribir_mensaje == "n":
        continuar = False

print("Gracias por usar Mi Red. Â¡Hasta pronto!")