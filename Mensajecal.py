print("ESTRUCTURA DE SELECCION")
cal=float(input("Dame una calificacion: "))
if cal==100:
    print("Excelente")
elif cal>=90 and cal <= 99.9 :
    print("Muy bien")
elif cal >= 70 and cal <= 89.9:
    print("Bien")
elif cal >= 60 and cal <= 69.9:
    print("Regular")
elif cal>=0 and cal<60:
    print("Reprobado")
else:
    print("Calificacion erronea")