class ListaIncidencia:

    def __init__(self):
        # Diccionario de vértices.
        # Cada vértice contiene una lista de aristas.
        self.lista = {}

        # Diccionario de aristas.
        # Cada arista guarda los dos vértices que conecta.
        self.aristas = {}

        # Contador para identificar las aristas
        self.contador_aristas = 0

    # AGREGAR VÉRTICE
    def agregar(self, vertice):

        if vertice in self.lista:
            print("El vértice ya existe.")
            return

        self.lista[vertice] = []

        print("Vértice agregado correctamente.")

    # BORRAR VÉRTICE
    def borrar(self):

        if len(self.lista) == 0:
            print("No hay vértices para borrar.")
            return

        vertices = list(self.lista.keys())

        print("\nVértices existentes:")

        for i, vertice in enumerate(vertices, 1):
            print(i, ".", vertice)

        opcion = int(input("Seleccione el vértice que desea borrar: "))

        if opcion < 1 or opcion > len(vertices):
            print("Opción inválida.")
            return

        vertice = vertices[opcion - 1]

        # Buscar las aristas que pertenecen al vértice
        aristas_a_borrar = []

        for arista, extremos in self.aristas.items():

            if vertice in extremos:
                aristas_a_borrar.append(arista)

        # Eliminar las aristas
        for arista in aristas_a_borrar:

            v1, v2 = self.aristas[arista]

            # Eliminar la arista de los dos vértices
            if arista in self.lista[v1]:
                self.lista[v1].remove(arista)

            if arista in self.lista[v2]:
                self.lista[v2].remove(arista)

            # Eliminar la arista del diccionario
            del self.aristas[arista]

        # Eliminar el vértice
        del self.lista[vertice]

        print("Vértice", vertice, "borrado correctamente.")

    # MODIFICAR CONEXIÓN
    def modificar(self):

        if len(self.lista) < 2:
            print("Se necesitan al menos 2 vértices.")
            return

        vertices = list(self.lista.keys())

        print("\nVértices existentes:")

        for i, vertice in enumerate(vertices, 1):
            print(i, ".", vertice)

        origen = int(input("Seleccione el vértice de origen: "))
        destino = int(input("Seleccione el vértice de destino: "))

        if origen < 1 or origen > len(vertices):
            print("Origen inválido.")
            return

        if destino < 1 or destino > len(vertices):
            print("Destino inválido.")
            return

        if origen == destino:
            print("No se permiten conexiones de un vértice consigo mismo.")
            return

        origen = vertices[origen - 1]
        destino = vertices[destino - 1]

        valor = int(input("Ingrese 1 para conectar o 0 para desconectar: "))

        if valor != 0 and valor != 1:
            print("El valor debe ser 0 o 1.")
            return

        # ==========================================
        # CONECTAR
        # ==========================================

        if valor == 1:

            # Comprobar si ya existe la conexión
            for arista, extremos in self.aristas.items():

                v1, v2 = extremos

                if (v1 == origen and v2 == destino) or \
                (v1 == destino and v2 == origen):

                    print("La conexión ya existe.")
                    return

            # Crear nueva arista
            self.contador_aristas += 1

            arista = "A" + str(self.contador_aristas)

            # Guardar la conexión
            self.aristas[arista] = (origen, destino)

            # Agregar la arista a ambos vértices
            self.lista[origen].append(arista)
            self.lista[destino].append(arista)

            print("Conexión", arista, "agregada correctamente.")

        # ==========================================
        # DESCONECTAR
        # ==========================================

        elif valor == 0:

            arista_encontrada = None

            # Buscar la arista
            for arista, extremos in self.aristas.items():

                v1, v2 = extremos

                if (v1 == origen and v2 == destino) or \
                (v1 == destino and v2 == origen):

                    arista_encontrada = arista
                    break

            if arista_encontrada is None:

                print("La conexión no existe.")
                return

            # Eliminar la arista de los vértices
            if arista_encontrada in self.lista[origen]:
                self.lista[origen].remove(arista_encontrada)

            if arista_encontrada in self.lista[destino]:
                self.lista[destino].remove(arista_encontrada)

            # Eliminar la arista
            del self.aristas[arista_encontrada]

            print("Conexión", arista_encontrada, "eliminada correctamente.")

    # MOSTRAR LISTA
    def mostrar(self):

        if len(self.lista) == 0:
            print("La lista está vacía.")
            return

        print("\n===== LISTA DE INCIDENCIA =====")

        # Mostrar las aristas
        if len(self.aristas) > 0:

            print("\nAristas:")

            for arista, extremos in self.aristas.items():

                print(arista, "->", extremos)

        else:

            print("\nNo hay aristas.")

        # Mostrar incidencia de cada vértice
        print("\nIncidencia:")

        for vertice in self.lista:

            print(vertice, "->", self.lista[vertice])
