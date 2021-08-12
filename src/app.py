from flask import Flask

app = Flask(__name__)

app.secret_key = "my secret key"


@app.route("/", methods=['GET'])
def test():
    return "Start challenge!.!.!"
