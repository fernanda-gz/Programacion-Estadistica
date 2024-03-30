manteles = {}
mobiliario={}
silla = {}
mesa = {}
def agregar_mantel(color, cantidad):
  if color not in manteles:
    manteles[color] = 0
  manteles[color] += cantidad

def agregar_silla(forma, cantidad):
  if material not in silla:
    silla[material] = 0
  silla[material] += cantidad

def agregar_mesa(forma, cantidad):
  if material not in mesa:
    mesa[material] = 0
  mesa[material] += cantidad

def mostrar_inventario():
  print("--------------------------" )
  print("Inventario de Manteles")
  print("--------------------------" )
  for color, cantidad in manteles.items():
    print(f"Color: {color}, Cantidad: {cantidad}")

  print("--------------------------" )
  print("Inventario de Mobiliario")
  print("***** Sillas *****")
  for tipo, cantidad in silla.items():
        print(f"    tipo: {material}, Cantidad: {cantidad}")
  print("***** Mesas *****")
  for tipo, cantidad in mesa.items():
        print(f"    tipo: {tipo}, Cantidad: {cantidad}")

def eliminar_mantel(color, cantidad_a_eliminar):
  if color in manteles and cantidad_a_eliminar <= manteles[color]:
    manteles[color] -= cantidad_a_eliminar
    if manteles[color] == 0:
      del manteles[color]
    print(f"Se eliminaron {cantidad_a_eliminar} manteles de color '{color}' del inventario.")
  else:
    if cantidad_a_eliminar > manteles[color]:
      print(f"La cantidad a eliminar ({cantidad_a_eliminar}) supera la cantidad disponible ({manteles[color]}).")
    else:
      print(f"El mantel de color '{color}' no existe en el inventario.")

def eliminar_silla(tipo_a_eliminar, cantidad_a_eliminar):
  if material in silla and cantidad <= silla[material]:
    silla[material] -= cantidad
    if silla[material] == 0:
      del silla[material]
    print(f"Se eliminaron {cantidad} de sillas de  '{material}' del inventario.")
  else:
    if cantidad > silla[material]:
      print(f"La cantidad a eliminar ({cantidad}) supera la cantidad disponible ({silla[material]}).")
    else:
      print(f"El mantel de color '{material}' no existe en el inventario.")
def mostrar_menu():
  print("--------------------------" )
  print("1. Agregar")
  print("2. Mostrar inventario")
  print("3. Eliminar")
  print("4. Salir")
  print("**************************" )

while True:
  mostrar_menu()

  opcion = int(input("Ingrese una opción: "))

  if opcion == 1:
    # Agregar un nuevo elemento al inventario
    tipo_elemento = input("¿Qué desea agregar (mantel o mueble)? ").lower()
    if tipo_elemento == "mantel":
      color = input("Ingrese el color del mantel: ")
      cantidad = int(input("Ingrese la cantidad a agregar: "))
      agregar_mantel(color, cantidad)
    else:
      tipo = input("Ingrese el tipo (silla o mesa): ")
      if tipo == "silla":
        material = input("Ingrese el material de la silla (madera, plástico, hierro): ")
        cantidad = int(input("Ingrese la cantidad de sillas a agregar: "))
        agregar_silla(material, cantidad)
      else:
        forma = input("Ingrese la forma de la mesa (redonda, cuadrada): ")
        cantidad = int(input("Ingrese la cantidad de mesas a agregar: "))
        agregar_mesa(forma, cantidad)
  elif opcion == 2:
    mostrar_inventario()
  elif opcion == 3:
        elemento_a_eliminar = input("¿Qué desea eliminar (mantel, mueble)? ")
        if elemento_a_eliminar == "mantel":
            color_a_eliminar = input("Ingrese el color del mantel a eliminar: ")
            cantidad_a_eliminar = int(input("Ingrese la cantidad a eliminar: "))
            eliminar_mantel(color_a_eliminar, cantidad_a_eliminar)
        elif elemento_a_eliminar == "mueble":
          tipo_a_eliminar = input("Ingrese que tipo de mueble (silla o mesa): ")
          if tipo_a_eliminar == "silla":
            material = input("Ingrese el tipo de silla (madera, plástico, hierro): ")
            cantidad = int(input("Ingrese la cantidad a eliminar: "))
            eliminar_silla(material, cantidad)
          elif elemento_a_eliminar == "mesa":
            tipo_a_eliminar = input("Ingrese la forma del mueble a eliminar (redonda, cuadrada): ")
            cantidad_a_eliminar = int(input("Ingrese la cantidad a eliminar: "))
            eliminar_mesa(tipo_a_eliminar,cantidad_a_eliminar)
        else:
            print("Tipo de elemento inválido.")

