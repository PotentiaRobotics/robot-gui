# app.py

from flask import Flask, render_template, request
from flask_assets import Bundle, Environment
import jyserver.Flask as jsf

app = Flask(__name__)

assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")

assets.register("css", css)
css.build()

@jsf.use(app)
class App:
    def __init__(self) -> None:
        pass

    def printinput(self):
        x = self.js.document.getElementById('userInput').value
        print(x)


@app.route("/")
def homepage():

    return App.render(render_template("index.html"))


if __name__ == "__main__":
    app.run(debug=True)

