# sanic-app Created by zhengzongwei on 2021/04/07
# Copyright (c) 2021 zhengzongwei. All rights reserved.

from sanic import Sanic
from config.config import config_map
# from config.log_config import LOG_SETTINGS
from sqlalchemy.ext.asyncio import create_async_engine

from api import api_v1


def create_app(config=None):
    app = Sanic(__name__)
    app.config.update_config(config_map[config])
    app.ctx.db = config_map[config].SQLALCHEMY_DATABASE_URI

    app.blueprint(api_v1, url_prefix="/")

    return app
