from flask import Flask, request, jsonify
import json

app = Flask(__name__)
personas = []

@app.route('/',methods=['GET'])
def inicio():
    return "Bienvenido"

@app.route('/agregar',methods=['POST'])
def agregarPersona():
    cuerpo = request.get_json()
    nombre = cuerpo['nombre']
    edad = cuerpo['edad']
    persona = {'nombre':nombre,'edad':edad}
    global personas
    personas.append(persona)
    return jsonify({"mensaje":"Agregado correctamente"})

@app.route('/obtener',methods=['GET'])
def obtenerPersonas():
    return jsonify(personas)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=4000)