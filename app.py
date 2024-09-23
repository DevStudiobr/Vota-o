from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_dados', methods=['POST'])
def enviar_dados():
    dados = request.json.get('dados')
    # Aqui você pode processar os dados como quiser
    print(f'Dados recebidos: {dados}')
    return jsonify({'resposta': f'Dados recebidos: {dados}'}), 200

if __name__ == '__main__':
    app.run(debug=True)