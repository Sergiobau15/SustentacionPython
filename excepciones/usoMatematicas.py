import matematicas

def main():
    try:
        # Pedir al usuario que ingrese dos números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        # Uso de las funciones del módulo matematicas
        print(f"Suma de {num1} y {num2}: {matematicas.suma(num1, num2)}")
        print(f"Resta de {num1} y {num2}: {matematicas.resta(num1, num2)}")
        print(f"Multiplicación de {num1} y {num2}: {matematicas.multiplicacion(num1, num2)}")
        try:
            print(f"División de {num1} entre {num2}: {matematicas.division(num1, num2)}")
        except ValueError as e:
            print(e)
    
    except ValueError:
        print("Error: Ingrese números válidos.")


main()