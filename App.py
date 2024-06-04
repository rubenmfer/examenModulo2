from flask import Flask, render_template, request
 
app = Flask(__name__)
 
# Ruta para el formulario de entrada de datos
@app.route('/')
def formulario():
    return render_template('form.html')
    
# Ruta para procesar los datos del formulario
@app.route('/comparar', methods=['POST'])
def comparar():
    texto1 = request.form['texto1']
    texto2 = request.form['texto2']
    comp = texto(texto1, texto2)

    if comp is True:
        comparacion = "Los textos son IGUALES"
    else:
        comparacion = "Los textos son DIFERENTES"

    return render_template('result.html', txt1=texto1, txt2=texto2, compar=comparacion)

def texto(texto1, texto2):
    
    if texto1 == texto2:
        comparacion = True
    else:
        comparacion = False
    
    return comparacion

 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

