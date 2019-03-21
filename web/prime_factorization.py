#!/usr/bin/env python3

import time
import math
import time
from flask import Flask, request, render_template, flash
from wtforms import Form, IntegerField, validators

import os
from flask import send_from_directory


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b617sd199l'


class ReusableForm(Form):
	number = IntegerField("Please input integer number to factorise:", 
		validators=[
		validators.DataRequired(), 
		validators.NumberRange(min=1)
		])


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET', 'POST'])
def calculate():
	form = ReusableForm(request.form)

	n = 100

	if request.method == 'POST':
		n = int(request.form['number'])

	if form.validate():

		factors = []

		start_time = time.time()

		while n % 2 == 0:
			factors.append(2)
			n = n // 2

		for i in range(3, int(math.sqrt(n)) + 1, 2):
			while n % i == 0:
				factors.append(i)
				n = n // i

		if (n > 2):
			factors.append(n)

		message =  "Factors: [" + " * ".join([str(i) for i in factors]) + "]" + \
		"    " + ' Execution time: [{:.7f} seconds]'.format(time.time() - start_time) 

		flash(message)
	else:
		flash('Error. Please try again to input integer greater than 0.')

	return render_template('calc.html', form=form)


@app.route('/livetest')
def livetest():
	return "TEST OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 80)
