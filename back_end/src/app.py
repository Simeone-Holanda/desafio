from flask import Flask
from src.api.card.card_api import CardAPI
from src.api.tag.tag_api import TagAPI
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)

SWAGGER_URL = '/v1/reference'
API_URL = '/static/swagger.yaml'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Documentation"
    }
)
app.secret_key = "my secret key"
CORS(app)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(CardAPI)
app.register_blueprint(TagAPI)

