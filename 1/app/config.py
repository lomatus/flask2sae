#config.py

class Config(object):
    DEBUG = False
    TESTING = False
    USERNAME = 'admin'
    PASSWORD = 'flask2sae'
    SECRET_KEY= 'flask2sae secret key'
    THREADS_PER_PAGE = 8

class ProductionConfig(Config):
    import os
    CONNECTION_STR = ''
    if 'SERVER_SOFTWARE' in os.environ:
        import sae
        from sae.const import (MYSQL_HOST,MYSQL_HOST_S,MYSQL_PORT,MYSQL_USER,MYSQL_PASS,MYSQL_DB)
        CONNECTION_STR = 'mysql://'+MYSQL_USER+':'+MYSQL_PASS+'@'+MYSQL_HOST+':'+MYSQL_PORT+'/'+MYSQL_DB
    SQLALCHEMY_DATABASE_URI = CONNECTION_STR

class DevelopmentConfig(Config):
    DEBUG = True
    import os
    _basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')

class TestingConfig(Config):
    TESTING = True