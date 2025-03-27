from flask_caching import Cache

cache = Cache(config={
    'CACHE_TYPE': 'RedisCache',
    'CACHE_REDIS_URL': 'redis://redis:379/0',
    'CACHE_DEFAULT_TIMEOUT': 300
})

def init_cache(app):
    cache.init_app(app)