miLista = [1,2,3]
opcion = 0
while opcion != 4:
    print("--------Menu--------")
    print("1.-Agregar elemento ")
    print("2.- Borrar elemento")
    print("3.- Mostrar lista")
    print("4.- Salir")
    opcion = int(input("Ingresa opcion: "))
    match opcion:
        case 1:
            print("---Agregar elemento---")
            dato = int(input("Ingresa nuevo dato: "))
            miLista.append(dato)

        case 2:
            print("---Borrar elemento---")
            con=0
            for i in miLista:
                print("la posicion de: ", i,"es ",con)
                con=con+1
            pos= int(input("Ingresa posicion: "))
            elemento = miLista.pop(pos)
            print("Saque: ", elemento)
        case 3:
            print("---Mostrar lista")
            print(miLista)

        case 4:
            print("Elegiste salir")

        case _:
            print("Elegiste una opción no valida")