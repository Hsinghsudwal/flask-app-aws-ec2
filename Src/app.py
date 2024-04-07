from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_docker():
    return "<h1> This app for flask and docker.</h1><br><p>This Devops layout approch, with basic set-up.</p> "


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
