# _*_ coding:utf-8 _*_

import psycopg2
import psycopg2.extras

class PsyBase():

    conn = psycopg2.connect(database="renhuai", user="huangkaijie",
                            cursor_factory=psycopg2.extras.RealDictCursor,
                            password="edison", host="47.93.5.189")
    cursor = conn.cursor()

    @classmethod
    def fetch_one(cls,operation):
        cls.cursor.execute(operation)
        return cls.cursor.fetchone()

    @classmethod
    def find_user(cls, phone_number=None):
        if not phone_number:
            return {"code":20002,"msg": "参数错误"}
        user = cls.fetch_one("select * from renhuai_user where phone_number=%s" %phone_number)
        return user
