opcion=0
while opcion != 7:
    print("---------------------" )
    print("--------Menu--------")
    print("----------------------")
    print("1. test")
    print("2. Clientes")
    print("3. Productos")
    print("4. Sample")
    print("5. Town")
    print("6. train")
    print("7. Salir")
    print("-------------------------")
    opcion = int(input("Ingresa opcion: "))
    match opcion:
      case 1:
          import pandas as pd
          df = pd.read_csv("test.csv")
          print(df)
      case 2:
          import pandas as pd
          df = pd.read_csv("cliente_tabla.csv")
          print(df)
      case 3:
          import pandas as pd
          df = pd.read_csv("producto_tabla.csv")
          print(df)
      case 4:
          import pandas as pd
          df = pd.read_csv("sample_submission.csv")
          print(df)
      case 5:
          import pandas as pd
          df = pd.read_csv("town_state.csv")
          print(df)
      case 6:
          import pandas as pd
          df = pd.read_csv("train.csv")
          print(df)
      case 7:
          import pandas as pd
          print("Elegiste salir")
      case _:
        print("error:Opción no válida.")
