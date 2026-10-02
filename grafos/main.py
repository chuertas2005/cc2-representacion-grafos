
from Adyacencia.matriz import MatrizAdyacencia
from Adyacencia.lista import ListaAdyacencia
from Incidencia.matriz import MatrizIncidencia
from Incidencia.lista import ListaIncidencia

# ==========================================
# CREAR LAS CUATRO REPRESENTACIONES
# ==========================================

matriz_adyacencia = MatrizAdyacencia()
lista_adyacencia = ListaAdyacencia()
matriz_incidencia = MatrizIncidencia()
lista_incidencia = ListaIncidencia()

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

    # ==========================================
    # 1. MATRIZ DE ADYACENCIA
    # ==========================================

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

    # ==========================================
    # 2. LISTA DE ADYACENCIA
    # ==========================================

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

    # ==========================================
    # 3. MATRIZ DE INCIDENCIA
    # ==========================================

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

    # ==========================================
    # 4. LISTA DE INCIDENCIA
    # ==========================================

    elif opcion == "4":

        while True:

            print("\n===================================")
            print("         LISTA DE INCIDENCIA")
            print("===================================")
            print("1. Agregar vértice")
            print("2. Borrar vértice")
            print("3. Agregar conexión")
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

    # ==========================================
    # 5. SALIR
    # ==========================================

    elif opcion == "5":

        print("\nPrograma terminado.")
        break

    else:

        print("\nOpción inválida.")
