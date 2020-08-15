import unittest
from grafo import Grafo


class TestGrafo(unittest.TestCase):
    def test_vertice_pertenece(self):
        #creo un grafo no dirigido
        grafo = Grafo(False)
        #le agrego un vértice
        grafo.agregar_vertice("A")
        #me fijo si el vértice pertenece o no al grafo
        self.assertTrue(grafo.vertice_pertenece("A"))


if __name__ == '__main__':
    unittest.main()
