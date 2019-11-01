from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/params')
@app.route('/params/<name>')
def params(name= 'default'):
    return "El parametro es: {}".format(name)

app.run()
#prueba 1