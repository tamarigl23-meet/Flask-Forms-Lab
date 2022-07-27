from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

username = "Tamari"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]

@app.route('/', methods=['GET', 'POST'])
def login_page():
		if request.method == 'GET':
				return render_template('login.html')
		else:
				username1 = request.form['username']
				password1 = request.form['password']

				if username == username1 and password== password1:
						return redirect(url_for('home'),
						user_check = username,
						pass_check = password)

				else:
						return render_template('login.html')

@app.route('/home')
def home_page():
      return render_template('home.html')

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)