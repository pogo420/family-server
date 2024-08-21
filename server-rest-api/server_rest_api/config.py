# File contains list of application configs for application

class Config:
    """Base config class"""
    APP_NAME = "family server rest app"
    TESTING = False

class ProductionConfig(Config):
    """Production config class"""
    APP_VERSION = "prod:v0.1"


class DevelopmentConfig(Config):
    """Development config class"""
    APP_VERSION = "dev:v0.1"

# Mapping of config
configs = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'default': ProductionConfig
}
