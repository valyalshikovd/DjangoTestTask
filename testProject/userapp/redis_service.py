from django_redis import get_redis_connection


def add_cache(key, data, ex):
    redis_conn = get_redis_connection("default")
    redis_conn.set(key, data, ex=ex)

def get_cache(key):
    redis_conn = get_redis_connection("default")
    value = redis_conn.get(key)
    return value.decode("utf-8")