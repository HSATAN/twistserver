# _*_ coding:utf-8 _*_

import psycopg2
import psycopg2.extras
import random
defaul_head_url = 'https://www.baidu.com/s?rsv_idx=1&wd=%E5%B8%85%E5%93%A5&usm=3&ie=utf-8&rsv_cq=%E5%9B%BE%E7%89%87&rsv_dl=0_right_recommends_merge_20826&euri=6481626'
class PsyBase():

    conn = psycopg2.connect(database="renhuai", user="huangkaijie",
                            cursor_factory=psycopg2.extras.RealDictCursor,
                            password="edison", host="47.93.5.189")
    cursor = conn.cursor()

    @classmethod
    def fetch_one(cls,operation):
        try:
            cls.cursor.execute(operation)
            return cls.cursor.fetchone()
        except Exception as e:
            print(e)
            return None
    @classmethod
    def run_operation(cls,operation):
        try:
            cls.cursor.execute(operation)
            return cls.conn.commit()
        except Exception as e:
            print(e)
            return None
    @classmethod
    def find_user(cls, phone_number=None):
        if not phone_number:
            return {"code":20002,"msg": "参数错误"}
        user = cls.fetch_one("select * from renhuai_user where phone_number=%s" %phone_number)
        return user

    @classmethod
    def insert_user(cls,name="潇湘妃子", password="123456",phone_number=15326666239,intro="天外飞仙",id_number=522160199107162342):
        id_number = random.random()
        sql = "insert into renhuai_user (phone_number,id_number,name,intro) values (%s,'%s','%s','%s')"%(phone_number,
                                                                                                                  id_number,
                                                                                                                  name,
                                                                                                                  intro)
        print(sql)
        return  cls.run_operation(sql)
