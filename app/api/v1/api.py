# sanic-app Created by zhengzongwei on 2021/04/07
# Copyright (c) 2021 zhengzongwei. All rights reserved.


from sanic.response import json

from sanic import Blueprint

api_v1 = Blueprint("api", __name__)


@api_v1.route("/")
async def index(request):
    data = {
        "api": "v1"
    }
    return json(data)
