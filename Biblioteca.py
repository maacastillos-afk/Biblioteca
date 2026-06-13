stock = 120
historial = 0

while True:
    print("===MENÚ PRINCIPAL===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("Libros disponibles:", stock)
    elif opcion == "2":
        while True:
            try:
                cantidad = int(input("Cantidad de libros a prestar: "))
                if cantidad > 0 and cantidad <= stock:
                    stock -= cantidad
                    historial += cantidad
                    break
                else:
                    print("Cantidad inválida. Debe ser mayor a 0 y no superar el stock disponible.")
            except:
                print("Entrada inválida. Ingresa un número entero positivo.")
    elif opcion == "3":
        while True:
            try:
                cantidad = int(input("Cantidad de libros a devolver: "))
                if cantidad > 0 and stock + cantidad <= 120:
                    stock += cantidad
                    historial -= cantidad
                    break
                else:
                    print("Cantidad inválida. Debe ser mayor a 0 y no superar la capacidad máxima de la biblioteca.")
            except:
                print("Entrada inválida. Ingresa un número entero positivo.")
    elif opcion == "4":
        print("Historial de préstamos activos:", historial)
    elif opcion == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")
