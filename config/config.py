import os


class BaseConfig(object):
    TIMEZONE = "Asia/Shanghai"
    # C:/Users/zzw/Documents/GitHub/sanic-app
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DEBUG = False


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
