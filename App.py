import pymysql
from flask import Flask, render_template, request

# Insertar credenciales de la base de datos
host = 'XXXXXXXXXX'
port = 3306
user = 'XXXXX'
password = 'XXXXX'
database = 'examen'

# Conectar a la base de datos
connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)


app = Flask(__name__)
 
# Ruta para el formulario de entrada de datos
@app.route('/')
def formulario():
    return render_template('form.html')
    
# Ruta para procesar los datos del formulario
@app.route('/comparar', methods=['POST'])
def comparar():
    usuario = request.form['usuario']
    texto1 = request.form['texto1']
    texto2 = request.form['texto2']
    comp = texto(texto1, texto2)
    
    cursor = connection.cursor()
    if comp == 1:
        comparacion = "Los textos son IGUALES"
        query = 'INSERT INTO formulario (name, texto1, texto2, comparacion) VALUES ("'+usuario +'", "'+texto1 +'", "'+texto2+'", 1)'
        print('INSERT INTO formulario (name, texto1, texto2, comparacion) VALUES ("'+usuario +'", "'+texto1 +'", "'+texto2+'", 1)')

    else:
        comparacion = "Los textos son DIFERENTES"
        query = 'INSERT INTO formulario (name, texto1, texto2, comparacion) VALUES ("'+usuario +'", "'+texto1 +'", "'+texto2+'", 0)'
        print('INSERT INTO formulario (name, texto1, texto2, comparacion) VALUES ("'+usuario +'", "'+texto1 +'", "'+texto2+'", 0)')

    cursor.execute(query)
    connection.commit()
    
    cursor.close()
    connection.close()

    return render_template('result.html', txt1=texto1, txt2=texto2, compar=comparacion)

def texto(texto1, texto2):
    
    if texto1 == texto2:
        comparacion = 1
    else:
        comparacion = 0
    
    print("Valor de comparacion -> " +str(comparacion))
    return comparacion

 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



