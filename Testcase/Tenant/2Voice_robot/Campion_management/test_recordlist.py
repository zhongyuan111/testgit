#coding=gbk
import json
import allure
import pytest
from Common.common_param import  Common_param
import Common.public_tenant_api
from Common.get_token import Login_Token

token=Login_Token()
pre_camp=Common_param()
header1 = token.json_header('tenant')  # 实例json根式的头
pre_res=pre_camp.pre_campinon()
#print(pre_res)
pre_res1=pre_camp.pre_campinon1()
# 测试数据
test_datas =  [({"id":pre_res[2]},["\u6210\u529F!",10],"人机活动通话记录查询，正向用例")]
@allure.epic("活动管理")    #根目录
@allure.feature("人机活动")   #功能模块
@allure.story("人机通话记录查询")   #功能模块下的分支
@allure.link("https://redmine.lingban.cn/")  #链接
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
@pytest.mark.skipif(pre_res=='false',reason='pre_wrong')
def test_robotrecordlist(test_input,expected,title):
    res=Common.public_tenant_api.camp_query_record(header1,test_input)
    msg=json.loads(res)['msg']
    total=json.loads(res)['data']['total']
    checklist=[]
    checklist.append(msg)
    checklist.append(total)
    assert checklist==expected,'接口返回空'



#测试数据
test_datas1 =  [({"id":pre_res1[2]},["\u6210\u529F!",10],"人机协同通话记录查询，正向用例")]
@allure.epic("活动管理")    #根目录
@allure.feature("人机活动")   #功能模块
@allure.story("人机协同通话记录查询")   #功能模块下的分支
@allure.link("https://redmine.lingban.cn/")  #链接
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas1
                         )
@pytest.mark.skipif(pre_res1=='false',reason='pre_wrong')
def test_mixcrecordlist(test_input,expected,title):
    res=Common.public_tenant_api.camp_query_record(header1,test_input)
    msg=json.loads(res)['msg']
    total=json.loads(res)['data']['total']
    checklist=[]
    checklist.append(msg)
    checklist.append(total)
    assert checklist==expected,'接口返回空'
