from sanic import Sanic
from config.config import config_map
from config.log_config import LOG_SETTINGS
from api import api_v1



def create_app(config=None):

    app = Sanic(__name__)
    app.config.update_config(config_map[config])
    app.config.update_config(LOG_SETTINGS)

    app.blueprint(api_v1,url_prefix="/")

    return  app

