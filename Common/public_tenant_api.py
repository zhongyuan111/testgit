import json
import requests
import os
from Common.get_token  import Login_Token
from Config.public_config import Get_Config
import Common.get_date


public_param = Login_Token()  # 实例化
public_config = Get_Config()  #实例化
# header1 = public_param.json_header('tenant')  # 实例json根式的头
# header2 = public_param.upload_header('tenant')  # 实例上传文件用的头
ws_url = public_param.get_ws_url()  # 生成websocket连接
#socketid = public_param.get_socketid(ws_url)
tenant_url = public_config.get_address_tenant()
tenant_id = public_config.get_tenant_id()
call_no = public_config.get_robot_callno()
called_no = public_config.get_robot_calledno()
inst_id = public_config.get_robot_instid()
mixinst_id = public_config.get_mixrobot_instid()
flow_id = public_config.get_robot_flowid()
mixflow_id = public_config.get_mixrobot_flowid()
cc_id = public_config.get_mixrobot_ccid()
group_id = public_config.get_mixrobot_groupid()
group_dn = public_config.get_mixrobot_groupdn()
group_name = public_config.get_mixrobot_groupname()
start_time = Common.get_date.get_starttime()
end_time = Common.get_date.get_endtime()
now_time = Common.get_date.get_timestr()

def upload_file(head,test_file):
    '''上传外呼文件'''
    upload_path = os.path.dirname(os.path.abspath('.')) + '\\auto_4.0\\up_files\\'

    post_url = tenant_url+'/api/file/upload'
    open_file = open(upload_path + test_file, 'rb')
    file = {'tag': (None, 'task-core'),
            'expireTime': (None, '691200000'),
            'files': (test_file, open_file, 'application/vnd.ms-excel')
            }
    # 执行上传文件接口
    res = requests.post(post_url, files=file, headers=head)
    open_file.close()
    #print('执行上传文件结果：',res.text)
    file_info = json.loads(res.text)['data']
    #print('up_load：',file_info)
    list_info = file_info['list']

    #print('list_info:',list_info)
    file_name = list_info[0]['localName']
    #print('file_name',file_name)
    return file_name


def  mix_camp_save(head,test_input):
    '''创建人机协同活动接口'''
    url = tenant_url+'outbound/campaign/save'
    body = {
            "bizData": "",
            "name": test_input["name"],
            "speaker": "YAY",
            "instId": test_input["instId"],
            "flowId": test_input["flowId"],
            "callingNo": test_input["callingNo"],
            "version": 1,
            "auditStatus": 1,
            "type": 2,
            "ratio": 3,
            "ttsMale": "",
            "ttsFemale": "",
            "ttsPolicy": 0,
            "concurrency": 2,
            "callingTimeout": 30,
            "rule": 0,
            "callInterval": 1,
            "callStrategy": "standard",
            "timeAfterCall": 30,
            "ztransfer": 3,
            "checked": False,
            "repeatCheckDays": "",
            "params": [
                {
                    "comment": "",
                    "contact": False,
                    "dataMapping": [

                    ],
                    "dataType": "phoneNumber",
                    "debugValue": "",
                    "defaultValue": "",
                    "dimension": False,
                    "experienceValue": "",
                    "foreignKey": False,
                    "index": True,
                    "name": "电话号码",
                    "output": True,
                    "output_round": False,
                    "readable": False,
                    "required": True,
                    "status_vals": [

                    ],
                    "type": "",
                    "upload": True,
                    "values": [

                    ],
                    "variable": "phone",
                    "writable": False
                }
            ],
            "maxAttempts": 0,
            "attemptCondition": 0,
            "attemptWay": 0,
            "attemptStrategys": [

            ],
            "groupId": test_input["groupId"],
            "file": test_input["file"],
            "socketId": test_input["socketId"],
            "fileName": test_input["fileName"],
            "schedulerTimeList": [
                {
                    "startTime": "08:30",
                    "endTime": "12:00",
                    "order": 1
                },
                {
                    "startTime": "13:00",
                    "endTime": "20:00",
                    "order": 2
                }
            ],
            "groupDn": test_input["groupDn"],
            "groupName": test_input["groupName"],
            }

    print('body:',body)

    res = requests.post(url,json=body, headers=head)
    print('save:',res.text)
    return res.text

def  robot_camp_save(head,test_input):
    '''创建人机活动接口'''
    url = tenant_url+'outbound/campaign/save'
    # body = {
    #       "name":test_input["name"],
    #       "speaker":test_input["speaker"],
    #       "instId":test_input["instId"],
    #       "flowId":test_input["flowId"],
    #       "callStrategy": "standard",
    #       "callInterval": 1,
    #       "ztransfer": 3,
    #       "callingNo":test_input["callingNo"],
    #       "callingTimeout":30,
    #       "file":test_input["file"],
    #       "socketId":test_input["socketId"],
    #       "fileName":test_input["fileName"],
    #       "schedulerTimeList":[
    #           {
    #               "startTime":"08:30",
    #               "endTime":"12:00",
    #               "order":1
    #           },
    #           {
    #               "startTime":"13:00",
    #               "endTime":"20:00",
    #               "order":2
    #           }
    #       ],
    #       "ratio":1,
    #       "rule":0,
    #       "type":1,
    #       "groupDn":"",
    #       "groupName":""
    #   }
    body ={	"instId": test_input["instId"],	"name": test_input["name"],	"flowId": test_input["flowId"],	"version": -1,	"auditStatus": 1,	"type": 1,	"bizData": "{\"bizType\": [\"满意度调查\"]}",	"ratio": 3,	"callingNo": test_input["callingNo"],	"speaker": test_input["speaker"],	"ttsMale": "",	"ttsFemale": "",	"ttsPolicy": 0,	"concurrency": 1,	"files": [{		"localName": test_input["file"],		"name": test_input["fileName"]	}],	"callingTimeout": 30,	"rule": 0,	"callInterval": 1,	"callStrategy": "standard",	"timeAfterCall": 30,	"ztransfer": 3,	"checked": False,	"repeatCheckDays": "",	"params": [{		"comment": "",		"contact": False,		"dataMapping": [],		"dataType": "phoneNumber",		"debugValue": "",		"defaultValue": "",		"dimension": False,		"experienceValue": "",		"foreignKey": False,		"index": True,		"name": "电话号码",		"output": True,		"output_round": False,		"readable": False,		"required": True,		"status_vals": [],		"type": "",		"upload": True,		"values": [],		"variable": "phone",		"writable": False	}],	"maxAttempts": 0,	"attemptCondition": 0,	"attemptWay": 0,	"attemptStrategys": [],	"workOrder": 0,	"file": test_input["file"],	"socketId": test_input["socketId"],	"fileName": test_input["fileName"],	"schedulerTimeList": [{		"startTime": "08:30",		"endTime": "12:00",		"order": 1	}, {		"startTime": "12:00",		"endTime": "24:00",		"order": 2	}],	"groupDn": "",	"groupName": ""}
    #print('body:',body)
    #print(url)
    res = requests.post(url,json=body, headers=head)
    #print('save:',res.text)
    return res.text

def camp_operation(head,test_input):
    '''启停活动  action 1 启动 2 暂停 3 取消'''
    url =  tenant_url+'outbound/campaign/change/state'
    body = {"action": test_input["action"],
            "campaignUuid": test_input['camp_uuid'],
            "socketId": test_input['socketId']
            }
    res = requests.put(url,json=body,headers=head)
    #print('camp_operation',body)
    return res.text


def camp_query_record(head,camp_id):
    '''查询通话记录'''
    url = tenant_url + 'outbound/campaign/record/list'
    body = {"campaignId":camp_id['id'],
            "startCallTime":start_time,
            "endCallTime":end_time,
            "pageNo":1,
            "pageSize":20,
            "searchType":0,
            "outboundResult": ""
            # "tenantId":tenant_id
            }
    print('record:',body)
    res = requests.post(url,json=body,headers=head)
    print('record:',res.text)
    return res.text


def camp_manage_list(head, camp_name1):
    '''活动管理列表查询接口'''
    url = tenant_url + 'outbound/campaign/manage/list'
    body = {
            "time":[
                start_time,
                end_time
            ],
            "name": camp_name1,
            "pageNo": 1,
            "pageSize": 20,
            "startCreateTime": start_time,
            "endCreateTime": end_time
            }
    res = requests.post(url,json=body,headers=head)
    return res.text


def camp_record_detail(head,cticallid):
    '''通话详情'''
    url = tenant_url + 'outbound/campaign/dialog/list?ctiCallId='+cticallid
    res = requests.get(url,headers=head)
    return res.text

def webhook_send(head,test_input):
    '''webhook查询接口'''
    url = tenant_url+'msg/api/webhook/log'
    body = {
            "startTime":start_time,
            "endTime":end_time,
            "status":"",
            "phone":"",
            "outId":"",
            "taskId":"",
            "event":"",
            "pageNo":test_input['pageNo'],
            "pageSize":100
            }

    res = requests.post(url,json= body ,headers=head)
    return res.text

def outgroup_create(head):
    '''创建技能组-类型：呼出'''
    url = tenant_url+'config/queues'
    body = {"groupName":"自"+now_time,"groupType":0,"strategy":"top-down","callerIdNumber":"18812345671","mohSound":"local_stream://moh","timeAfterCall":30,"maxWaitTime":60,"useExtOrderRecord":"0","orderRecordUrl":"","formData":"","knowledgeGroupIds":[],"enableSatisfaction":"","guideWords":"","failureDate":[1603641600000,1635263999999],"instId":"","flowId":"","tenantId":tenant_id,"businessTemplate":[{"fieldName":"手机号码","fieldType":"input","fieldValue":"","required":True,"options":[]},{"fieldName":"跟进状态","fieldType":"select","fieldValue":"","required":True,"options":[{"name":"成单"},{"name":"跟进低"},{"name":"跟进中"},{"name":"跟进高"},{"name":"放弃"},{"name":"敏感"}]},{"fieldName":"备注","fieldType":"textarea","fieldValue":"","required":True,"options":[]}],"extData":{"satisfaction":{"enable":False}}}

    res = requests.post(url,json=body,headers = head)
    return res.text

def incomegroup_create(head):
    '''创建技能组-类型：呼入'''
    url = tenant_url+'config/queues'
    body = {"groupName":"自"+now_time,"groupType":1,"strategy":"top-down","callerIdNumber":"","mohSound":"local_stream://moh_sax_go_home","timeAfterCall":30,"maxWaitTime":60,"useExtOrderRecord":"0","orderRecordUrl":"","formData":"","knowledgeGroupIds":[],"enableSatisfaction":True,"guideWords":"","failureDate":[1603641600000,1635263999999],"instId":1094,"flowId":2079,"tenantId":tenant_id,"businessTemplate":[{"fieldName":"手机号码","fieldType":"input","fieldValue":"","required":True,"options":[]},{"fieldName":"跟进状态","fieldType":"select","fieldValue":"","required":True,"options":[{"name":"成单"},{"name":"跟进低"},{"name":"跟进中"},{"name":"跟进高"},{"name":"放弃"},{"name":"敏感"}]},{"fieldName":"备注","fieldType":"textarea","fieldValue":"","required":True,"options":[]}],"extData":{"satisfaction":{"enable":True,"instId":1094,"flowId":2079,"robotName":"迭代21","versionName":"工作台版本","startDate":1603641600000,"endDate":1635263999999,"guideWords":""}}}
    res = requests.post(url,json=body,headers = head)
    return res.text

def  group_query(head):
    '''查询技能组'''
    url = tenant_url+'config/queues/list'
    body = {"pageNo":1,"pageSize":100,"groupType":"","groupName":"","callerIdNumber":"","groupSn":"","time":"","tenantId":tenant_id,"createTimeStart":"","createTimeEnd":""}
    res = requests.post(url,json=body,headers= head)
    return res.text


def group_modify(head,group_id,group_name):
    '''修改技能组信息'''
    url = tenant_url+'config/queues/'+str(group_id)
    body = {
            "businessTemplate":[
                {
                    "fieldId":1,
                    "fieldName":"手机号码",
                    "fieldType":"input",
                    "fieldValue":"",
                    "options":[

                    ],
                    "required":"true"
                },
                {
                    "fieldId":2,
                    "fieldName":"跟进状态",
                    "fieldType":"select",
                    "fieldValue":"",
                    "options":[
                        {
                            "id":1,
                            "name":"成单"
                        }
                    ],
                    "required":"true"
                },
                {
                    "fieldId":3,
                    "fieldName":"备注",
                    "fieldType":"textarea",
                    "fieldValue":"",
                    "options":[

                    ],
                    "required":"true"
                }
            ],
            "callerIdNumber":call_no,
            "deleteFlag":0,
            "groupName":group_name,
            "id":group_id,
            "knowledgeGroupIds":[

            ],
            "maxWaitTime":10,
            "mohSound":"local_stream://moh",
            "orderRecordUrl":"",
            "queueName":"1110679007",
            "strategy":"top-down",
            "tenantId":tenant_id,
            "timeAfterCall":20,
            "useExtOrderRecord":"0",
            "queueId":group_id
           }
    res = requests.put(url,json=body,headers=head)
    return res.text


def edit_group_member(head,group_id,member):
    '''编辑技能组成员'''
    url = tenant_url +'config/queues/bindAgent/'+str(group_id)
    if int(member)>999:
       body = {
               "list":[
                   {
                       "name":member,
                       "agentType":0
                   }
               ],
               "tenantId":tenant_id
              }
       res = requests.post(url,json=body,headers= head)
       return res.text
    else:
        body = {
            "list": [],
            "tenantId": tenant_id
        }
        res = requests.post(url, json=body, headers=head)
        return res.text


def  del_group(head,group_id):
    '''删除技能组'''
    url = tenant_url+'config/queues/'+str(group_id)
    res = requests.delete(url,headers=head)
    return res.text



def add_member_check(head):
    '''添加技能组成员校验'''
    url = tenant_url+'config/agents/insertcheck/'+tenant_id
    res = requests.get(url,headers=head)
    return res.text

def query_agent(head):
    '''坐席管理-查询坐席列表'''
    url = tenant_url+'config/agents/list'
    # body = {"pageNo": 1, "pageSize": 100, "tenantId": 111050, "defaultFlag": 0}

    body = {"pageNo":1,"pageSize":100,"agentName":"","name":"","contact":"","agentType":"","queueId":"","status":"","bindPhone":"","tenantId":tenant_id,"defaultFlag":0,"workType":"","time":""}
    res = requests.post(url,json=body,headers=head)
    return res.text

def delete_agent(head,test_input):
    '''删除坐席'''
    url = tenant_url+'config/agents/'+test_input['agent_id']
    res = requests.delete(url,headers=head)
    return res.text


def agent_insertcheck(head):
    '''添加单个坐席校验'''
    url = tenant_url+'config/agents/insertcheck/'+tenant_id
    res = requests.get(url,headers=head)
    return res.text



def add_single_member(head,test_input):
    '''添加单个坐席'''
    url = tenant_url+'config/agents'
    group_l =[]
    group_l.append(group_id)
    body = {
            "name":test_input["member_name"],
            "password":"Lingban2019",
            "agentName":"自动化",
            "agentType":0,
            "bindPhone":"",
            "defaultQueue":group_id,
            "list":group_l,
            "sexuality":1,
            "tenantId":tenant_id
            }
    print(body)
    res = requests.post(url,json=body,headers=head)
    return res.text


def agents_checkRepeat(head,startnum):
    '''批量添加坐席校验重复坐席数据'''
    url = tenant_url+'config/agents/checkRepeat'
    body = {"size":1,"startNum":startnum,"tenantId":tenant_id}
    res = requests.get(url,json=body,headers=head)
    return res.text

def agents_batch(head,test_input):
    '''批量添加坐席提交接口'''
    group_l =[]
    group_l.append(group_id)
    url = tenant_url+'config/agents/batch'
    body ={"size":"1","agentType":0,"startNum":int(test_input['startnum']),"prefix":"lb","password":"Lingban2019","defaultQueue":group_id,"list":group_l,"sexuality":0,"tenantId":tenant_id}
    print(body)
    res = requests.post(url,json=body,headers=head)
    return res.text


def edit_member(head,member_id,member_name):
    '''编辑坐席信息'''
    url = tenant_url+'config/agents/'+str(member_id)
    print('url:',url)
    group_l = []
    group_l.append(group_id)
    body ={
           "agentId":member_id,
           "agentName":"自动化",
           "agentType":0,
           "bindPhone":"",
           "defaultQueue":group_id,
           "defaultQueueName":"默认技能组",
           "domain":"",
           "id":member_id,
           "list":group_l,
           "name":member_name,
           "password":"Lingban2019",
           "sexuality":1,
           "status":0,
           "templateId":-1,
           "userName":str(tenant_id)+str(member_name),
           "validFlag":0,
           "workType":0,
           "tenantId":tenant_id
          }
    print('body:',body)
    res = requests.put(url,json=body,headers=head)
    return res.text


def del_member(head,member_id):
    '''删除坐席'''
    url = tenant_url+'config/agents/'+str(member_id)
    res = requests.delete(url,headers=head)
    return res.text


def qeury_manmachine(head):
    '''统计分析-查询人机协同活动'''
    url = tenant_url+'analysis/statistics/manmachine'
    body = {"campaignId":"","instId":"","flowId":"","startTime":start_time,"endTime":end_time,"pageNo":1,"pageSize":20}
    res = requests.post(url,json=body,headers=head)
    return res.text


def query_agentlog(head):
    '''统计分析-坐席工作日志'''
    url = tenant_url+'analysis/statistics/agent/log'
    body ={"time":[start_time,end_time],"startTime":start_time,"endTime":end_time,"pageNo":1,"pageSize":20}
    print(body)
    res = requests.post(url,json=body,headers=head)
    # print(res)
    return res.text


def query_agentwork(head):
    '''统计分析-坐席工作量'''
    url = tenant_url+'analysis/statistics/agent/work'
    body = {"time":[start_time,end_time],"orderBy":"orderNum","sort":"desc","startTime":start_time,"endTime":end_time,"pageNo":1,"pageSize":20}
    res = requests.post(url,json=body,headers=head)
    return res.text


def  robot_work(head):
    '''统计分析-机器人工作量查询接口'''
    url = tenant_url+'analysis/statistics/robot/work'
    body ={"instId":"","flowId":"","startTime":start_time,"endTime":end_time,"pageNo":1,"pageSize":20}
    res = requests.post(url,json=body,headers=head)
    return res.text

def robot_nomatch(head):
    '''统计分析-机器人未理解分析'''
    url = tenant_url+'analysis/statistics/robot/nomatch'
    body= {"outboundId":"","instId":"","flowId":"","time":[start_time,end_time],"startTime":start_time,"endTime":end_time,"pageNo":1,"pageSize":100}
    res = requests.post(url,json=body,headers=head)
    return res.text

def satisfaction_overview(head):
    '''统计分析-话后满意度统计'''
    url = tenant_url+'analysis/satisfaction/overview?analysisDateStart='+str(start_time)+'&analysisDateEnd='+str(end_time)
    res= requests.get(url,headers=head)
    return res.text


def analysis_callAnalyze(head):
    '''统计分析-通话分析'''
    url =tenant_url+'analysis/callAnalyze'
    body ={"statisticalDimension":1,"statisticType":1,"callType":"","callTimeStart":start_time,"callTimeEnd":end_time,"pageNo":1,"pageSize":100}
    res = requests.post(url,json=body,headers=head)
    return res.text

def campaign_Analyze(head):
    '''统计分析-活动执行分析'''
    url= tenant_url+'analysis/campaignAnalyze'
    body = {"campaignCreateTimeStart":start_time,"campaignCreateTimeEnd":end_time,"resultType":1,"pageNo":1,"pageSize":100}
    res =requests.post(url,json=body,headers=head)
    return  res.text


def query_record_voice(head,test_input):
    '''通话详情中录音查询'''
    url = tenant_url+'records/records/' + test_input['camp_uuid']
    body = {"tenantID": tenant_id}
    res = requests.post(url, json=body, headers=head)
    return res.content

def callerIdNumbers(head):
    '''查询租户下外显号码'''
    url = tenant_url+'config/tenants/'+tenant_id+'/callerIdNumbers'
    print(url)
    res = requests.get(url,headers=head)
    return res.text

def mohsound(head):
    '''技能组-排队音查询'''
    url= tenant_url+'config/global/mohsound'
    res = requests.get(url,headers=head)
    return res.text

def robot_satisfaction(head):
    '''查询租户下满意度机器人'''
    url= tenant_url+'robot/api/robot/instance?name=&pageNo=1&pageSize=100&withFlow=true&outboundFlag=1&bizType=%E6%BB%A1%E6%84%8F%E5%BA%A6%E8%B0%83%E6%9F%A5'
    res = requests.get(url,headers=head)
    return res.text

def departments(head):
    '''部门列表查询'''
    url = tenant_url+'crm/api/departments?pageNo=1&pageSize=20'
    res = requests.get(url,headers=head)
    return res.text

def department(head,test_input):
    '''添加部门 action:1 ;更新部门信息 action:2'''
    url = tenant_url + 'crm/api/department'
    body = {"name": "部门", "remark": ""}
    if test_input['action']==1:
        res =requests.post(url,json=body,headers=head)
        return res.text
    if test_input['action']==2:
        url1 = url+'/'+test_input['deptid']
        body = {"name":"部门","remark":""}
        res =requests.put(url1,json=body,headers=head)
        return res.text


def robot_instance_allocate(head,test_input):
    '''部门管理-分配机器人'''
    url =tenant_url+'robot/api/robot/instance/allocate'
    body = {"deptId":test_input['deptid'],"instanceIds":[inst_id]}
    res = requests.post(url,json=body,headers=head)
    return res.text


def department_swith(head,test_input):
    '''关闭部门'''
    url = tenant_url+ 'crm/api/department/'+str(test_input['deptid'])+'/switch'
    body = {"validFlag":0}
    res = requests.put(url,json=body,headers=head)
    return res.text


def users_list(head):
    '''用户管理-用户列表查询'''
    url = tenant_url+'crm/api/users?pageNo=1&pageSize=100'
    res = requests.get(url,headers=head)
    return res.text

def user_add(head):
    '''用户管理-添加用户'''
    url = tenant_url+'crm/api/user'
    body = {"fullName":"自动化","password":"Lingban2019","userName":"auto"+now_time,"email":""}
    print('用户管理-添加用户',body)
    res =requests.post(url,json=body,headers=head)
    return res.text

def user_delete(head,test_input):
    '''用户管理-删除用户'''
    url = tenant_url+'crm/admin/api/user/'+str(test_input['user_id'])
    res = requests.delete(url,headers=head)
    return res.text


def password_reset(head,test_input):
    '''用户管理-重置密码'''
    url = tenant_url+'crm/api/user/'+str(test_input['user_id'])+'/password'
    res= requests.get(url,headers=head)
    return res.text

def allot_dept(head,test_input):
    '''用户管理-批量分配部门'''
    url = tenant_url+'crm/api/department/'+str(test_input['deptid'])+'/allot'
    body = {"idList":[test_input['user_id']]}
    res = requests.post(url,json=body,headers=head)
    return  res.text

def allot_role(head,test_input):
    '''用户管理-分配角色'''

    url = tenant_url+'crm/api/user/'+str(test_input['user_id'])+'/role/allot'
    # print('用户管理-分配角色', url)
    body = {"idList":[test_input['role_id']]}
    # print('用户管理-分配角色',body)
    res=requests.post(url,json=body,headers=head)
    return res.text




def api_role(head):
    '''添加角色'''
    url =tenant_url+'crm/api/role'
    body = {"name":"角色","description":"","client":"aicc_cp"}
    res=requests.post(url,json=body,headers=head)
    return res.text

def valid_role(head,test_input):
    '''角色管理-启用：valid=1，禁用：valid=0'''
    url = tenant_url+'crm/api/role/'+str(test_input['role_id'])+'/valid'
    body ={"validFlag":0}
    body1 ={"validFlag":1}
    if test_input['valid']==0:
        res= requests.put(url,json=body,headers=head)
        return res.text
    elif test_input['valid']==1:
        res =requests.put(url,json=body1,headers=head)
        return res.text


def permission_allot(head,test_input):
    '''角色管理-分配权限'''
    url =tenant_url+'crm/api/role/'+str(test_input['role_id'])+'/permission/allot'
    body = {"idList":[265]}
    res = requests.post(url,json=body,headers=head)
    return res.text

def crm_api_roles(head):
    '''角色管理-查询'''
    url =tenant_url+'crm/api/roles?pageNo=1&pageSize=20'
    res = requests.get(url,headers=head)
    return res.text

def globalparams_list(head):
    '''全局参数管理--参数列表查询'''
    url = tenant_url+'config/globalParam/list'
    body = {"chineseName":"","configType":"","tenantId":tenant_id}
    res = requests.post(url,json=body,headers=head)
    return res.text


def globalparams_add(head):
    '''全局参数管理-新增'''
    url = tenant_url +'config/globalParam'
    body = {"configType":1,"enumValue":[""],"chineseName":"自"+now_time,"englishName":"a"+now_time,"defaultValue":"1","dataForm":"number","tenantId":tenant_id}
    res = requests.post(url,json=body,headers=head)
    return res.text


def globalparams_del(head,test_input):
    '''全局参数管理-删除'''
    url = tenant_url+'config/globalParam/'+str(test_input['param_id'])
    res = requests.delete(url,headers=head)
    return res.text

