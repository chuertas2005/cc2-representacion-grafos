class ListaIncidencia:

    def __init__(self):

        # Diccionario de vértices.
        # Cada vértice contiene una lista de aristas
        # en las que participa.
        self.lista = {}

        # Diccionario de aristas.
        # Cada arista guarda:
        # (origen, destino, valor)
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

        for arista, datos in self.aristas.items():

            origen = datos[0]
            destino = datos[1]

            if vertice == origen or vertice == destino:
                aristas_a_borrar.append(arista)

        # Eliminar las aristas
        for arista in aristas_a_borrar:

            origen = self.aristas[arista][0]
            destino = self.aristas[arista][1]

            # Eliminar la arista del origen
            if arista in self.lista[origen]:
                self.lista[origen].remove(arista)

            # Eliminar la arista del destino
            if arista in self.lista[destino]:
                self.lista[destino].remove(arista)

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

        # ==========================================
        # BUSCAR SI YA EXISTE ORIGEN -> DESTINO
        # ==========================================

        arista_encontrada = None

        for arista, datos in self.aristas.items():

            v1 = datos[0]
            v2 = datos[1]

            # IMPORTANTE:
            # En un grafo dirigido importa el orden.
            if v1 == origen and v2 == destino:
                arista_encontrada = arista
                break

        # ==========================================
        # PREGUNTAR QUÉ HACER
        # ==========================================

        print("\n¿Qué desea hacer?")
        print("1. Agregar conexión")
        print("2. Modificar valor de conexión")
        print("3. Eliminar conexión")

        opcion = input("Seleccione una opción: ")

        # ==========================================
        # AGREGAR CONEXIÓN
        # ==========================================

        if opcion == "1":

            if arista_encontrada is not None:

                print("La conexión ya existe.")
                return

            valor = int(input("Ingrese el valor de la arista: "))

            # Crear nueva arista
            self.contador_aristas += 1

            arista = "A" + str(self.contador_aristas)

            # Guardar:
            # origen, destino y valor
            self.aristas[arista] = (
                origen,
                destino,
                valor
            )

            # La arista pertenece a ambos vértices
            self.lista[origen].append(arista)
            self.lista[destino].append(arista)

            print(
                "Conexión",
                arista,
                origen,
                "->",
                destino,
                "agregada correctamente."
            )

        # ==========================================
        # MODIFICAR VALOR
        # ==========================================

        elif opcion == "2":

            if arista_encontrada is None:

                print("La conexión no existe.")
                return

            valor = int(input("Ingrese el nuevo valor de la arista: "))

            origen_arista = self.aristas[arista_encontrada][0]
            destino_arista = self.aristas[arista_encontrada][1]

            # Actualizar el valor
            self.aristas[arista_encontrada] = (
                origen_arista,
                destino_arista,
                valor
            )

            print(
                "Valor de la conexión",
                arista_encontrada,
                "modificado correctamente."
            )

        # ==========================================
        # ELIMINAR CONEXIÓN
        # ==========================================

        elif opcion == "3":

            if arista_encontrada is None:

                print("La conexión no existe.")
                return

            # Eliminar la arista del origen
            if arista_encontrada in self.lista[origen]:
                self.lista[origen].remove(arista_encontrada)

            # Eliminar la arista del destino
            if arista_encontrada in self.lista[destino]:
                self.lista[destino].remove(arista_encontrada)

            # Eliminar la arista
            del self.aristas[arista_encontrada]

            print(
                "Conexión",
                arista_encontrada,
                "eliminada correctamente."
            )

        else:

            print("Opción inválida.")

    # MOSTRAR LISTA
    def mostrar(self):

        if len(self.lista) == 0:
            print("La lista está vacía.")
            return

        print("\n===== LISTA DE INCIDENCIA =====")

        # ==========================================
        # MOSTRAR ARISTAS
        # ==========================================

        if len(self.aristas) > 0:

            print("\nAristas:")

            for arista, datos in self.aristas.items():

                origen = datos[0]
                destino = datos[1]
                valor = datos[2]

                print(
                    arista,
                    "->",
                    "(",
                    origen,
                    "->",
                    destino,
                    ", valor =",
                    valor,
                    ")"
                )

        else:

            print("\nNo hay aristas.")

        # ==========================================
        # MOSTRAR INCIDENCIA
        # ==========================================

        print("\nIncidencia:")

        for vertice in self.lista:

            print(vertice, "->", end=" ")

            for arista in self.lista[vertice]:

                origen = self.aristas[arista][0]
                destino = self.aristas[arista][1]
                valor = self.aristas[arista][2]

                # Si el vértice es el origen
                if vertice == origen:

                    print(
                        "(" + arista + ", +" + str(valor) + ")",
                        end=" "
                    )

                # Si el vértice es el destino
                elif vertice == destino:

                    print(
                        "(" + arista + ", -" + str(valor) + ")",
                        end=" "
                    )

            print()


def main():

    lista = ListaIncidencia()

    return lista
