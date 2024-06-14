class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'geo'
    MYSQL_PASSWORD = 'N1usuario'
    MYSQL_DB = 'usuarios_pro_adm'


config = {
    'development': DevelopmentConfig
}
