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
            #print(f'{w} no esta visitado, lo visito')
            orden[w] = orden[v] + 1
            componentes_fuertemente_conexas(
                w, grafo, visitados, apilados, orden, mb, pila, todas_cfc
            )

        if w in apilados:
            #if mb[v] > mb[w]:
                #print(f'wii {v} bajo su mb de {mb[v]} a {mb[w]} gracias a la coneccion con {w}')
            mb[v] = min(mb[v], mb[w])

    if orden[v] == mb[v] and len(pila) > 0:
        nueva_cfc = []
        while True:
            w = pila.popleft()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break

        #print('NUEVA CFC!: ', nueva_cfc)
        todas_cfc.append(nueva_cfc)
    return todas_cfc