#Area del cuadrado
def areaCuadrado():
    lado = float(input("Digite el lado del cuadrado: "))
    resultadoC = lado*lado
    print ("El area del cuadrado es: ",resultadoC)

#Area del rectangulo
def areaRectangulo():
    base = float(input("Digite la base del rectangulo: "))
    altura = float(input("Digite la altura del rectangulo: "))
    resultadoR = base * altura
    print ("El area del rectangulo es: ",resultadoR)

#Area del triangulo
def areaTriangulo():
    base = float(input("Digite la base del triangulo: "))
    altura = float(input("Digite la altura del triangulo: "))
    resultadoT = (base * altura) / 2
    print ("El area del triangulo es: ",resultadoT)

#Area del rombo
def areaRombo():
    diagonalMenor = float(input("Digite la diagonal MENOR del rombo: "))
    diagonalMayor = float(input("Digite la diagonal MAYOR del rombo: "))
    resultadoRom = (diagonalMayor * diagonalMenor) / 2
    print ("El area del rombo es: ",resultadoRom)


print ("Calculo de areas")
print ("1. Area del cuadrado")
print ("2. Area del rectangulo")
print ("3. Area del triangulo")
print ("4. Area del rombo")

opcion = input("Digite el numero de area que desea visualizar (1-4):")

if opcion == "1":
    areaCuadrado()
elif opcion == "2":
    areaRectangulo()
elif opcion == "3":
    areaTriangulo()
elif opcion == "4":
    areaRombo()
else:
    print ("Opcion no valida, verifique")