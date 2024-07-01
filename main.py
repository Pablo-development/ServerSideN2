from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/vetor_randomizado', methods=['POST'])
def vetor_randomizado():
    try:
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

if __name__ == '__main__':
    app.run(port=5000, debug=True)