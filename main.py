from flask import Flask, request, jsonify, send_file
import random
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

@app.route('/vetor_randomizado', methods=['POST'])
def vetor_randomizado():
    try:
        #recupera json
        data = request.get_json()
    except Exception as e:
        data = None
    #Organização do vetor por meio do algoritmo Bubble sort
    if data and 'vetor' in data:
        length = len(data['vetor'])
        for i in range(length - 1):
            swapped = False
            for j in range(0, length - i - 1):
                if data['vetor'][j] > data['vetor'][j + 1]:
                    data['vetor'][j], data['vetor'][j + 1] = data['vetor'][j + 1], data['vetor'][j]
                    swapped = True
            if not swapped:
                break
        return jsonify({'vetor': data['vetor']})
    else:
        vetor = []
        for _ in range(50000):
            numero_aleatorio = random.randint(0, 100000)
            vetor.append(numero_aleatorio)

        n = len(vetor)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            vetor[i], vetor[j] = vetor[j], vetor[i]

        return jsonify({'vetor': vetor})

@app.route('/scatter_plot', methods=['POST'])
def scatter_plot():
    data = request.get_json()
    if not data or 'x' not in data or 'y' not in data:
        return jsonify({'Error': 'Necessario informar todos os parametros!'})

    x = data['x']
    y = data['y']

    #gera grafico
    plt.scatter(x, y)

    #salva
    plot_buffer = BytesIO()
    plt.savefig(plot_buffer, format='png')
    plot_buffer.seek(0)

    return send_file(plot_buffer, mimetype='image/png')

@app.route('/line_plot', methods=['POST'])
def line_plot():

    data = request.get_json()

    if not data or 'vetor' not in data:
        return jsonify({'ERRO': 'Necessario informar o vetor para criação do grafico'})

    else:
        plt.plot(data['vetor'], linestyle='dotted')
        plot_buffer = BytesIO()
        plt.savefig(plot_buffer, format='png')
        plot_buffer.seek(0)
        plt.close()

        return send_file(plot_buffer, mimetype='image/png')

@app.route('/bar_plot', methods=['POST'])
def bar_plot():
    data = request.get_json()

    if not data or 'vetor' not in data:
        return jsonify({"Erro": "Necessario informar o vetor"})

    else:
        x = ["A", "B", "C", "D"]
        y = data['vetor']

        plt.bar(x, y)
        plot_buffer = BytesIO()
        plt.savefig(plot_buffer, format='png')
        plot_buffer.seek(0)
        plt.close()

        return send_file(plot_buffer, mimetype='image/png')

@app.route('/bubble_plot', methods=['POST'])
def bubble_plot():
    data = request.get_json()
    if not data or 'x' not in data or 'y' not in data or 'size' not in data:
        return jsonify({"Erro": "Necessario informar todos os parametros"})

    else:
        plt.scatter(data['x'], data['y'], data['size'])
        plot_buffer = BytesIO()
        plt.savefig(plot_buffer, format='png')
        plot_buffer.seek(0)
        plt.close()

        return send_file(plot_buffer, mimetype='image/png')


if __name__ == '__main__':
    app.run(port=5000, debug=True)