from Common.get_token import Login_Token
import Common.public_operation_api
from Config.public_config import Get_Config
from Config.public_config import Random_Number
import json
import  pytest
import allure

login_token = Login_Token() #实例化
public_config = Get_Config()  #实例化
public_config1 = Random_Number() #实例化
head =login_token.json_header('operation') #获取json格式头
head2 = login_token.upload_header('operation') #获取json上传文件格式头
test_file = public_config.get_operation_testfile() #获取图片文件
certPicUrl = Common.public_operation_api.upload_file(head2,test_file) #获取图片文件名字
#print('certPicUrl***',certPicUrl)
#test_file =public_config.get_operation_testfile()
#head=public_param.upload_header('operation') #获取上传文件头
#head1 = public_param.json_header('operation') #获取json格式头
phone = public_config1.random_phone() #获取手机号
name = public_config1.random_name() #获取名字
domainName = public_config1.random_domainName()  #获取域名
email = public_config1.random_email() #获取邮箱
#print("*****All****",phone,name,domainName,email)

# 测试数据
# accountType 0：线下付费 3：预支付-并发 4：预支付
test_datas = [
        ({"phone": public_config1.random_phone(), "fullName": public_config1.random_name(), "certPicUrl1": certPicUrl,
          "certPicUrl2": "", "shortName": public_config1.random_name(), "name": public_config1.random_name(),
          "password": "Aa1579", "type": 1, "email": public_config1.random_email(),
          "list": [{"callerIdNumber": "15200000001", "id": 198, "shareType": 0, "type": 3}],
          "agentSize": 5, "industryId": 2405, "concurrent": 8, "domainName": public_config1.random_domainName(),
          "expiryDate": 1790697600000, "outboundLimit": 20, "accountType": 0, "earlyMediaSwitch": 0}, ["成功!"],"输入正确信息，添加线下内部测试类型租户"),
         ({"phone": public_config1.random_phone(), "fullName": public_config1.random_name(), "certPicUrl1": certPicUrl,
          "certPicUrl2": "", "shortName": public_config1.random_name(), "name": public_config1.random_name(),
          "password": "Aa1579", "type": 1, "email": public_config1.random_email(),
          "list": [{"callerIdNumber": "15200000001", "id": 198, "shareType": 0, "type": 3}],
          "agentSize": 0, "industryId": 2405, "concurrent": 0, "domainName": public_config1.random_domainName(),
          "expiryDate": 1790697600000, "outboundLimit": 0, "accountType": 3, "earlyMediaSwitch": 0}, ["成功!"],"输入正确信息，添加预付款-并发类型租户"),
        ({"phone": public_config1.random_phone(), "fullName": public_config1.random_name(), "certPicUrl1": certPicUrl,
          "certPicUrl2": "", "shortName": public_config1.random_name(), "name": public_config1.random_name(),
          "password": "Aa1579", "type": 1, "email": public_config1.random_email(),
          "list": [{"callerIdNumber": "15200000001", "id": 198, "shareType": 0, "type": 3}],
          "agentSize": 0, "industryId": 2405, "concurrent": 100, "domainName": public_config1.random_domainName(),
          "expiryDate": 1790697600000, "outboundLimit": 0, "accountType": 4, "earlyMediaSwitch": 0}, ["成功!"],"输入正确信息，添加预付款-通话数类型租户"),
]
#print('****@@@@@@**',test_datas)
@allure.epic("运营端")
@allure.feature("租户管理")   #功能模块
@allure.story("创建租户")   #功能模块下的分支
@allure.link("https://redmine.lingban.cn/")  #链接
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
def test_01creat_customer(test_input,expected,title):
    '''添加租户'''

    save_res = Common.public_operation_api.creat_customer(head,test_input)
    #print(save_res)
    msg = json.loads(save_res)['msg']
    #print("testinput:::",test_input)
    #print("expected:::",expected)
    #print("'title':::",title)
    assert msg==expected[0]

