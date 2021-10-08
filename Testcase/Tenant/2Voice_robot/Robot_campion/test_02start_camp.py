#coding=gbk
from Common.get_token import Login_Token
import Common.public_tenant_api
from Config.public_config import Get_Config
import Common.public_tenant_api
import  pytest
import allure
import time
import json
from Common.Db_pg_conn import DB_pg

config =Get_Config()
token = Login_Token()
db_conn= DB_pg()
header1 = token.json_header('tenant')  # 实例json根式的头
header2 = token.upload_header('tenant')  # 实例上传文件用的头
test_file = config.get_robot_testfile()
real_file = Common.public_tenant_api.upload_file(header2, test_file)
#camp_name = '自动化人机活动' + str(int(time.time()))
instid=config.get_robot_instid()
flowid=config.get_robot_flowid()
callno=config.get_robot_callno()
ws_url = token.get_ws_url()  # 生成websocket连接
socketid = token.get_socketid(ws_url)
print('socketid:',socketid)
# 测试数据
test_datas =  [({"action":1,"socketId":socketid},["\u6210\u529F!",2,True],"启动人机活动，正向用例")]
@allure.epic("活动管理")    #根目录
@allure.feature("人机活动")   #功能模块
@allure.story("启动人机活动")   #功能模块下的分支
@allure.link("https://redmine.lingban.cn/")  #链接
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
# @pytest.mark.skip()
def test_02(test_input,expected,title):
    '''启动人机活动'''
    camp_name= '自动化人机活动' + str(int(time.time()))
    # input_json={"name":camp_name,"speaker":"YAY","instId":instid,"flowId":flowid,"callingNo":callno,"callingTimeout":30,
    #              "file":real_file,"socketId":socketid,"fileName":test_file}
    input_json = {	"instId": instid,	"name": camp_name,	"flowId": flowid,	"version": -1,	"auditStatus": 1,	"type": 1,	"bizData": "{\"bizType\": [\"满意度调查\"]}",	"ratio": 3,	"callingNo": callno,	"speaker": "YAY",	"ttsMale": "",	"ttsFemale": "",	"ttsPolicy": 0,	"concurrency": 1,	"files": [{		"localName": real_file,		"name": test_file	}],	"callingTimeout": 30,	"rule": 0,	"callInterval": 1,	"callStrategy": "standard",	"timeAfterCall": 30,	"ztransfer": 3,	"checked": False,	"repeatCheckDays": "",	"params": [{		"comment": "",		"contact": False,		"dataMapping": [],		"dataType": "phoneNumber",		"debugValue": "",		"defaultValue": "",		"dimension": False,		"experienceValue": "",		"foreignKey": False,		"index": True,		"name": "电话号码",		"output": True,		"output_round": False,		"readable": False,		"required": True,		"status_vals": [],		"type": "",		"upload": True,		"values": [],		"variable": "phone",		"writable": False	}],	"maxAttempts": 0,	"attemptCondition": 0,	"attemptWay": 0,	"attemptStrategys": [],	"workOrder": 0,	"file": real_file,	"socketId": socketid,	"fileName": test_file,	"schedulerTimeList": [{		"startTime": "08:30",		"endTime": "12:00",		"order": 1	}, {		"startTime": "12:00",		"endTime": "24:00",		"order": 2	}],	"groupDn": "",	"groupName": ""}
    res = Common.public_tenant_api.robot_camp_save(header1,input_json)
    print('活动名称：',camp_name)
    print('创建活动接口返回::',res)
    print('campaignuuid:', json.loads(res)['data']['campaignUuid'])
    camp_uuid = json.loads(res)['data']['campaignUuid']
    test_input["camp_uuid"]=camp_uuid
    time.sleep(10)
    operation_res=Common.public_tenant_api.camp_operation(header1,test_input)
    print('启动活动接口返回：',operation_res)
    msg=json.loads(operation_res)['msg']
    time.sleep(10)
    sql = 'select state from campaign where  campaign_uuid=\'' + camp_uuid + '\';'
    print('核查语句sql:::', sql)
    result = db_conn.select("outbound", sql)
    time.sleep(200)
    sql1 = 'select execute_numbers from campaign where  campaign_uuid=\'' + camp_uuid + '\';'
    print('核查语句sql:::', sql1)
    result1 = db_conn.select("outbound", sql1)
    for rec1 in result1:
        execute_numbers = rec1[0]
    if result is not None:
        for rec in result:
             camp_state=rec[0]
    else:
             camp_state=888
             execute_numbers=rec1[0]
    if execute_numbers>0:
        exe_result=True
    else:
        exe_result=False
    list_res = []
    list_res.append(msg)
    list_res.append(camp_state)#校验活动状态'状态:0-规划中;2-已启用;3-停止中;4-已停止;5-已完成;7-已取消
    list_res.append(exe_result)

    print('活动状态state:', camp_state)
    print('执行数量:',execute_numbers)

    assert   list_res==expected ,'请核查接口'