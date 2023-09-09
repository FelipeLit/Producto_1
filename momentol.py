equipos = {}

def agregarEquipo ():
    nombre = input("Nombre del equipo: ")
    copas = int(input("Copas ganadas: "))
    localidad = input ("Donde juega el equipo: ")
    
    equipos [nombre] = {"copas": copas, "localidad": localidad}
    print (f"El nombre del equipo es {nombre} cantidad de copas ganadas {copas} y su localidad es en {localidad}")
    
def buscar():
    nombre = input("Ingrese el nombre del equipo que desea buscar: ")
    equipo_info = equipos.get(nombre)
    if equipo_info:
        print(f"Nombre del equipo: {nombre}")
        print(f"Copas: {equipo_info['copas']}")
        print(f"Su localidad es: {equipo_info['localidad']}")
    else:
        print(f"El equipo '{nombre}' no fue encontrado en la base de datos.")


def Actualizar ():
    nombre = input("Ingrese el nombre del equipo que desea actualizar: ")
    if nombre in equipos:
        print(f"Equipo encontrado: {nombre}")
        nueva_copas = int(input("Nuevo número de copas ganadas: "))
        nueva_localidad = input("Nueva localidad del equipo: ")
        equipos[nombre]['copas'] = nueva_copas
        equipos[nombre]['localidad'] = nueva_localidad
    else:
        print(f"El equipo '{nombre}' no fue encontrado en la base de datos.")
        
def Eliminar ():
    nombre = input ("Nombre del equipo que desea eliminar: ")
    if nombre in equipos:
        del equipos[nombre]
        print (f"El equipo {nombre} ha sido eliminado")
        
while True:
    print("\nMenu")
    print("1. Agregar")
    print("2. Buscar")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")  # Agrega la opción para salir

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregarEquipo()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        Actualizar()
    elif opcion == "4":
        Eliminar()
    elif opcion == "5":
        print("Saliendo del programa.")
        break 
    else:
        print("Número incorrecto")

    





    
    
    
    