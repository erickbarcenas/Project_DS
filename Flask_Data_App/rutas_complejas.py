from flask import Flask
from flask import request

app = Flask(__name__) #instancia: nuevo objeto
@app.route('/')
def index(): 
	return 'Bienvenido'

@app.route('/params')
@app.route('/params/<name>')
@app.route('/params/<name>/<int:num>')
def params(name = 'Error por default', num = 'Valor por default'):
	return 'El nombre es: {}, y el número {}'.format(name, num)

if __name__ == '__main__':
	app.run(debug = True, port= 5000)
