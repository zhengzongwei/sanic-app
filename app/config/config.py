# sanic-app Created by zhengzongwei on 2021/04/07
# Copyright (c) 2021 zhengzongwei. All rights reserved.

import logging
class BaseConfig(object):
    TIMEZONE = "Asia/Shanghai"
    # C:/Users/zzw/Documents/GitHub/sanic-app
    DEBUG = False
    access_log = False



class DevelopConfig(BaseConfig):
    DEBUG = True


class ProductConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    DEBUG = True


config_map = {
    'develop': DevelopConfig,
    'product': ProductConfig,
    'test': TestConfig
}
