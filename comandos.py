import grafo_utils

def reconstruir_camino(padres, origen):
    camino = []
    camino.append(origen)
    for v in padres:
        camino.append()

def camino_minimo(grafo, origen, destino):
    padres, costo = bfs(origen, destino)
    camino = reconstruir_camino(padres, origen)