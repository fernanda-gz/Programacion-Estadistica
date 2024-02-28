opcion =0
def grados(a):
    g = a *(9/5)+ 32
    return g
def posnig(a):
    if a<0:
        return "El numero es negativo"
    else:
        return "El numero es positivo"

def poi(a):
    if a%2 == 0:
        return "El numero es par"
    else:
        return "El numero es impar"

def suma(a,b,c,d,e):
    s = a+b+c+d+e
    return s
def numal(a):
    if a==1:
        return "Uno"
    if a==2:
        return "Dos"
    if a==3:
        return "Tres"
    if a==4:
        return "Cuatro"
    if a==5:
        return "Cinco"
    if a==6:
        return "Seis"
    if a==7:
        return "Siete"
    if a==8:
        return "Ocho"
    if a==9:
        return "Nueve"
    if a==10:
        return "Diez"
    if a>10:
        return "Error solo se puede del 1 al 10"
    if a<0:
        return "Error solo se puede del 1 al 10 no se puede numero negativo"
    if a==0:
        return "El cero no es valido"
while opcion != 6:
    print("--------Menu--------")
    print("1.-Convertidor de Centigrados a fahrenheit ")
    print("2.- Positivo o Negativo")
    print("3.- Par o Impar")
    print("4.- De numero a texto")
    print("5.- Suma de 5 numeros")
    print("6.- Salir")
    opcion = int(input("Ingresa opcion: "))
    match opcion:
        case 1:
            z= int(input("Dame los grados: "))
            g= grados(z)
            print("Son ", g ,"grados Fahrenheit")
        case 2:
            nop=int(input("Dame el numero: "))
            c=posnig(nop)
            print(c)
        case 3:
            p=int(input("Ingresa el numero: "))
            a=poi(p)
            print(a)
        case 4:
            z=int(input("Ingresa numero: "))
            x=numal(z)
            print(x)
        case 5:
            a = int(input("Ingresa numero 1: "))
            b = int(input("Ingresa numero 2: "))
            c = int(input("Ingresa numero 3: "))
            d = int(input("Ingresa numero 4: "))
            e = int(input("Ingresa numero 5: "))
            s= suma(a,b,c,d,e)
            print("La suma es ",s)
        case 6:
            print("Elegiste salir")
        case _:
            print("Opcion no valida")



