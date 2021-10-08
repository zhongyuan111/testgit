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
camp_name=pre_camp.pre_campinon()
camp_name1=pre_camp.pre_campinon1()
# 测试数据
test_datas =  [({"name":camp_name[0]},["\u6210\u529F!",1],"人机活动查询，正向用例")]
@allure.epic("活动管理")    #根目录
@allure.feature("人机活动")   #功能模块
@allure.story("人机活动查询")   #功能模块下的分支
@allure.link("https://redmine.lingban.cn/")  #链接
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
@pytest.mark.skipif(camp_name='false')
def test_robotcamplist(test_input,expected,title):
    res=Common.public_tenant_api.camp_manage_list(header1,test_input)
    msg=json.loads(res)['msg']
    total=json.loads(res)['data']['total']
    checklist=[]
    checklist.append(msg)
    checklist.append(total)
    assert checklist==expected,'接口返回空'



# 测试数据
test_datas1 =  [({"name":camp_name1[0]},["\u6210\u529F!",1],"人机协同活动查询，正向用例")]
@allure.epic("活动管理")    #根目录
@allure.feature("人机活动")   #功能模块
@allure.story("人机协同活动查询")   #功能模块下的分支
@allure.link("https://redmine.lingban.cn/")  #链接
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas1
                         )
@pytest.mark.skipif(camp_name1='false')
def test_mixcamplist(test_input,expected,title):
    res=Common.public_tenant_api.camp_manage_list(header1,test_input)
    msg=json.loads(res)['msg']
    total=json.loads(res)['data']['total']
    checklist=[]
    checklist.append(msg)
    checklist.append(total)
    assert checklist==expected,'接口返回空'
