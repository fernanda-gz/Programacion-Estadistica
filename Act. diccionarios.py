diccionario= {}
opcion = 0
while opcion != 5:
    print("--------Menu--------")
    print("1.-Agregar elemento ")
    print("2.- Modificar elemento")
    print("3.- Borrar elemento")
    print("4.- Mostrar diccionario")
    print("5.- Salir")
    opcion = int(input("Ingresa opcion: "))
    match opcion:
        case 1:
            print("---Agregar elemento---")
            dato = input("Ingresa dato 1: ")
            dato2 = input("Ingresa dato 2: ")
            diccionario[dato] = dato2
        case 2:
            print("---Modificar elemento---")
            print(diccionario)
            dato4 = input("Ingresa el dato que desea modificar: ")
            dato5 = input("Ingresa el dato nuevo: ")
            diccionario[dato4] = dato5
        case 3:
            print("---Borrar elemento---")
            print(diccionario)
            dato3 = input("Ingresa dato que desea eliminar: ")
            diccionario.pop(dato3)
        case 4:
            print("---Mostras diccionario---")
            print(diccionario)
        case 5:
            print("---Elegiste salir---")
        case _:
            print("*Opcion no valida*")



