from sanic import Sanic
from api import api_v1


def create_app():

    app = Sanic(__name__)

    app.blueprint(api_v1,url_prefix="/")

    return  app

