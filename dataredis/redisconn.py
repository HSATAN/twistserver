# _*_ coding:utf-8 _*_
import redis

class BaseRedis():
    IP = '39.107.240.28'
    r = redis.Redis(host=IP, db=0)
    @classmethod
    def reopen(cls):
        try:
            cls.r = redis.Redis(host=cls.IP, db=0)
        except Exception as e:
            print(e)

    @classmethod
    def set(cls,key, number):
        cls.r.set(key, number)
        pass

    @classmethod
    def update(cls,key,number):
        cls.r.incr(key,number)

