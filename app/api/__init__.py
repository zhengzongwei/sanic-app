# sanic-app Created by zhengzongwei on 2021/04/07
# Copyright (c) 2021 zhengzongwei. All rights reserved.

from sanic import Blueprint


api_v1 = Blueprint("api",__name__)

from .v1 import api