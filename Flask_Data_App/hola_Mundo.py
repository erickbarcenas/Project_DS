from flask import Flask

app = Flask(__name__) #instancia: nuevo objeto
@app.route('/')#Decorador o wrap: ruta de acceso
def index(): #Función que retorna un string
	return 'Hola Mundo'

app.run()#Ejecuta el servido localhost:5000

