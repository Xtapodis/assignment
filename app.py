from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "assignment1"
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/hello", methods=["GET"])
def hello():
	return render_template("index.html", hello_text = "Hello there!")