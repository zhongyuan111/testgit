
import requests

from Common.get_token  import Login_Token
from Common.public_config import Get_Config
import Common.get_date


public_param = Login_Token()  # 实例化
public_config = Get_Config()  #实例化
ws_url = public_param.get_ws_url()  # 生成websocket连接
agent_url = public_config.get_address_agent()
tenant_id = public_config.get_tenant_id()
call_no = public_config.get_robot_callno()
called_no = public_config.get_robot_calledno()
inst_id = public_config.get_robot_instid()
flow_id = public_config.get_robot_flowid()
start_time = Common.get_date.get_starttime()
end_time = Common.get_date.get_endtime()
cc_id = public_config.get_mixrobot_ccid()




def get_agentinfo(head,agentnum):
    '''获取坐席信息'''
    url = agent_url+'config/agents/detail/'+agentnum
    res = requests.get(url,headers=head)
    return res.text


def query_business_record(head,template_id,dailing_num,agent_num):
    '''业务记录查询'''
    url = agent_url+'outbound/business/record/list'
    body ={
           "templateId":template_id,
           "flowState":1,
           "phoneNumber":dailing_num,
           "startCreateTime":start_time,
           "endCreateTime":end_time,
           "pageNo":1,
           "pageSize":20,
           "agentId":agent_num
           }
    res = requests.post(url,json=body,headers=head)
    return res.text


def query_record(head,dailing_num,agent_num):
    '''通话记录查询'''
    url = agent_url+'contact/campaign/record/list'
    body ={
           "time":[
               start_time,
               end_time
           ],
           "phoneNumber":dailing_num,
           "campaignType":"-1",
           "outboundResult":"EndOfTheCall",
           "campaignId":0,
           "startCallTime":start_time,
           "endCallTime":end_time,
           "pageNo":1,
           "pageSize":20,
           "agentId":agent_num,
           "searchType":1,
           "tenantId":tenant_id
           }

    res =requests.post(url,json=body,headers=head)
    return res.text







