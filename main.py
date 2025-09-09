# pip install flask

from flask import Flask, request, make_response, jsonify

# Importação da base de dados
from bd import Carros

# Esse módulo do Flask vai subir a nossa API localmente
# Vamos instaciar o modulo Flask na nossa variavel
app = Flask ('carros')

# Metodo 1 - Visualização de dados (get)
# 1 - o que esse metodo vai fazer?
# 2 - Onde ele vai fazer?
@app.route('/carrinho', methods=['GET'])
def get_carros():
    return Carros

# Metodo 1 parte 2 - visualização de dados por id (get)
@app.route('/carrinho/<int:id_pam>', methods=['GET'])
def get_carros_id(id_pam):
    for car in Carros:
        if car.get('id') == id_pam:
            return jsonify(car)
        
# Metodo 2 - Criar novos registros (get)
# Verificar os dados que estão passados na requisição e armazenar na 

@app.route('/carrinho', methods=['Post'])
def criar_carro():
    car = request.json
    Carros.append(car)
    return make_response(
        jsonify(
            texto = 'Carro cadastrado com sucesso!',
            carrinho = car
        )
    )

# Metodo 3 - Deletar registros (delete)
@app.route('/carrinho/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify(
                {'mensagem': "Carro Excluído"}
            )    
        
# Metodo 4 - Editar os registros (put)
@app.route('/carrinho/<int:id>', methods=['PUT'])
def editar_carro(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(
                Carros[indice]
            )

app.run(port=5000, host='localhost', debug=True)