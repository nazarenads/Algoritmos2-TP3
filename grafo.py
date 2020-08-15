class Grafo:
    def __init__(self, dirigido):
        self.dirigido = dirigido
        self.vertices = {}
        self.cantidad_vertices = 0

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}
            self.cantidad_vertices += 1

    def vertice_pertenece(self, vertice):
        return vertice in self.vertices

    def agregar_arista(self, v, w, peso=None):
        if not (self.vertice_pertenece(v) and self.vertice_pertenece(w)):
            return False
        self.vertices[v][w] = peso
        if not self.dirigido:
            self.vertices[w][v] = peso
        return True
