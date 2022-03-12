# Primer reto
Crea una función que pueda sumar 2 números enteros.

## Prototipo de función:
int sumar(int x, int y);
Donde,
- x es el primer número entero.
- y es el segundo número entero.

## Valor que regresa
La suma de los números enteros de arriba

## Prueba de entrada
x = 2
y = 3

## Prueba de salida
5

## Explicación
La suma de los 2 números enteros x & z se calcula como 2+3=5

##Programa de dulcecallejas
#Definicion de la funcion que suma 2 numeros enteros
def Suma2Enteros (x,y):
  z = x + y 
  return z

# Estructura del menú y las entradas al programa
while True:
  print ("¿Quieres jugar a sumar dos números?")  
  print ("1 Si")
  print ("2 No")
  opcion = int(input("Introduce la opcion==>"))

  if opcion == 1: 
    x = int(input("Escribe el valor del primer número entero==>"))
    y = int(input("Escribe el valor del segundo número entero==>"))
    z = Suma2Enteros(x,y)
    print (x, " + ", y, " = ", z)

  elif opcion == 2:
    print ("Bye")
    break
  else:
    print("Opción incorrecta")
  
