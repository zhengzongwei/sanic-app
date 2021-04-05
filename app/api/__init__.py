from sanic import Blueprint


api_v1 = Blueprint("api",__name__)

from .v1 import api