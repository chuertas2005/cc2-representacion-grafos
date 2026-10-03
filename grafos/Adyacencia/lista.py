class ListaAdyacencia:

    def __init__(self):
        self.lista = {}

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

        # Eliminar conexiones hacia ese vértice
        for v in self.lista:

            for conexion in self.lista[v][:]:

                if conexion[0] == vertice:
                    self.lista[v].remove(conexion)

        # Eliminar vértice
        del self.lista[vertice]

        print("Vértice", vertice, "borrado correctamente.")

    # MODIFICAR CONEXIONES
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

        origen = vertices[origen - 1]
        destino = vertices[destino - 1]

        # Valor de origen -> destino
        valor_ida = int(input(
            f"Ingrese el valor de {origen} -> {destino} "
            "(0 para desconectar): "
        ))

        # Valor de destino -> origen
        valor_vuelta = int(input(
            f"Ingrese el valor de {destino} -> {origen} "
            "(0 para desconectar): "
        ))

        # Buscar conexión origen -> destino
        conexion_origen = None

        for conexion in self.lista[origen]:

            if conexion[0] == destino:
                conexion_origen = conexion
                break

        # Buscar conexión destino -> origen
        conexion_destino = None

        for conexion in self.lista[destino]:

            if conexion[0] == origen:
                conexion_destino = conexion
                break

        # ==========================================
        # MODIFICAR / AGREGAR ORIGEN -> DESTINO
        # ==========================================

        if valor_ida != 0:

            if conexion_origen is not None:

                posicion = self.lista[origen].index(conexion_origen)

                self.lista[origen][posicion] = (destino, valor_ida)

            else:

                self.lista[origen].append((destino, valor_ida))

        else:

            if conexion_origen is not None:
                self.lista[origen].remove(conexion_origen)

        # ==========================================
        # MODIFICAR / AGREGAR DESTINO -> ORIGEN
        # ==========================================

        if valor_vuelta != 0:

            if conexion_destino is not None:

                posicion = self.lista[destino].index(conexion_destino)

                self.lista[destino][posicion] = (origen, valor_vuelta)

            else:

                self.lista[destino].append((origen, valor_vuelta))

        else:

            if conexion_destino is not None:
                self.lista[destino].remove(conexion_destino)

        print("Conexiones modificadas correctamente.")

    # MOSTRAR LISTA
    def mostrar(self):

        if len(self.lista) == 0:
            print("La lista está vacía.")
            return

        print("\n===== LISTA DE ADYACENCIA =====")

        for vertice in self.lista:

            print(vertice, "->", end=" ")

            for conexion in self.lista[vertice]:

                destino = conexion[0]
                valor = conexion[1]

                print(f"({destino}, {valor})", end=" ")

            print()


def main():

    lista = ListaAdyacencia()

    return lista
