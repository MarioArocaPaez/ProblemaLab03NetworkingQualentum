from flask import Flask, request, jsonify
from database import create_string, read_strings, update_string, delete_string

app = Flask(__name__)

# Endpoint para crear una cadena
@app.route('/strings', methods=['POST'])
def create():
    data = request.get_json()
    if not data or "string" not in data:
        return {"error": "Invalid input"}, 400
    string = data["string"]
    response, status = create_string(string)
    return jsonify(response), status

# Endpoint para leer todas las cadenas
@app.route('/strings', methods=['GET'])
def read():
    response, status = read_strings()
    return jsonify(response), status

# Endpoint para actualizar una cadena
@app.route('/strings/<old_string>', methods=['PUT'])
def update(old_string):
    data = request.get_json()
    if not data or "new_string" not in data:
        return {"error": "Invalid input"}, 400
    new_string = data["new_string"]
    return jsonify(*update_string(old_string, new_string))

# Endpoint para eliminar una cadena
@app.route('/strings/<string>', methods=['DELETE'])
def delete(string):
    return jsonify(*delete_string(string))

if __name__ == '__main__':
    app.run(debug=True)
