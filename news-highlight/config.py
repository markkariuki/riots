import os

class Config:


    NEWS_API_KEY = 'e2213e59a10643e1a9bfd7cdf3ee86b9'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources/{}?apiKey{}'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

Config_options = {
'develpment':DevConfig,
'production':ProdConfig
}
