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
test_datas =  [({"action":2,"socketId":socketid},["\u6210\u529F!",4],"暂停人机活动，正向用例")]
@allure.epic("活动管理")    #根目录
@allure.feature("人机活动")   #功能模块
@allure.story("启动人机活动")   #功能模块下的分支
@allure.link("https://redmine.lingban.cn/")  #链接
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
# @pytest.mark.skip()
def test_03(test_input,expected,title):
    '''启动人机活动'''
    camp_name= '自动化人机活动' + str(int(time.time()))
    input_json=[{"name":camp_name,"speaker":"YAY","instId":instid,"flowId":flowid,"callingNo":callno,"callingTimeout":30,
                 "file":real_file,"socketId":socketid,"fileName":test_file},{"action":1,"socketId":socketid}]
    res = Common.public_tenant_api.robot_camp_save(header1,input_json[0])
    print('活动名称：',camp_name)
    print('创建活动接口返回::',res)
    print('campaignuuid:', json.loads(res)['data']['campaignUuid'])
    camp_uuid = json.loads(res)['data']['campaignUuid']
    test_input["camp_uuid"] = camp_uuid
    time.sleep(10)
    Common.public_tenant_api.camp_operation(header1,input_json[1],camp_uuid)
    time.sleep(20)
    operation_res=Common.public_tenant_api.camp_operation(header1,test_input,camp_uuid)
    print('暂停活动接口返回：',operation_res)
    msg=json.loads(operation_res)['msg']
    time.sleep(30)
    sql = 'select state from campaign where  campaign_uuid=\'' + camp_uuid + '\';'
    print('核查语句sql:::', sql)
    result = db_conn.select("outbound", sql)
    if result is not None:
        for rec in result:
             camp_state=rec[0]
    else:
             camp_state=888

    list_res = []
    list_res.append(msg)
    list_res.append(camp_state)  #校验活动状态'状态:0-规划中;2-已启用;3-停止中;4-已停止;5-已完成;7-已取消

    print('活动状态state:', camp_state)

    assert   list_res==expected ,'请核查接口'