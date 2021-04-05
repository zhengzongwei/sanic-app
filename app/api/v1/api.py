from api import api_v1 as api
from sanic.response import json

@api.route("/")
async def index(request):
    data = {
        "api":"v1"
    }
    return json(data)