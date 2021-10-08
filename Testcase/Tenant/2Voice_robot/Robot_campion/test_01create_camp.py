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
test_file = config.get_robot_testfile()   #外呼文件，源文件名称
real_file = Common.public_tenant_api.upload_file(header2, test_file)#upload接口返回文件名字
#camp_name = '自动化人机活动' + str(int(time.time()))
instid=config.get_robot_instid() #robotid
flowid=config.get_robot_flowid() #版本id
callno=config.get_robot_callno()  #码号
ws_url = token.get_ws_url()  # 生成websocket连接
socketid = token.get_socketid(ws_url)

# 测试数据test
#钟源增加备注
test_datas =  [({"name": '自动化人机活动' + str(int(time.time())),"speaker":"YAY","instId":instid,"flowId":flowid,"callingNo":callno,"callingTimeout":30,
                 "file":real_file,"socketId":socketid,"fileName":test_file},["\u6210\u529F!",0,1,10],"创建人机活动，正向用例1"),
               ({"name": '自动化人机活动' + str(int(time.time())+1),"speaker": "wlu","instId": instid,"flowId": flowid,"callingNo": callno,"callingTimeout": 30,
                 "file": real_file, "socketId": socketid, "fileName": test_file}, ["\u6210\u529F!", 0, 1,10],"创建人机活动，正向用例2"),
               ({"name": '自动化人机活动' + str(int(time.time())+1),"speaker": "wlu","instId": instid,"flowId": flowid,"callingNo": callno,"callingTimeout": 30,
                 "file": real_file, "socketId": socketid, "fileName": test_file}, ["已有重名的外呼活动", 999, 999,999], "活动名称重复")
               ]
@allure.epic("活动管理")    #根目录
@allure.feature("人机活动")   #功能模块
@allure.story("创建人机活动")   #功能模块下的分支
@allure.link("https://redmine.lingban.cn/")  #链接
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
# @pytest.mark.skip()
def test_01(test_input,expected,title):
    '''创建人机活动'''

    res = Common.public_tenant_api.robot_camp_save(header1,test_input)
    print('test_input',test_input)
    print('res::::::::::',res)

    msg = json.loads(res)['msg']
    time.sleep(10)

    if msg == "\u6210\u529F!":       #接口返回msg成功则查活动状态和类型是否正确
        print('campaignuuid:', json.loads(res)['data']['campaignUuid'])
        camp_uuid = json.loads(res)['data']['campaignUuid']
        sql='select state,type,total_numbers from campaign where  campaign_uuid=\''+camp_uuid+'\';'
        print('核查语句sql:::',sql)
        result = db_conn.select("outbound",sql)
        if result is not None:
            for rec in result:
                camp_state=rec[0]
                type=rec[1]
                total=rec[2]
    else:                          #接口返回失败，核查活动数据是否入表，如果入表则程序有问题
        sql = 'select count(*) from campaign where  name=\'' + test_input['name'] + '\';'
        print('核查语句sql:::', sql)
        result = db_conn.select("outbound", sql)
        for rec in result:
             cont=rec[0]
        if cont==1:
            camp_state = 999
            type = 999
            total=999
        else:
            camp_state=888
            type=888
            total=888
    list_res = []
    list_res.append(msg)    #接口返回
    list_res.append(camp_state)   #校验活动状态'状态:0-规划中;2-已启用;3-停止中;4-已停止;5-已完成;7-已取消
    list_res.append(type)      #校验活动类型   活动类型 1-机器人外呼 2-人机协同外呼3-人工预览外呼
    list_res.append(total)     #校验上传条数与入库总数字段，默认10条
    print('活动状态state和活动类型、上传总数:', camp_state,type,total)

    assert   list_res==expected ,'请核查接口'
#jlwang 