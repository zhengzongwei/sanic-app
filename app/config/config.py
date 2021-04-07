

class BaseConfig(object):
    TIMEZONE = "Asia/Shanghai"
    # C:/Users/zzw/Documents/GitHub/sanic-app
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
