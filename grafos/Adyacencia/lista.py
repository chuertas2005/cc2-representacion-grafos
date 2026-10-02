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
            if vertice in self.lista[v]:
                self.lista[v].remove(vertice)

        # Eliminar vértice
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

        origen = vertices[origen - 1]
        destino = vertices[destino - 1]

        valor = int(input("Ingrese 1 para conectar o 0 para desconectar: "))

        if valor == 1:

            if destino not in self.lista[origen]:
                self.lista[origen].append(destino)

            if origen not in self.lista[destino]:
                self.lista[destino].append(origen)

            print("Conexión agregada correctamente.")

        elif valor == 0:

            if destino in self.lista[origen]:
                self.lista[origen].remove(destino)

            if origen in self.lista[destino]:
                self.lista[destino].remove(origen)

            print("Conexión eliminada correctamente.")

        else:

            print("El valor debe ser 0 o 1.")

    # MOSTRAR LISTA
    def mostrar(self):

        if len(self.lista) == 0:
            print("La lista está vacía.")
            return

        print("\n===== LISTA DE ADYACENCIA =====")

        for vertice in self.lista:
            print(vertice, "->", self.lista[vertice])


def main():

    lista = ListaAdyacencia()

    return lista

