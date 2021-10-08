import pymysql
import logging
import sys
from Common.public_config import  Get_Config

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


class DB_mysql():
    # 构造函数,初始化数据库连接
    def __init__(self,db,sql,params=None):
        self.database=db
        self.sql = sql
        self.params = params
        self.conn = None
        self.cur = None

    def connectiondatabase(self):
        print(Get_Config.get_mysql_conn()['host'],Get_Config.get_mysql_conn()['username'],Get_Config.get_mysql_conn()['password'],Get_Config.get_mysql_conn()['database'],Get_Config.get_mysql_conn()['charset'])
        try:
            self.conn = pymysql.connect(Get_Config.get_mysql_conn()['host'],Get_Config.get_mysql_conn()['username'],
                                    Get_Config.get_mysql_conn()['password'],self.database,charset=Get_Config.get_mysql_conn()['charset'])
        except:
            logger.error("connectDatabase failed")
            return False
        self.cur = self.conn.cursor()
        return True



    # 关闭数据库
    def closedatabase(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True



    # 用来查询表数据
    def select(self):
        self.connectiondatabase()
        self.cur.execute(self.sql,self.params)
        result = self.cur.fetchall()
        print(result)
        return result
