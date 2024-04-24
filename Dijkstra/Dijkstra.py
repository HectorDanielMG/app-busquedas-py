def dijkstra(Grafo, salida, destino):
    dist, prev = {}, {}

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    Q = set(Grafo.keys())

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)

        for vecino, peso in Grafo[u].items():
            alt = dist[u] + peso
            if alt < dist[vecino]:
                dist[vecino] = alt
                prev[vecino] = u

    return prev

def reconstruir_camino(previos, nodo):
    camino = []
    while nodo is not None:
        camino.insert(0, nodo)
        nodo = previos[nodo]
    return camino
