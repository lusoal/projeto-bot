#For Queue Service on Redis
import redis

class RedisController():

    redis_host = None
    redis_port = None
    redis_password = None

    connect = None

    def __init__(self, redis_host, redis_port, redis_password):
        self.redis_host = redis_host
        self.redis_password = redis_password
        self.redis_port = int(redis_port)
        self.connect = redis.Redis(host=self.redis_host, port=self.redis_port, db=0)

    def push(self, key, value):
        print self.connect
        self.connect.set(key, value)

    def pop(self, key):
        return self.connect.get(key)