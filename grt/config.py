class Config:
    DEBUG = True


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/grt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '42e1260049e4e519708099a926b24761fa28e347c6710f9c859b8e4d285a7603'


class Production(Config):
    DEBUG = False
