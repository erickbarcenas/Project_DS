#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__) #instancia: nuevo objeto

@app.route('/user/<name>')
def user(name='Erick'): 
	age = 21
	my_list = [1, 2, 3 ,4]
	return render_template('user.html', this_name= name, this_age= age, this_list= my_list)

if __name__ == '__main__':
	app.run(debug = True, port= 5000)