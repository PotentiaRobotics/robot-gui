# app.py

from flask import Flask, render_template, request
from flask_assets import Bundle, Environment

app = Flask(__name__)

assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")

assets.register("css", css)
css.build()


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/base.html", methods =["GET", "POST"])
def sendData():
            
    rot = request.form.get("rot")
    try:
        rot = int(rot)
        print("Activated")
        import socket
        s=socket.socket()
        host="raspberrypi"       #This is your Server IP!
        port=2345
        s.connect((host,port))
        s.send(str(rot).encode())
        rece=s.recv(1024)
        print("Received",rece)
        s.close()
        rece = "Confirm Sent: "+rece.decode("ASCII")
        return render_template("index.html", conf=rece)
    except ValueError:
        return render_template("index.html", conf='Invalid Input "'+rot+'"')
if __name__ == "__main__":
    app.run(debug=True)

