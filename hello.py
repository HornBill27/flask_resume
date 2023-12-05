from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	first_name="Max"
	favourite_pizza=["pepperoni","margarita","chilly","cheese-burst","vegetable"]
	return render_template('index.html', f_name=first_name, favourite_pizza=favourite_pizza)

@app.route('/about')
def about():
	return render_template('about.html')