from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

votantes = []
opcoes = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar_votante', methods=['POST'])
def adicionar_votante():
    nome_votante = request.json.get('nome')
    if nome_votante:
        votantes.append(nome_votante)
        return jsonify(votantes), 200
    return jsonify({'error': 'Nome inválido'}), 400

@app.route('/adicionar_opcao', methods=['POST'])
def adicionar_opcao():
    opcao_votacao = request.json.get('opcao')
    if opcao_votacao:
        opcoes.append(opcao_votacao)
        return jsonify(opcoes), 200
    return jsonify({'error': 'Opção inválida'}), 400

@app.route('/realizar_votacao', methods=['GET'])
def realizar_votacao():
    if not votantes or not opcoes:
        return jsonify({'error': 'É necessário ter votantes e opções para realizar a votação.'}), 400
    
    votos = {opcao: 0 for opcao in opcoes}
    
    for votante in votantes:
        voto = random.choice(opcoes)
        votos[voto] += 1
    
    return jsonify(votos), 200

if __name__ == '__main__':
    app.run(debug=True)
