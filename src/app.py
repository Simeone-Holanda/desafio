from flask import Flask
from src.api.card.card_api import CardAPI
from src.api.tag.tag_api import TagAPI
from flask_cors import CORS
app = Flask(__name__)

app.secret_key = "my secret key"
CORS(app)

app.register_blueprint(CardAPI)
app.register_blueprint(TagAPI)

