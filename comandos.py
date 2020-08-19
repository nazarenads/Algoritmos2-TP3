import random

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
    camino = []
    orden = {}
    camino.append(origen)
    orden[origen] = 0
    _dfs_primer_link(grafo, origen, orden, camino)
    last_index = len(camino) - 1
    resultado = ""
    for v in camino[:last_index]:
        resultado += v + " -> "
    resultado += camino[last_index]
    print(resultado)


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


def max_frec(label, vecinos):
    frecuencias = {}
    for i in vecinos: # Recorro vecinos y voy contando la frequencia con la que aparece cada etiqueta
        etiqueta = label[i]
        if etiqueta not in frecuencias:
            frecuencias[etiqueta] = 1
        else:
            frecuencias[etiqueta] += 1
    return max(frecuencias, key=frecuencias.get) # devuelvo la etiqueta con mayor frecuencia

def comunidades(grafo, origen):
    label = {}
    vertices = grafo.obtener_vertices()
    for i in range(grafo.ver_cantidad_vertices()): # Asigno una etiqueta a cada vertice del grafo
        label[vertices[i]] = i
    random.shuffle(vertices) # Determino un orden aleatorio para recorrer los vertices
    for v in vertices:
        vecinos = []
        for w in vertices:
            if v in grafo.obtener_adyacentes(w): # Obtengo vecinos de v
                vecinos.append(w)
        label[v] = max_frec(label, vecinos) # Actualizo etiqueta de v
    etiqueta_de_origen = label[origen]
    comunidad_del_origen = []
    for etiqueta in label.items(): # Busco la comunidad de origen
        if etiqueta[1] == etiqueta_de_origen:
            comunidad_del_origen.append(etiqueta[0])
    resultado = ""
    for v in comunidad_del_origen:
        if v != comunidad_del_origen[len(comunidad_del_origen)-1]:
            resultado += v + ", "
        else:
            resultado += v
    print(resultado)


def main():
    grafo = Grafo(True)
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_vertice("E")
    grafo.agregar_vertice("F")
    grafo.agregar_vertice("G")
    grafo.agregar_vertice("H")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("B", "D")
    grafo.agregar_arista("C", "E")
    grafo.agregar_arista("E", "F")
    grafo.agregar_arista("F", "G")
    grafo.agregar_arista("G", "H")
    #comunidades(grafo, "A")

main()