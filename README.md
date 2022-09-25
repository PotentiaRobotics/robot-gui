# Robot GUI

A web server GUI hosted by flask which can be used to control the robot in manual, semi-automatic, and automatic modes.
The web server is meant to run on a flask backend, but we currently just run it on vanilla HTML and CSS with no backend; we plan on integrating it with flask in the very near future.

### Code Description

`bare/` Files containing the actual vanilla server, with vanilla HTML and CSS code.

-   `bare/index.html` is the main HTML file of the server.
-   `bare/style.css` is the main CSS file of the server. Currently is just vanilla without tailwind framework.
-   All other files are images used in the server.

All of our other files are related to the flask backend, but do not contain any meaningful server code:

-   `static/` contains placeholder CSS files to be integrated into the flask application.
-   `templates/` contains placeholder HTML filess to be integrated into the flask application.
-   `app.py` is the flask application to be run. If backend were integrated the command to initiate the server is `python app.py`.
-   `tailwind.config.js` configures tailwind.

### Setup and Run.

1. Clone this repo

```
git clone https://github.com/PotentiaRobotics/robot-gui.git
```

2. `cd` to `bare/` directory

```
cd bare/
```

3. Run live server on `index.html` or open `index.html` with web browser
