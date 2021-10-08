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
test_datas=[({'camp_uuid':pre_res[1],'call_id':pre_res[3]},None,'通话详情录音')]
@allure.epic("活动管理")    #根目录
@allure.feature("人机活动")   #功能模块
@allure.story("通话详情录音")   #功能模块下的分支
@allure.link("https://redmine.lingban.cn/")  #链接
@allure.title("{title}")
@pytest.mark.skipif(pre_res=='false',reason='webhook_wrong')
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
def test_record_voice(test_input,expected,title):
   '''通话详情中查询录音接口'''

   res=Common.public_tenant_api.query_record_voice(header1,test_input)
   assert res!=expected,'未返回录音'

