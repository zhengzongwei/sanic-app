# sanic-app Created by zhengzongwei on 2021/04/07
# Copyright (c) 2021 zhengzongwei. All rights reserved.

from sanic import Sanic

from app.api.v1 import api


def create_app(config=None):
    app = Sanic(__name__)

    app.blueprint(api.api_v1, url_prefix="/")
    return app
