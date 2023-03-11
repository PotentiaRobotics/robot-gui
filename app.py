# app.py

from flask import Flask, render_template, request, jsonify
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

#Modify to get data
@app.route('/api/datapoint')
def api_datapoint():

    deg = [int(random.random() * 100) / 100 for _ in range(3)]
    dictionary_to_return = {
        'angle1': deg[0],
        'angle2': deg[1],
        'angle3': deg[2]
    }

    return jsonify(dictionary_to_return)


@app.route("/sendData", methods =["GET", "POST"])
def sendData():
            
    rot = request.form.get("rot")
    try:
        rot = int(rot)%360
        rot = rot-360 if rot > 180 else rot
        print("Activated")
        import socket
        s=socket.socket()
        host="raspberrypi"       #This is your Server IP!
        port=2345
        s.settimeout(10)
        s.connect((host,port))
        s.send(str(rot).encode())
        rece=s.recv(1024)
        print("Received",rece)
        s.close()
        rece = "Confirm Sent: "+rece.decode("ASCII")
        return render_template("manual.html", conf=rece)
    except ValueError:
        return render_template("manual.html", conf='Invalid Input "'+rot+'"')
    except:
        return render_template("manual.html", conf='Timeout: Unable to reach Pi')

if __name__ == "__main__":
    app.run(debug=True)

