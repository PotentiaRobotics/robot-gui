# app.py

from flask import Flask, render_template, request
from flask_assets import Bundle, Environment
import random
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
        s.settimeout(5)
        s.connect((host,port))
        s.send(str(rot).encode())
        rece=s.recv(1024)
        print("Received",rece)
        s.close()
        rece = "Confirm Sent: "+rece.decode("ASCII")
        return render_template("index.html", conf=rece)
    except ValueError:
        return render_template("index.html", conf='Invalid Input "'+rot+'"')
    except:
        return render_template("index.html", conf='Timeout: Unable to reach Pi')
@app.context_processor
def inject_load1():
    deg = [int(random.random() * 100) / 100 for _ in range(3)]
    return {'load1': deg[0], 'load2': deg[1], 'load3' :deg[2]}
if __name__ == "__main__":
    app.run(debug=True)

