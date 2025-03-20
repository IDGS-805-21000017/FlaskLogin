import os
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave_secreta_muy_segura_123456789')
    SESSION_COOKIE_SECURE = False
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY', 'clave_csrf_muy_segura_123456789')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:password@localhost/bdidgs805?charset=utf8mb4')
    SQLALCHEMY_TRACK_MODIFICATIONS = False