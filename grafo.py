class Grafo:
    def __init__(self, dirigido):
        """Crea un grafo vacío."""
        self.dirigido = dirigido
        self.grafo = {}
        self.cantidad_vertices = 0

    def agregar_vertice(self, vertice):
        """Agrega un vértice al grafo."""
        if vertice not in self.grafo:
            self.grafo[vertice] = {}
            self.cantidad_vertices += 1

    def vertice_pertenece(self, vertice):
        """Permite saber si un vértice ya está dentro del grafo."""
        return vertice in self.grafo

    def agregar_arista(self, v, w, peso=None):
        """Agrega una arista al grafo, si el grafo es pesado guarda su peso."""
        if not (self.vertice_pertenece(v) and self.vertice_pertenece(w)):
            raise Exception("Alguno de los vertices no pertenece al grafo.")
        self.grafo[v][w] = peso
        if not self.dirigido:
            self.grafo[w][v] = peso

    def ver_cantidad_vertices(self):
        return self.cantidad_vertices

    def obtener_vertices(self):
        """Devuelve una lista de todos los vértices que pertenecen al grafo."""
        vertices = []
        for vertice in self.grafo.keys():
            vertices.append(vertice)
        return vertices

    def obtener_adyacentes(self, vertice):
        """Devuelve una lista de vértices adyacentes a un vértice dado."""
        adyacentes = []
        if vertice not in self.grafo:
            raise Exception(f"El vértice {vertice} no pertenece al grafo")
        for v in self.grafo[vertice]:
            adyacentes.append(v)
        return adyacentes

    def borrar_vertice(self, vertice):
        """Borra un vértice del grafo."""
        if self.vertice_pertenece(self.grafo):
            self.grafo.pop(vertice)
        raise Exception(f"El vértice {vertice} no pertenece al grafo")

    def borrar_arista(self, v, w):
        """Borra una arista del grafo."""
        if not (self.vertice_pertenece(v) and self.vertice_pertenece(w)):
            raise Exception("Alguno de los vértices no pertenece al grafo.")
        self.grafo[v].pop(w)
        if not self.dirigido:
            self.grafo[w].pop(v)
