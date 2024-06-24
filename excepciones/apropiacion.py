lista = [3,5,6,8]
try:
    pos = int(input("ingrese la posición del elemento que desea obtener:"))
    print(f"El valor en la posicion {pos} es {lista[pos]}")

except ValueError:
    print("La posición ingresada no es válida,verifique")
except:
    print("La posición no existe")
