
import flask
import requests
import os

app = flask.Flask(__name__)





response = requests.get(BASE_URL, params=params)
data = response.json()
headlines = []

for i in range(0, 10):
    print(data['response']['docs'][i]['headline']['main'])
    headlines.append(data['response']['docs'][i]['headline']['main'])

@app.route("/")
def index():
    return flask.render_template("index.html", headlines=headlines)


app.run()