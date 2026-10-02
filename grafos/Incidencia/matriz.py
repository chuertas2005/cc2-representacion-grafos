class MatrizIncidencia:

    def __init__(self):
        self.vertices = []
        self.aristas = []

    # AGREGAR VÉRTICE
    def agregar(self, vertice):

        if vertice in self.vertices:
            print("El vértice ya existe.")
            return

        self.vertices.append(vertice)

        print("Vértice agregado correctamente.")

    # BORRAR VÉRTICE
    def borrar(self):

        if len(self.vertices) == 0:
            print("No hay vértices para borrar.")
            return

        print("\nVértices existentes:")

        for i, vertice in enumerate(self.vertices, 1):
            print(i, ".", vertice)

        opcion = int(input("Seleccione el vértice que desea borrar: "))

        if opcion < 1 or opcion > len(self.vertices):
            print("Opción inválida.")
            return

        posicion = opcion - 1
        vertice = self.vertices[posicion]

        # Buscar las aristas que contienen al vértice
        aristas_a_borrar = []

        for i, arista in enumerate(self.aristas):

            if posicion in arista:
                aristas_a_borrar.append(i)

        # Borrar las aristas
        for i in reversed(aristas_a_borrar):
            self.aristas.pop(i)

        # Ajustar los índices de los vértices restantes
        nuevas_aristas = []

        for v1, v2 in self.aristas:

            if v1 > posicion:
                v1 -= 1

            if v2 > posicion:
                v2 -= 1

            nuevas_aristas.append((v1, v2))

        self.aristas = nuevas_aristas

        # Borrar el vértice
        self.vertices.pop(posicion)

        print("Vértice", vertice, "borrado correctamente.")

    # AGREGAR / ELIMINAR CONEXIÓN
    def modificar(self):

        if len(self.vertices) < 2:
            print("Se necesitan al menos 2 vértices.")
            return

        print("\nVértices existentes:")

        for i, vertice in enumerate(self.vertices, 1):
            print(i, ".", vertice)

        origen = int(input("Seleccione el vértice de origen: "))
        destino = int(input("Seleccione el vértice de destino: "))

        # Validar origen
        if origen < 1 or origen > len(self.vertices):
            print("Origen inválido.")
            return

        # Validar destino
        if destino < 1 or destino > len(self.vertices):
            print("Destino inválido.")
            return

        # No permitir lazos
        if origen == destino:
            print("No se permiten conexiones de un vértice consigo mismo.")
            return

        i = origen - 1
        j = destino - 1

        # ==========================================
        # BUSCAR SI LA CONEXIÓN YA EXISTE
        # ==========================================

        posicion_arista = -1

        for posicion, (v1, v2) in enumerate(self.aristas):

            if (v1 == i and v2 == j) or (v1 == j and v2 == i):

                posicion_arista = posicion
                break

        # ==========================================
        # PREGUNTAR QUÉ HACER
        # ==========================================

        print("\n¿Qué desea hacer?")
        print("1. Agregar conexión")
        print("2. Eliminar conexión")

        opcion = input("Seleccione una opción: ")

        # ==========================================
        # AGREGAR CONEXIÓN
        # ==========================================

        if opcion == "1":

            if posicion_arista != -1:

                print("La conexión ya existe.")
                return

            # Agregar nueva arista
            self.aristas.append((i, j))

            print(
                "Conexión",
                self.vertices[i],
                "-",
                self.vertices[j],
                "agregada correctamente."
            )

        # ==========================================
        # ELIMINAR CONEXIÓN
        # ==========================================

        elif opcion == "2":

            if posicion_arista == -1:

                print("La conexión no existe.")
                return

            # Eliminar la arista
            self.aristas.pop(posicion_arista)

            print(
                "Conexión",
                self.vertices[i],
                "-",
                self.vertices[j],
                "eliminada correctamente."
            )

        else:

            print("Opción inválida.")

    # MOSTRAR MATRIZ
    def mostrar(self):

        if len(self.vertices) == 0:
            print("La matriz está vacía.")
            return

        print("\n===== MATRIZ DE INCIDENCIA =====")

        # Si no existen aristas
        if len(self.aristas) == 0:

            print("No hay aristas.")
            return

        # Encabezado de las aristas
        print("      ", end="")

        for i in range(len(self.aristas)):
            print("A" + str(i + 1), end="  ")

        print()

        # Filas de los vértices
        for i, vertice in enumerate(self.vertices):

            print(str(vertice) + "     ", end="")

            for v1, v2 in self.aristas:

                if i == v1 or i == v2:
                    print("1", end="   ")
                else:
                    print("0", end="   ")

            print()