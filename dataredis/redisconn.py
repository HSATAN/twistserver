# _*_ coding:utf-8 _*_
import redis

class BaseRedis():

    r = redis.Redis(host='47.93.5.189',db=0)
    @classmethod
    def reopen(cls):
        try:
            cls.r = redis.Redis(host='47.93.5.189',db=0)
        except Exception as e:
            print(e)

    @classmethod
    def set(cls,key, number):
        cls.r.set(key, number)
        pass

    @classmethod
    def update(cls,key,number):
        cls.r.incr(key,number)

