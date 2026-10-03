from Adyacencia.matriz import MatrizAdyacencia
from Adyacencia.lista import ListaAdyacencia
from Incidencia.matriz import MatrizIncidencia
from Incidencia.lista import ListaIncidencia


matriz_adyacencia = MatrizAdyacencia()
lista_adyacencia = ListaAdyacencia()
matriz_incidencia = MatrizIncidencia()
lista_incidencia = ListaIncidencia()

vertices = ["A", "B", "C", "D"]

aristas = [
    ("A", "B", 5),
    ("A", "C", 10),
    ("B", "D", 3),
    ("C", "D", 7)
]

# ======================
# INICIALIZAR MATRICES
# ======================

for vertice in vertices:
    matriz_adyacencia.agregar(vertice)
    lista_adyacencia.agregar(vertice)
    matriz_incidencia.agregar(vertice)
    lista_incidencia.agregar(vertice)

for origen, destino, valor in aristas:

    i = matriz_adyacencia.vertices.index(origen)
    j = matriz_adyacencia.vertices.index(destino)
    matriz_adyacencia.matriz[i][j] = valor
    matriz_adyacencia.matriz[j][i] = valor

    lista_adyacencia.lista[origen].append((destino, valor))
    lista_adyacencia.lista[destino].append((origen, valor))

    i = matriz_incidencia.vertices.index(origen)
    j = matriz_incidencia.vertices.index(destino)
    matriz_incidencia.aristas.append((i, j, valor))

    lista_incidencia.contador_aristas += 1
    nombre_arista = "A" + str(lista_incidencia.contador_aristas)
    lista_incidencia.aristas[nombre_arista] = (
        origen,
        destino,
        valor
    )

    lista_incidencia.lista[origen].append(nombre_arista)
    lista_incidencia.lista[destino].append(nombre_arista)


while True:

    print("\n===================================")
    print("             MENÚ")
    print("===================================")
    print("1. Trabajar con matriz de adyacencia")
    print("2. Trabajar con lista de adyacencia")
    print("3. Trabajar con matriz de incidencia")
    print("4. Trabajar con lista de incidencia")
    print("5. Salir")
    print("===================================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        while True:

            print("\n===================================")
            print("       MATRIZ DE ADYACENCIA")
            print("===================================")
            print("1. Agregar vértice")
            print("2. Borrar vértice")
            print("3. Modificar conexión")
            print("4. Mostrar matriz")
            print("5. Volver al menú principal")
            print("===================================")

            opcion_matriz = input("Seleccione una opción: ")

            if opcion_matriz == "1":

                vertice = input("Ingrese el vértice: ")
                matriz_adyacencia.agregar(vertice)

            elif opcion_matriz == "2":

                matriz_adyacencia.borrar()

            elif opcion_matriz == "3":

                matriz_adyacencia.modificar()

            elif opcion_matriz == "4":

                matriz_adyacencia.mostrar()

            elif opcion_matriz == "5":

                break

            else:

                print("Opción inválida.")


    elif opcion == "2":

        while True:

            print("\n===================================")
            print("        LISTA DE ADYACENCIA")
            print("===================================")
            print("1. Agregar vértice")
            print("2. Borrar vértice")
            print("3. Modificar conexión")
            print("4. Mostrar lista")
            print("5. Volver al menú principal")
            print("===================================")

            opcion_lista = input("Seleccione una opción: ")

            if opcion_lista == "1":

                vertice = input("Ingrese el vértice: ")
                lista_adyacencia.agregar(vertice)

            elif opcion_lista == "2":

                lista_adyacencia.borrar()

            elif opcion_lista == "3":

                lista_adyacencia.modificar()

            elif opcion_lista == "4":

                lista_adyacencia.mostrar()

            elif opcion_lista == "5":

                break

            else:

                print("Opción inválida.")

    elif opcion == "3":

        while True:

            print("\n===================================")
            print("        MATRIZ DE INCIDENCIA")
            print("===================================")
            print("1. Agregar vértice")
            print("2. Borrar vértice")
            print("3. Modificar conexión")
            print("4. Mostrar matriz")
            print("5. Volver al menú principal")
            print("===================================")

            opcion_incidencia = input("Seleccione una opción: ")

            if opcion_incidencia == "1":

                vertice = input("Ingrese el vértice: ")
                matriz_incidencia.agregar(vertice)

            elif opcion_incidencia == "2":

                matriz_incidencia.borrar()

            elif opcion_incidencia == "3":

                matriz_incidencia.modificar()

            elif opcion_incidencia == "4":

                matriz_incidencia.mostrar()

            elif opcion_incidencia == "5":

                break

            else:

                print("Opción inválida.")

    elif opcion == "4":

        while True:

            print("\n===================================")
            print("         LISTA DE INCIDENCIA")
            print("===================================")
            print("1. Agregar vértice")
            print("2. Borrar vértice")
            print("3. Modificar conexión")
            print("4. Mostrar lista")
            print("5. Volver al menú principal")
            print("===================================")

            opcion_lista_incidencia = input("Seleccione una opción: ")

            if opcion_lista_incidencia == "1":

                vertice = input("Ingrese el vértice: ")
                lista_incidencia.agregar(vertice)

            elif opcion_lista_incidencia == "2":

                lista_incidencia.borrar()

            elif opcion_lista_incidencia == "3":

                lista_incidencia.modificar()

            elif opcion_lista_incidencia == "4":

                lista_incidencia.mostrar()

            elif opcion_lista_incidencia == "5":

                break

            else:

                print("Opción inválida.")

    elif opcion == "5":

        print("\nPrograma terminado.")
        break

    else:

        print("\nOpción inválida.")
