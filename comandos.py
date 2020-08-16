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

def mostrar_camino(camino, destino, orden):
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

def camino_minimo(grafo, origen, destino = None):
    padres, orden = bfs(grafo, origen, destino)
    camino = reconstruir_camino(padres, origen, destino)
    mostrar_camino(camino, destino, orden)

def diametro(grafo):
    orden_max = {}
    costo_max = 0
    origen_max = ""
    destino_max = ""
    for v in grafo.obtener_vertices():
        padres, orden = bfs(grafo, v)
        costo = max(orden.values())
        if(costo > costo_max):
            costo_max = costo
            orden_max = orden
            destino_max = max(orden, key=orden_max.get)
            origen_max = v
    camino_max = reconstruir_camino(padres, v, destino_max)
    mostrar_camino(camino_max, destino_max, orden_max)

def main():
    grafo = Grafo(True)
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("C", "B")
    grafo.agregar_arista("B", "D")
    camino_minimo(grafo, "A", "D")
    dic = {"A": 4, "B": 2}
    max_dic = max(dic, key=dic.get)
    print(max_dic)

main()