import os

class Config:
    '''Gneral configuration parent class'''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key=dfc385bebd34c4267e25678a7c9ad113'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ph:Student11@localhost/watchlist'

class ProdConfig(Config):
    '''Production configuration child class 
        Args:
            Config: parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''Development configuration chid class
        Args:
            Config:The parent config class with general config settings
    '''
    DEBUG = True

config_options ={
    'development':DevConfig,
    'production':ProdConfig
}