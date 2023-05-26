from flask import Flask, request, render_template
from clases import *
import json

# Load the data from the JSON file
with open('data.json') as json_file:
    data = json.load(json_file)

# Access the data for each class
respuesta_de_cliente = data['RespuestaDeCliente']
llamada = data['Llamada']
cliente = data['Cliente']
estado = data['Estado']
cambio_estado = data['CambioEstado']
respuesta_posible = data['RespuestaPosible']
pregunta = data['Pregunta']
encuestas = data['Encuesta']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return 'About'

@app.route('/surveys', methods=['GET', 'POST'])
def get_surveys():
    if request.method == 'POST':
        initial_date = request.form['initial_date']
        end_date = request.form['end_date']

        encuestas_filtradas = [encuesta for encuesta in encuestas if initial_date <= encuesta.date <= end_date]

        return render_template('encuestas.html', encuestas=encuestas_filtradas)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)