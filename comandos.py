from constantes import LISTA_COMANDOS
from grafo_utils import *
from grafo import Grafo

def imprimir_operaciones():
    for comando in LISTA_COMANDOS[1:]:
        print(comando)

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

def imprimir_costo(destino, orden):
    print(f"Costo: {orden[destino]}")


def camino_minimo(grafo, origen, destino=None):
    padres, orden = bfs(grafo, origen, destino)
    camino = reconstruir_camino(padres, origen, destino)
    mostrar_camino(camino, destino, orden)
    imprimir_costo(destino, orden)

def diametro(grafo):
    orden_max = {}
    padres_max = {}
    costo_max = 0
    origen_max = ""
    destino_max = ""
    for v in grafo.obtener_vertices():
        padres, orden = bfs(grafo, v)
        costo = max(orden.values())
        if(costo > costo_max):
            costo_max = costo
            orden_max = orden
            padres_max = padres
            destino_max = max(orden, key=orden_max.get)
            origen_max = v
    camino_max = reconstruir_camino(padres_max, origen_max, destino_max)
    mostrar_camino(camino_max, destino_max, orden_max)
    imprimir_costo(destino_max, orden_max)

def todos_en_rango(grafo, pagina, n):
    padres, orden = bfs(grafo, pagina)
    cont = 0
    for x in orden.values():
        if x == n:
            cont += 1
    print(cont)


def navegacion_primer_link(grafo, origen):
    padre, orden = dfs_primer_link(grafo, origen)
    print(padre)
    print(orden)
    destino = max(orden, key=orden.get)
    camino = reconstruir_camino(padre, origen, destino)
    mostrar_camino(camino, destino, orden)


def dfs_primer_link(grafo, origen):
    padre = {}
    orden = {}
    padre[origen] = None
    orden[origen] = 0
    _dfs_primer_link(grafo, origen, padre, orden)
    return padre, orden


def _dfs_primer_link(grafo, vertice, padre, orden):
    adyacentes = grafo.obtener_adyacentes(vertice)
    if len(adyacentes) == 0 or orden[vertice] == 19:
        return
    primer_adyacente = adyacentes[0]
    padre[primer_adyacente] = vertice
    orden[primer_adyacente] = orden[vertice] + 1
    _dfs_primer_link(grafo, primer_adyacente, padre, orden)


def main():
    grafo = Grafo(True)
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_vertice("E")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("C", "B")
    grafo.agregar_arista("B", "D")
    grafo.agregar_arista("C", "E")
    todos_en_rango(grafo, "A", 2)

main()