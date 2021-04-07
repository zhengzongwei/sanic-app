from sanic import Sanic
from config.config import config_map
from api import api_v1



def create_app(config=None):

    app = Sanic(__name__)
    app.config.update_config(config_map[config])

    app.blueprint(api_v1,url_prefix="/")

    return  app

