#Funcion del cuadrado-----------------------------------------------
def cuadrado():
    numero = int(input("Digite el numero del tamaño que desea del cuadrado: "))
    for i in range(1,numero+1): #este ciclo sirve para recorrer las columnas del cuadrado, al no ponerlo no se pone la ultima fila
        for j in range(1,numero+1): #este ciclo es el encargado de reccorer las filas del cuadrado
            if i == 1 or i == numero:
                print(" * ", end="") #el end sirve para que se imprima el asterisco sin saltar de linea en la fila
            else:
                if j == 1 or j == numero:
                    print (" * ", end="")
                else:
                    print ("   ",end="")
        print("")


#Funcion del rectangulo-----------------------------------------------
def rectangulo():
    base = int(input("Digite la base del rectangulo: "))
    altura = int(input("Digite la altura del rectangulo: "))
    if altura!=base: #se condiciona de que no pueden ser numeros iguales, ya que el rectangulo debe tener numeros diferentes
        for i in range (1,altura+1): #se hace un bucle con el fin de representar la altura
            for j in range (1, base+1): #se hace un bucle con el fin de representar la base
                print (" * ",end="")
            print (" ")
    else:
        print ("Para hacer un rectangulo debes digitar una base o una altura mayor que la otra")


#Funcion del triangulo-----------------------------------------------
def triangulo():
    num = int(input("Introduzca el numero de renglones del triangulo que desea visualizar: "))
    for i in range (num+1): #el ciclo for se detiene un numero antes, por eso se pone +1
        espacios=num-i
        print(" "*espacios+"* "*i) #es importante el espacio en el asterisco para que se forme el triangulo completo


#Funcion del rombo-----------------------------------------------
def rombo():
    num = int(input("Introduzca el numero de renglones del rombo: "))
    for i in range (num+1): #el ciclo for se detiene un numero antes, por eso se pone +1
        espacios=num-i
        print(" "*espacios+"* "*i)

    for i in range (num-1,0,-1):
        espacios=num-i
        print(" "*espacios+"* "*i)


print ("Figuras en pantalla")
print ("1. Cuadrado")
print ("2. Rectangulo")
print ("3. Triangulo")
print ("4. Rombo")

opcion = input ("Ingresa el numero de figura que deseas visualizar (1-4): ")
if opcion == "1":
    cuadrado()
elif opcion == "2":
    rectangulo()
elif opcion == "3":
    triangulo()
elif opcion == "4":
    rombo()
else:
    print ("Opcion no valida, verifique")