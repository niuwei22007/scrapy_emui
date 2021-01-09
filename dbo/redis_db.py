from redis import Connection, ConnectionPool, Redis, StrictRedis
from redlock import RedLockFactory, RedLock

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379


class RedisDB(object):
    def __init__(self):
        self.__redis_pool = ConnectionPool(host=REDIS_HOST, port=REDIS_PORT)
        self.__redis_lock = RedLockFactory(
            connection_details=[
                {'host': REDIS_HOST, 'port': REDIS_PORT},
            ])

    @property
    def client(self):
        return Redis(connection_pool=self.__redis_pool)

    @property
    def lock(self):
        return self.__redis_lock


if __name__ == '__main__':
    redisDB = RedisDB()
    redisDB.client.rpush('a1', 'bbb')
    redisDB.client.hset('a2', 'ip', bytes([127, 0, 0, 1]))
    import json

    redisDB.client.hset('a3', 'ips', json.dumps({'ip': [127, 0, 0, 1]}))
    redisDB.client.flushall()
