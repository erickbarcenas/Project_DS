#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

#app = Flask(__name__, nombre_carpeta_dif_a_templates = "prueba_template")
app = Flask(__name__) #instancia: nuevo objeto

@app.route('/')
def index(): 
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True, port= 5000)
