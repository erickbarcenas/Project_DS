from flask import Flask
from flask import request

app = Flask(__name__) #instancia: nuevo objeto
@app.route('/')
def index(): 
	return 'Bienvenido'

@app.route('/PlayApps_201810')
def PlayApps_201810():
	return 'PlayApps_201810'

@app.route('/PlayApps_201811')
def PlayApps_201811():
	return 'PlayApps_201811'

@app.route('/PlayApps_201812')
def PlayApps_201812():
	return 'PlayApps_201812'

# http://localhost:5000/params?params1=Erick_Barcenas

@app.route('/params')
def params():
	param = request.args.get('params1', 'no contiene el parámetro') 
	param_dos = request.args.get('params2','no contiene el parámetro 2')
	return 'El parametro uno es: {}, y el dos es: {}'.format(param, param_dos)

if __name__ == '__main__':
	app.run(debug = True, port= 5000)

