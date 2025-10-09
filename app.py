from flask import Flask, render_template

app = Flask(__name__)

#a route to the home page
@app.route('/')
def index():
    return "Welcome to my Flask App home page"

#a new route to the greet page of our website
@app.route("/greet/<name>")
def GreetPage(name):
    return render_template("index.html", name=name)

if __name__ == '__main__':
    app.run(debug = True)