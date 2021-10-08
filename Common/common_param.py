# coding=gbk
import json
import random
import os
import time
from Common.get_token import Login_Token
import Common.public_tenant_api
from Config.public_config import Get_Config
from Common.Db_pg_conn import DB_pg
import datetime

# 配置文件目录
# 配置文件目录
root_dir = os.path.dirname(os.path.abspath('.'))  # 获取项目根目录的相对路径
#file_path = os.path.dirname(os.path.abspath('.')) + '\\auto_4.0\Config\camp.ymal'
config = Get_Config()
token = Login_Token()
db_conn= DB_pg()

header1 = token.json_header('tenant')  # 实例json根式的头
header2 = token.upload_header('tenant')  # 实例上传文件用的头
test_file = config.get_robot_testfile()
test_file1 = config.get_mixrobot_testfile()
real_file = Common.public_tenant_api.upload_file(header2, test_file)
real_file1 = Common.public_tenant_api.upload_file(header2, test_file1)
# camp_name = '自动化人机活动' + str(int(time.time()))
instid = config.get_robot_instid()
instid1=config.get_mixrobot_instid()
flowid = config.get_robot_flowid()
flowid1=config.get_mixrobot_flowid()
callno = config.get_robot_callno()
ws_url = token.get_ws_url()  # 生成websocket连接
socketid = token.get_socketid(ws_url)
groupid = config.get_mixrobot_groupid()
groupdn = config.get_mixrobot_groupdn()
ccid = config.get_mixrobot_ccid()
groupname = config.get_mixrobot_groupname()
tenant_id=config.get_tenant_id()
year_now=datetime.datetime.now().year
month_now=datetime.datetime.now().month
real_month=str(month_now).zfill(2)
class Common_param():
    def pre_campinon(self):
       camp_name = '自动化人机活动' + str(int(time.time()))
       # inputstr={"name": camp_name, "speaker": "YAY", "instId": instid, "flowId": flowid,"callingNo": callno,"callingTimeout": 30,"file": real_file, "socketId": socketid, "fileName": test_file,"action":1}
       #inputjson=json.dumps(inputstr,ensure_ascii=False)
       inputstr ={	"instId": instid,	"name": camp_name,	"flowId": flowid,	"version": -1,	"auditStatus": 1,	"type": 1,	"bizData": "{\"bizType\": [\"满意度调查\"]}",	"ratio": 3,	"callingNo": callno,	"speaker": "YAY",	"ttsMale": "",	"ttsFemale": "",	"ttsPolicy": 0,	"concurrency": 1,	"files": [{		"localName": real_file,		"name": test_file	}],	"callingTimeout": 30,	"rule": 0,	"callInterval": 1,	"callStrategy": "standard",	"timeAfterCall": 30,	"ztransfer": 3,	"checked": False,	"repeatCheckDays": "",	"params": [{		"comment": "",		"contact": False,		"dataMapping": [],		"dataType": "phoneNumber",		"debugValue": "",		"defaultValue": "",		"dimension": False,		"experienceValue": "",		"foreignKey": False,		"index": True,		"name": "电话号码",		"output": True,		"output_round": False,		"readable": False,		"required": True,		"status_vals": [],		"type": "",		"upload": True,		"values": [],		"variable": "phone",		"writable": False	}],	"maxAttempts": 0,	"attemptCondition": 0,	"attemptWay": 0,	"attemptStrategys": [],	"workOrder": 0,	"file": real_file,	"socketId": socketid,	"fileName": test_file,	"schedulerTimeList": [{		"startTime": "08:30",		"endTime": "12:00",		"order": 1	}, {		"startTime": "12:00",		"endTime": "24:00",		"order": 2	}],	"groupDn": "",	"groupName": ""}
       res = Common.public_tenant_api.robot_camp_save(header1, inputstr)
       print('活动名称：', camp_name)
       print('创建活动接口返回::', res)
       print('campaignuuid:', json.loads(res)['data']['campaignUuid'])
       camp_uuid = json.loads(res)['data']['campaignUuid']

       time.sleep(10)
       inputstr['camp_uuid']= camp_uuid
       inputstr1 ={"action":1,"camp_uuid":camp_uuid,"socketId":socketid}
       Common.public_tenant_api.camp_operation(header1,inputstr1)
       time.sleep(100)
       sql = 'select id,state from campaign where  campaign_uuid=\'' + camp_uuid + '\';'
       sql1= 'select call_id,call_time from calling_info_'+str(year_now)+real_month+' where tenant_id='+tenant_id+'and campaign_uuid=\''+camp_uuid+'\'  and is_answer=1;'
       print('核查语句sql:::', sql,sql1)
       result = db_conn.select("outbound", sql)
       result1 = db_conn.select("contact", sql1)
       camp_state=0
       id=0
       return_list=[]
       return_list.append(camp_name)
       return_list.append(camp_uuid)
       for rec in result:
           camp_id=rec[0]
           camp_state = rec[1]
           return_list.append(camp_id)

       for rec1 in result1:
           call_id=rec1[0]
           call_time=rec1[1]
           return_list.append(call_id)
           return_list.append(call_time)
       if camp_state==5:

           return return_list
       else:
           return 'false'

    def pre_campinon1(self):
       camp_name = '自动化人机协同活动' + str(int(time.time()))
       inputstr={
                "bizData":"",
                "instId":instid1,
                "name":camp_name,
                "flowId":flowid1,
                "version":2,
                "auditStatus":1,
                "type":2,
                "ratio":3,
                "callingNo":"15200000001",
                "speaker":"YAY",
                "ttsMale":"",
                "ttsFemale":"",
                "ttsPolicy":0,
                "concurrency":2,
                "callingTimeout":30,
                "rule":0,
                "callInterval":1,
                "callStrategy":"standard",
                "timeAfterCall":30,
                "ztransfer":3,
                "checked":False,
                "repeatCheckDays":"",
                "params":[
                    {
                        "comment":"",
                        "contact":False,
                        "dataMapping":[

                        ],
                        "dataType":"phoneNumber",
                        "debugValue":"",
                        "defaultValue":"",
                        "dimension":False,
                        "experienceValue":"",
                        "foreignKey":False,
                        "index":True,
                        "name":"电话号码",
                        "output":True,
                        "output_round":False,
                        "readable":False,
                        "required":True,
                        "status_vals":[

                        ],
                        "type":"",
                        "upload":True,
                        "values":[

                        ],
                        "variable":"phone",
                        "writable":False
                    }
                ],
                "maxAttempts":0,
                "attemptCondition":0,
                "attemptWay":0,
                "attemptStrategys":[

                ],
                "groupId":groupid,
                "file":real_file1,
                "socketId":socketid,
                "fileName":test_file1,
                "schedulerTimeList":[
                    {
                        "startTime":"08:30",
                        "endTime":"12:00",
                        "order":1
                    },
                    {
                        "startTime":"13:00",
                        "endTime":"20:00",
                        "order":2
                    }
                ],
                "groupDn":groupdn,
                "groupName":groupname,
                "action": 1
            }
       # inputjson=json.dumps(inputstr,ensure_ascii=False)
       res = Common.public_tenant_api.mix_camp_save(header1, inputstr)
       print('活动名称：', camp_name)
       print('创建活动接口返回::', res)
       print('campaignuuid:', json.loads(res)['data']['campaignUuid'])
       camp_uuid = json.loads(res)['data']['campaignUuid']

       time.sleep(10)
       inputstr['camp_uuid'] = camp_uuid
       Common.public_tenant_api.camp_operation(header1,inputstr)
       time.sleep(100)
       sql = 'select id,state from campaign where  campaign_uuid=\'' + camp_uuid + '\';'
       print('核查语句sql:::', sql)
       result = db_conn.select("outbound", sql)
       camp_state = 0
       id=0
       for rec in result:
           id=rec[0]
           camp_state = rec[1]
       if camp_state==5:
           return camp_name,camp_uuid,id
       else:
           return False

    def pre_agentinsertcheck(self):
        '''添加坐席校验'''
        res=Common.public_tenant_api.agent_insertcheck(header1)
        if json.loads(res)["msg"] == '\u6210\u529F!':
            return True
        else:
            return False

    def pre_agentcheckrepeat(self):
        '''批量添加坐席时重复数据校验'''
        startnum=str(random.randint(0,7777)).zfill(4)
        res = Common.public_tenant_api.agents_checkRepeat(header1,startnum)
        print(json.loads(res)["msg"])
        if json.loads(res)["msg"]== '\u6210\u529F!':
            return True
        else:
            return False

    def query_agent(self):
        '''查询坐席列表'''
        res = Common.public_tenant_api.query_agent(header1)
        if json.loads(res)["msg"] == '\u6210\u529F!':
            agent_id = json.loads(res)["data"]["list"][0]["id"]
            return agent_id
        else:
            return False

    def delete_member(self):
        res = Common.public_tenant_api.query_agent(header1)
        agent_id = json.loads(res)["data"]["list"][0]["id"]
        test_input={"agent_id":str(agent_id)}
        res = Common.public_tenant_api.delete_agent(header1, test_input)
        return json.loads(res)["msg"]

