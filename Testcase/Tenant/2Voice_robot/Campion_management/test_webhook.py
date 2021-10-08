#coding=gbk
import json
import allure
import pytest
from Common.common_param import  Common_param
import Common.public_tenant_api
from Common.get_token import Login_Token
import math
token=Login_Token()
pre_camp=Common_param()
header1 = token.json_header('tenant')  # 实例json根式的头
pre_res=pre_camp.pre_campinon()

# 测试数据
test_datas=[({'camp_uuid':pre_res[1]},4,'webhook查询')]
@allure.epic("活动管理")    #根目录
@allure.feature("人机活动")   #功能模块
@allure.story("webhook查询")   #功能模块下的分支
@allure.link("https://redmine.lingban.cn/")  #链接
@allure.title("{title}")
@pytest.mark.skipif(pre_res=='false',reason='webhook_wrong')
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
def test_webhook_log(test_input,expected,title):
    exepct_list=['EventCampaignCreated','EventCampaignStarted','EventCallResult','EventCampaignCompleted']
    test_input['pageNo']=1
    res=Common.public_tenant_api.webhook_send(header1,test_input)
    total=json.loads(res)['data']['total']
    pages=math.ceil(total/100)
    print('pageno::',pages)
    test_input['pageNo']=pages
    res1 = Common.public_tenant_api.webhook_send(header1, test_input)
    loglist=json.loads(res1)['data']['list']
    statelist=[]
    i=0
    j = 0
    for i in range(len(loglist) - 1):

        if loglist[i]['taskId'] == test_input['camp_uuid']:
            statelist.append(loglist[i]['event'])
        i += 1
    for j in range(len(exepct_list)):
        if exepct_list[j] in statelist:
            j += 1
        else:
            break

    assert j==expected,'webhook 回推事件不全'

