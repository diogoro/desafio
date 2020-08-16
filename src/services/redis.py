import redis
import os

try:
    address = os.environ['REDIS_ADDRESS']
    port = os.environ['REDIS_PORT']
    r = redis.Redis(host=address, port=port, db=0)
except Exception as e:
    r = redis.Redis(host="localhost", port='6379', db=0)


def save(key, value):
    r.set(key, value)


def get(key):
    return r.get(key)


def delete(key):
    r.delete(key)

