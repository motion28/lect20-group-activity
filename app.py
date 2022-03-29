
import flask
import requests
import os

app = flask.Flask(__name__)



params = {
    'q': 'braves', # Query keywords
    'api-key': os.getenv(MY_API_SECRET_KEY),
}

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