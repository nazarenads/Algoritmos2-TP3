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
        if destino != None and v == destino:
            break
    return padre, orden


def componentes_fuertemente_conexas(
        v, grafo, visitados, apilados, orden, mb, pila, todas_cfc):
    visitados.add(v)
    mb[v] = orden[v]
    pila.appendleft(v)
    apilados.add(v)
    for w in grafo.obtener_adyacentes(v):
        if w not in visitados:
            orden[w] = orden[v] + 1
            componentes_fuertemente_conexas(
                w, grafo, visitados, apilados, orden, mb, pila, todas_cfc
            )
        if w in apilados:
            mb[v] = min(mb[v], mb[w])
    if orden[v] == mb[v] and len(pila) > 0:
        nueva_cfc = []
        while True:
            w = pila.popleft()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break
        todas_cfc.append(nueva_cfc)


def grados_entrada(grafo, vertices):
    grados_ent = {}
    for v in vertices:
        grados_ent[v] = 0
    for v in vertices:
        for w in grafo.obtener_adyacentes(v):
            if v in vertices and w in grados_ent:
                grados_ent[w] += 1
    return grados_ent


def orden_topologico_grados(grafo, vertices):
    grados_ent = grados_entrada(grafo, vertices)
    cola = deque()
    for v in vertices:
        if grados_ent[v] == 0:
            cola.append(v)
    resultado = []
    while len(cola) != 0:
        v = cola.pop()
        resultado.append(v)
        for w in grafo.obtener_adyacentes(v):
            if w in vertices:
                grados_ent[w] -= 1
                if grados_ent[w] == 0:
                    cola.append(w)
    if len(resultado) == len(vertices):
        return resultado
    else:
        return None