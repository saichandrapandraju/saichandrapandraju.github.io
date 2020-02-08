from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')

@app.route("/cv")
def cv():
	return render_template("cv.html")

@app.route("/other")
def other():
	return render_template("other.html")
