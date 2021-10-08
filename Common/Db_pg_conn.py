#coding=gbk
import psycopg2
import logging
import sys
from Config.public_config import  Get_Config
import json
# 加入日志
# 获取logger实例
logger = logging.getLogger("baseSpider")
# 指定输出格式
formatter = logging.Formatter('%(asctime)s\
              %(levelname)-8s:%(message)s')
# 文件日志
file_handler = logging.FileHandler("operation_database.log")
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# 为logge添加具体的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)

get_config=Get_Config()

class DB_pg():
    # 用来查询表数据
    def select(self,db,sql):

        host=json.loads(get_config.get_pg_conn())['host']
        user=json.loads(get_config.get_pg_conn())['user']
        password=json.loads(get_config.get_pg_conn())['password']
        port=json.loads(get_config.get_pg_conn())['port']
        # print(get_config.get_pg_conn()['user'])
        # print(get_config.get_pg_conn()['password'])
        conn = psycopg2.connect(host=host, user=user,
                                password=password, database=db, port=port)
        cur=conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        print('查询语句返回结果:',result)
        cur.close()
        conn.close()
        return result
