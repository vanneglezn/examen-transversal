# Categorías: Platinum, Gold, Silver
# Datos de las categorías: [stock, precio, ganancias]
entradas = [['Platinum', 2, 120000, 0], ['Gold', 4, 80000, 0], ['Silver', 10, 50000, 0]]

# Asientos es una lista de 100 elementos (1-100 para asientos disponibles, 'X' para asientos ocupados)
asientos = list(range(1,101))

# Lista de asistentes, cada asistente es una lista de tres elementos: [categoría, asiento, run]
asistentes = []

def menu():
    while True:
        print("\nMenu:\n1 Comprar entradas\n2 Mostrar ubicaciones\n3 Ver listado de asistentes\n4 Mostrar ganancias totales\n5 Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            comprar_entradas()
        elif opcion == '2':
            mostrar_ubicaciones()
        elif opcion == '3':
            ver_listado_asistentes()
        elif opcion == '4':
            mostrar_ganancias()
        elif opcion == '5':
            print("\nGracias por utilizar nuestros servicios. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del menú.")

def comprar_entradas():
    print("\nEntradas disponibles:")
    for i in range(len(entradas)):
        print(str(i+1) + '. ' + entradas[i][0] + ', ' + str(entradas[i][1]) + ', $' + str(entradas[i][2]))
    tipo_entrada = input("Seleccione la categoría de entradas: ")
    if not tipo_entrada.isdigit() or int(tipo_entrada) < 1 or int(tipo_entrada) > len(entradas):
        print("\nEntrada no válida. Inténtelo de nuevo.")
        return
    tipo_entrada = int(tipo_entrada) - 1
    run = input("Ingrese el RUN del asistente (sin dígito verificador): ")
    asiento = input("Seleccione el número de asiento (1-100): ")
    if not asiento.isdigit() or int(asiento) < 1 or int(asiento) > 100:
        print("\nNúmero de asiento no válido. Inténtelo de nuevo.")
        return
    asiento = int(asiento)
    if asientos[asiento-1] == 'X':
        print("\nLo sentimos, este asiento ya está ocupado. Inténtelo de nuevo.")
        return
    entradas[tipo_entrada][1] -= 1
    asientos[asiento-1] = 'X'
    asistentes.append([entradas[tipo_entrada][0], asiento, run])
    entradas[tipo_entrada][3] += entradas[tipo_entrada][2]
    print("\nHa comprado 1 entrada " + entradas[tipo_entrada][0] + ". ¡Disfrute del evento!")

def mostrar_ubicaciones():
    print("\nUbicaciones disponibles:")
    for j in range(0, 100, 10):
        for i in range(10):
            print(asientos[j+i], end=' ')
        print()


def ver_listado_asistentes():
    print("\nListado de asistentes:")
    for i in range(len(asistentes)):
        print("Categoría: " + asistentes[i][0] + ", Asiento: " + str(asistentes[i][1]) + ", RUN: " + asistentes[i][2])

def mostrar_ganancias():
    print("\nGanancias totales:")
    total = 0
    for i in range(len(entradas)):
        print(entradas[i][0] + ": $" + str(entradas[i][3]))
        total += entradas[i][3]
    print("Total: $" + str(total))

# Llamar a la función de menú para iniciar el programa
menu()
