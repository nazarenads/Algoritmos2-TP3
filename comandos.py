from grafo_utils import *
from grafo import Grafo

def reconstruir_camino(padres, origen, destino):
    camino = []
    v = destino
    while v != None:
        camino.append(v)
        if v not in padres: break
        v = padres[v]
    camino.reverse()
    return camino

def camino_minimo(grafo, origen, destino):
    padres, orden = bfs(grafo, origen, destino)
    camino = reconstruir_camino(padres, origen, destino)
    resultado = ""
    for v in camino:
        if v != destino:
            resultado += v + " -> "
        else:
            resultado += v
    if destino not in orden:
        print("No se encontro recorrido")
    else:
        print(resultado)
        print(f"Costo: {orden[destino]}")

def main():
    grafo = Grafo(True)
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("C", "B")
    grafo.agregar_arista("B", "D")
    camino_minimo(grafo, "D", "A")

main()