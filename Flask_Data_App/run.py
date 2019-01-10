from flask import Flask

app = Flask(__name__) #instancia: nuevo objeto
@app.route('/')#Decorador o wrap: ruta de acceso
def index(): #Función que retorna un string
	return 'It Works'

if __name__ == '__main__':
	app.run(debug = True, port= 5000)#2^16 [1024,65500] || debug = False (default)

