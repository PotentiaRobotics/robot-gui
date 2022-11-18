# Robot GUI

A web server GUI hosted by flask which can be used to control the robot in manual, semi-automatic, and automatic modes.
The web server is meant to run on a flask backend, but we currently just run it on vanilla HTML and CSS with no backend; we plan on integrating it with flask in the very near future.

### Code Description

As of now, the code **is** integrated with the flask server, which is able to send commands to the RaspberryPi via python's socket library.

-   `static/` contains CSS files integrated into the flask application for styling purposes.
-   `templates/` contains the HTML pages we display in our gui.
-   `app.py` is the flask application to be run. This features both intialization of pages and can send/recieve commands 
-   `tailwind.config.js` configures tailwind.

### Setup and Run.

1. Clone this repo

```
git clone https://github.com/PotentiaRobotics/robot-gui.git
```

2. Install required libraries (`requirements.txt` to be generated, for now just install what is required in `app.py`)

3. Set up RaspberryPi server code (to be uploaded to this repo) and allow port 2345 and 2346

4. Run server code on the RaspberryPi
```
python server1.py
```

5. Initialize client
```
python app.py
```
