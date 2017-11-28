# project/server/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    SECRET_KEY = 'secret.key'#open(os.path.join(basedir, 'secret.file')).read()
    DEBUG = False
    API_PER_PAGE = 100


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    API_USERNAME = 'a@pi.com'
    API_PWD = 'api123'
    API_URL = 'http://127.0.0.1:5000/api/'
    TEAM_SERVER = 'SLAWEK\MSSQLSERVER01'
    TEAM_DATABASE = 'TeamExport'
    TEAM_USER = 'teampolska'
    TEAM_PWD = 'teampolska'