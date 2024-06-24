def agregar_una_vez(lista, el):
    if el in lista:
        raise ValueError(f"El elemento '{el}' ya está en la lista")
    else:
        lista.append(el)

#Lista
mi_lista = [10, 2, 35]

# Mostrar la lista inicial
print(f"Lista inicial: {mi_lista}")

# Preguntar al usuario si desea añadir un elemento
try:
    elemento = input("Introduce un elemento para añadir a la lista: ")
    elemento = int(elemento)  # Convertir la entrada a entero
    agregar_una_vez(mi_lista, elemento)
    print(f"Lista actualizada: {mi_lista}")
except ValueError as e:
    print(f"Ingrese valores enteros, verifique {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Este bloque se ejecutará siempre, después del try/except
    print("Gracias por usar este programa")
