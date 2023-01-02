# sanic-app Created by zhengzongwei on 2021/04/07
# Copyright (c) 2021 zhengzongwei. All rights reserved.

import os
import logging
# from sqlalchemy.ext.asyncio import create_async_engine


class BaseConfig(object):
    TIMEZONE = "Asia/Shanghai"
    # C:/Users/zzw/Documents/GitHub/sanic-app
    DEBUG = False
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    access_log = False


class DevelopConfig(BaseConfig):
    DEBUG = True
    USERNAME = 'develop'
    PASSWORD = 'develop'
    HOSTNAME = '127.0.0.1'
    PORT = 3306
    DBNAME = 'snaic'
    # SQLALCHEMY_DATABASE_URI = create_async_engine(
    #     "mysql+aiomysql://%s:%s@%s:%d/%s" % (USERNAME, PASSWORD, HOSTNAME, PORT, DBNAME))


class ProductConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    DEBUG = True


config_map = {
    'develop': DevelopConfig,
    'product': ProductConfig,
    'test': TestConfig
}
