from flask import Flask,render_template,request
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('homepage.html')

@app.route('/diagnosis', methods = ['POST'])
def diagnosis():

	if request.method == 'POST':
		age = request.form['age']
		gender = request.form['age']
		tot_bilirubin= request.form['tot_bilirubin']
		direct_bilirubin = request.form['direct_bilirubin']
		tot_proteins = request.form['tot_proteins']
		albumin= request.form['albumin']
		ag_ratio = request.form['ag_ratio']
		sgot= request.form['sgot']
		sgpt = request.form['sgpt']
		alkphos = request.form['alkphos']

		gender = gender.lower()
		if (gender=='male'):
			gender=1
		else:
			gender=0
		age = float(age)
		gender = float(gender)
		tot_bilirubin = float(tot_bilirubin)
		direct_bilirubin = float(direct_bilirubin)
		albumin = float(albumin)
		ag_ratio = float(ag_ratio)
		sgpt = float(sgpt)
		sgot = float(sgot)
		alkphos = float(alkphos)
		tot_proteins = float(tot_proteins)
		pred= np.array([[age,gender,tot_bilirubin,direct_bilirubin,tot_proteins,albumin,ag_ratio,sgpt,sgot,alkphos]])
		model = joblib.load('model.pkl')
		my_pred = model.predict(pred)
		print(my_pred)
	return render_template('liver.html', prediction = my_pred)



if __name__ =='__main__':
	app.run(debug=True)