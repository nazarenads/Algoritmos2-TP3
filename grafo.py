class Grafo:
    def __init__(self):
        self.vertices = {}
        self.cantidad_vertices = 0

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
            self.cantidad_vertices += 1

    def vertice_pertenece(self, vertice):
        return vertice in self.vertices

    def agregar_arista(self, inicio, fin):
        if not (self.vertice_pertenece(inicio) and self.vertice_pertenece(fin)):
            return False
        self.vertices[inicio].append(fin)
        return True

# si agrego vertices A y B el grafo queda: self.vertices = {"A": {}, "B":{}}