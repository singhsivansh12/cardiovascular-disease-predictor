from flask import Flask, render_template, redirect, request
import pickle
# from sklearn.externals import joblib


app = Flask(__name__)

pickle_in = open("cardio_vascular_model.pickle", "rb")
model = pickle.load(pickle_in)

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/', methods = ['POST'])
def marks():
	try:
		if request.method == 'POST' :
			age = int(request.form['age'])
			gender = int(request.form['gender'])
			height = int(request.form['height'])
			weight = float(request.form['weight'])
			ap_hi = int(request.form['ap_hi'])
			ap_lo = int(request.form['ap_lo'])
			cholesterol = int(request.form['cholesterol'])
			gluc = int(request.form['gluc'])
			smoke = int(request.form['smoke'])
			alco = int(request.form['alco'])
			active = int(request.form['active'])
			bmi = float(request.form['bmi'])

			result = model.predict([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, bmi]])

			if result[0] == 1:
				return render_template("index1.html", result = "Ahhh..You have Cardio-Vascular Disease" )
			else:
				return render_template("index2.html", result = "You are Disease-free!! :) :)")
	except ValueError:
		return render_template('error.html')
	
@app.errorhandler(404)
def not_found(e):
	return render_template('error.html')

if __name__ == '__main__':
	app.run(debug = True)