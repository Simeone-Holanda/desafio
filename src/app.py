from flask import Flask
from src.api.card.card_api import CardAPI
from src.api.tag.tag_api import TagAPI

app = Flask(__name__)

app.secret_key = "my secret key"

app.register_blueprint(CardAPI)
app.register_blueprint(TagAPI)

