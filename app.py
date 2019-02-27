from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def say_hello_to():
return render_template("index.html")

@app.route("/<name>")
def say_hello_to(name):
  return f"hello {name}""

app.run(debug=True)

