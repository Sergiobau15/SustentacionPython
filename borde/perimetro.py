#Perimetro del cuadrado
def perimetroCuadrado():
    lado = float(input("Digite un lado del cuadrado: "))
    resultadoC = lado*4
    print ("El perimetro del cuadrado es: ",resultadoC)

#Perimetro del rectangulo
def perimetroRectangulo():
    base = float(input("Digite la base del rectangulo: "))
    altura = float(input("Digite la altura del rectangulo: "))
    resultadoR = (base*2) + (altura*2)
    print ("El perimetro del rectangulo es: ",resultadoR)

#Perimetro del triangulo
def perimetroTriangulo():
    base = float(input("Digite la base del triangulo: "))
    altura = float(input("Digite la altura del triangulo: "))
    resultadoT = base + (altura*2)
    print ("El perimetro del triangulo es: ",resultadoT)

#Perimetro del rombo
def perimetroRombo():
    ladoRombo = float(input("Digite un lado del rombo: "))
    resultadoRom = ladoRombo*4
    print ("El perimetro del rombo es: ",resultadoRom)


print ("Calculo de perimetros")
print ("1. Perimetro del cuadrado")
print ("2. Perimetro del rectangulo")
print ("3. Perimetro del triangulo")
print ("4. Perimetro del rombo")

opcion = input("Digite el numero de perimetro que desea visualizar (1-4):")

if opcion == "1":
    perimetroCuadrado()
elif opcion == "2":
    perimetroRectangulo()
elif opcion == "3":
    perimetroTriangulo()
elif opcion == "4":
    perimetroRombo()
else:
    print ("Opcion no valida, verifique")