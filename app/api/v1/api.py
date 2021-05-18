# sanic-app Created by zhengzongwei on 2021/04/07
# Copyright (c) 2021 zhengzongwei. All rights reserved.

from api import api_v1 as api
from sanic.response import json


@api.route("/")
async def index(request):
    data = {
        "api": "v1"
    }
    return json(data)