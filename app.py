from flask import Flask, render_template

app = Flask(__name__)

#a route to the home page
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/scroll')
def scroll():
    return render_template("scroller.html")

#a new route to the greet page of our website
@app.route("/greet/<name>")
def GreetPage():
    return "Welcome to my Flask App home page"


if __name__ == '__main__':
    app.run(debug = True)