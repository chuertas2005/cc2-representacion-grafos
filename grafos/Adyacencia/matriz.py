class MatrizAdyacencia:

    def __init__(self):
        self.vertices = []
        self.matriz = []

    # AGREGAR VÉRTICE
    def agregar(self, vertice):

        if vertice in self.vertices:
            print("El vértice ya existe")
            return

        self.vertices.append(vertice)

        # Agregar columna
        for fila in self.matriz:
            fila.append(0)

        # Agregar fila
        self.matriz.append([0] * len(self.vertices))

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

        # Eliminar fila
        self.matriz.pop(posicion)

        # Eliminar columna
        for fila in self.matriz:
            fila.pop(posicion)

        # Eliminar vértice
        self.vertices.pop(posicion)

        print("Vértice", vertice, "borrado correctamente.")

    # MODIFICAR CONEXIONES
    def modificar(self):

        if len(self.vertices) < 2:
            print("Se necesitan al menos 2 vértices.")
            return

        print("\nVértices existentes:")

        for i, vertice in enumerate(self.vertices, 1):
            print(i, ".", vertice)

        origen = int(input("Seleccione el vértice de origen: "))
        destino = int(input("Seleccione el vértice de destino: "))

        if origen < 1 or origen > len(self.vertices):
            print("Origen inválido.")
            return

        if destino < 1 or destino > len(self.vertices):
            print("Destino inválido.")
            return

        i = origen - 1
        j = destino - 1

        # Valor de origen -> destino
        valor_ida = int(input(
            f"Ingrese el valor de {self.vertices[i]} -> {self.vertices[j]} "
            "(0 para desconectar): "
        ))

        # Valor de destino -> origen
        valor_vuelta = int(input(
            f"Ingrese el valor de {self.vertices[j]} -> {self.vertices[i]} "
            "(0 para desconectar): "
        ))

        self.matriz[i][j] = valor_ida
        self.matriz[j][i] = valor_vuelta

        print("Conexiones modificadas correctamente.")

    # MOSTRAR MATRIZ
    def mostrar(self):

        if len(self.vertices) == 0:
            print("La matriz está vacía.")
            return

        print("\n===== MATRIZ DE ADYACENCIA =====")

        print("   ", end="")

        for vertice in self.vertices:
            print(vertice, end=" ")

        print()

        for i in range(len(self.vertices)):

            print(self.vertices[i], "  ", end="")

            for valor in self.matriz[i]:
                print(valor, end=" ")

            print()


def main():

    matriz = MatrizAdyacencia()

    return matriz
