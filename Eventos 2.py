opcion=0
while opcion != 7:
    print("---------------------" )
    print("--------Menu--------")
    print("----------------------")
    print("1. Imprimir todo")
    print("2. Ganancia maxima")
    print("3. Ganancia minima")
    print("4. Año")
    print("5. Descripcion general de ganancias")
    print("6. Ganancias mayor a")
    print("7. Salir")
    print("-------------------------")
    opcion = int(input("Ingresa opcion: "))
    match opcion:
      case 1:
          import pandas as pd
          df = pd.read_excel("Eventos.xlsx")
          print(df)
      case 2:
          import pandas as pd
          df = pd.read_excel("Eventos.xlsx")
          daf=(df['Ganancia'].max())
          print("La ganancia maxima que se a obtenido es de ", daf)
      case 3:
          import pandas as pd
          df = pd.read_excel("Eventos.xlsx")
          daf=(df['Ganancia'].min())
          print("La ganancia minima que se a obtenido es de ", daf)
      case 4:
          import pandas as pd
          df = pd.read_excel("Eventos.xlsx")
          a= int(input("Ingrese el año (2020 a 2024): "))
          print (df[df["Año de evento"]==a])
      case 5:
          import pandas as pd
          df = pd.read_excel("Eventos.xlsx")
          print(df["Ganancia"]. describe())
      case 6:
          import pandas as pd
          df = pd.read_excel("Eventos.xlsx")
          a= int(input("Ingrese la cantidad : "))
          print (df[df["Ganancia"]>=a])
      case 7:
          print("Elegiste salir")
      case _:
        print("error:Opción no válida.")
