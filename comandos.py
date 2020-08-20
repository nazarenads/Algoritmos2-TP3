import random

from constantes import LISTA_COMANDOS
from grafo_utils import *
from grafo import Grafo

# FUNCIONES AUXILIARES

def reconstruir_camino(padres, origen, destino):
    camino = []
    v = destino
    while v != None:
        camino.append(v)
        if v not in padres: break
        v = padres[v]
    camino.reverse()
    return camino

def mostrar_camino(camino):
    resultado = " -> ".join(camino)
    print(resultado)

def imprimir_costo(destino, orden):
    print(f"Costo: {orden[destino]}")


# COMANDOS

def imprimir_operaciones():
    for comando in LISTA_COMANDOS[1:]:
        print(comando)

def camino_minimo(grafo, origen, destino=None):
    padres, orden = bfs(grafo, origen, destino)
    camino = reconstruir_camino(padres, origen, destino)
    if destino not in orden:
        print("No se encontro recorrido")
    else:
        mostrar_camino(camino)
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
    mostrar_camino(camino_max)
    imprimir_costo(destino_max, orden_max)


def todos_en_rango(grafo, pagina, n):
    padres, orden = bfs(grafo, pagina)
    cont = 0
    for x in orden.values():
        if x == n:
            cont += 1
    print(cont)


def navegacion_primer_link(grafo, origen):
    camino = []
    orden = {}
    camino.append(origen)
    orden[origen] = 0
    _dfs_primer_link(grafo, origen, orden, camino)
    mostrar_camino(camino)

def _dfs_primer_link(grafo, vertice, orden, camino):
    adyacentes = grafo.obtener_adyacentes(vertice)
    if len(adyacentes) == 0 or orden[vertice] == 20:
        return camino
    primer_adyacente = adyacentes[0]
    camino.append(primer_adyacente)
    orden[primer_adyacente] = orden[vertice] + 1
    _dfs_primer_link(grafo, primer_adyacente, orden, camino)


def conectividad(grafo, origen, cfc_guardada):
    visitados = set()
    apilados = set()
    orden = dict()
    orden[origen] = 0
    mb = dict()
    pila = deque()
    todas_cfc = []
    if origen not in cfc_guardada:
        componentes_fuertemente_conexas(
            origen, grafo, visitados, apilados, orden, mb, pila, todas_cfc
        )
        cfc_guardada = todas_cfc[len(todas_cfc)-1]
    resultado = ", ".join(cfc_guardada)
    print(resultado)
    return cfc_guardada


def lectura(grafo, paginas):
    orden = orden_topologico_grados(grafo, paginas)
    if orden is None:
        print("No existe forma de leer las paginas en orden")
    else:
        resultado = ", ".join(orden)
        print(resultado)

def ciclo_dfs(grafo, v, camino, n):
    camino.append(v)
    if len(camino) == n+1 and camino[n] == camino[0]:
        return True
    if len(camino) > n+1:
        camino.pop()
        return False
    for w in grafo.obtener_adyacentes(v):
        if w != camino[0] and w in camino: continue
        if ciclo_dfs(grafo, w, camino, n):
            return True
    camino.pop()
    return False

def ciclo(grafo, pagina, n):
    camino = []
    ciclo_dfs(grafo, pagina, camino, n)
    if len(camino) != n+1 or camino[n] != pagina:
        print("No se encontro recorrido")
    else:
        mostrar_camino(camino)