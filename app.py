from flask import Flask, render_template, request

app = Flask(__name__)

def convertir_metros_a_kilometros(metros):
    return metros / 1000

def convertir_gramos_a_kilogramos(gramos):
    return gramos / 1000

def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    unidad = None
    error = None

    if request.method == 'POST':
        try:
            valor = float(request.form['valor'])
            tipo_conversion = request.form['tipo_conversion']

            if tipo_conversion == 'metros_kilometros':
                resultado = convertir_metros_a_kilometros(valor)
                unidad = 'kilómetros'
            elif tipo_conversion == 'gramos_kilogramos':
                resultado = convertir_gramos_a_kilogramos(valor)
                unidad = 'kilogramos'
            elif tipo_conversion == 'celsius_fahrenheit':
                resultado = convertir_celsius_a_fahrenheit(valor)
                unidad = '°F'
            else:
                error = "Tipo de conversión no válida."
        except ValueError:
            error = "Por favor, introduce un valor numérico válido."

    return render_template('index.html', resultado=resultado, unidad=unidad, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
