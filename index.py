from flask import Flask, render_template, request
from BCU.BCU import buscar_solucion_UCS as BCU_buscar_solucion
from Dijkstra.Dijkstra import dijkstra as dijkstra_buscar_solucion
from BCU.BCU import conexiones

# Define el grafo aquí o importa el archivo que lo contiene
grafo = {
    '1': {'2': 3, '3': 6},
    '2': {'3': 2, '4': 1},
    '3': {'4': 4, '5': 2},
    '4': {'3': 4, '5': 6},
    '5': {'6': 2, '7': 2},
    '6': {'7': 3},
    '7': {}
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_BCU', methods=['POST'])
def buscar_BCU():
    estado_inicial = request.form['estado_inicial']
    solucion = request.form['solucion']
    nodo_solucion = BCU_buscar_solucion(conexiones, estado_inicial, solucion)
    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()

    return render_template('index.html', resultado_BCU=resultado, costo_BCU=nodo_solucion.get_costo())

@app.route('/buscar_dijkstra', methods=['POST'])
def buscar_dijkstra():
    salida = request.form['salida']
    nodo_destino = request.form['nodo_destino']
    previos = dijkstra_buscar_solucion(grafo, salida, nodo_destino)
    camino = []
    nodo = nodo_destino
    while nodo is not None:
        camino.insert(0, nodo)
        nodo = previos[nodo]
    return render_template('index.html', resultado_dijkstra=camino)

if __name__ == '__main__':
    app.run(debug=True)
