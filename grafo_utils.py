from grafo import Grafo
from collections import deque

def bfs(grafo, origen, destino = None):
    visitados = set()
    orden = {}
    padre = {}
    orden[origen] = 0
    padre[origen] = None
    visitados.add(origen)
    cola = deque()
    cola.append(origen)
    while len(cola) != 0:
        v = cola.popleft()
        for w in grafo.obtener_adyacentes(v):
            if w not in visitados:
                padre[w] = v
                orden[w] = orden[v] + 1
                visitados.add(w)
                cola.append(w)
    return padre, orden