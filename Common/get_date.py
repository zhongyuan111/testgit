import time
from datetime import datetime
import datetime



def get_starttime():
    '''当日零点'''
    start_time = int(time.mktime(time.strptime(str(datetime.date.today()), '%Y-%m-%d'))) * 1000

    return start_time

def get_endtime():
    '''当日24点'''
    end_time = int(time.mktime(time.strptime(str(datetime.date.today()), '%Y-%m-%d'))) * 1000 + 86399000
    return end_time

def get_timestr():
    '''当前年月日时分秒拼串'''
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday

    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    second = time.localtime().tm_sec
    # print(year, '年', month, '月', day, '日')
    # print(hour, '时', minute, '分', second, '秒')

    timestr = str(year) + str(month).rjust(2,'0') + str(day).rjust(2,'0') + str(hour).rjust(2,'0') + str(minute).rjust(2,'0') + str(second).rjust(2,'0')

    return timestr

















