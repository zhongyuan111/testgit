import json
import requests
import os
from Common.get_token  import Login_Token
from Config.public_config import Get_Config
from Config.public_config import Random_Number

login_token = Login_Token()  # 实例化
public_config = Get_Config()  #实例化
public_config1 = Random_Number() #实例化
operation_url = public_config.get_address_operation() #获取运营端地址
test_file1 =public_config.get_operation_testfile()
head1= login_token.upload_header('operation') #获取上传文件头
head2 = login_token.json_header('operation') #获取json格式头
operation_user = public_config.get_operation_user() #获取运营端账号
operation_password = public_config.get_operation_password()#获取运营端密码
phone = public_config1.random_phone() #获取手机号
name = public_config1.random_name() #获取名字
domainName = public_config1.random_domainName()  #获取域名
email = public_config1.random_email() #获取邮箱

def upload_file(head,test_file):
    '''上传图片'''
    upload_path = os.path.dirname(os.path.abspath('.')) + '\\auto_4.0\\up_files\\'
    print(upload_path)

    post_url = operation_url+'/api/file/upload'
    open_file = open(upload_path + test_file, 'rb')
    file = {'tag': (None, 'task-core'),
            'files': (test_file, open_file, 'image/png')
            }
    # 执行上传文件接口
    res = requests.post(post_url, files=file, headers=head)
    open_file.close()
    print('执行上传文件结果：',res.text)
    file_info = json.loads(res.text)['data']
    #print('up_load：',file_info)
    list_info = file_info['list']

    #print('list_info:',list_info)
    certPicUrl = list_info[0]['localName']
    print('certPicUrl',certPicUrl)
    return certPicUrl

#upload_file()

def creat_right_customer():
    '''创建租户 '''
    url = operation_url+'/crm/admin/api/customer'
    body = {
            "phone":phone,
            "fullName":name,
            "certPicUrl1":upload_file(head1,test_file1),
            "certPicUrl2":"",
            "shortName":name,
            "name":name,
            "password":"Aa1579",
            "type":1,
            "email":email,
            "list":[
                {
                    "callerIdNumber":"15200000001",
                    "id":198,
                    "shareType":0,
                    "type":3
                }
            ],
            "agentSize":1,
            "industryId":2405,
            "concurrent":1,
            "domainName":domainName,
            "expiryDate":1790697600000,
            "outboundLimit":1,
            "accountType":3,
            "earlyMediaSwitch":0
        }
    #print('body',body)
    res = requests.post(url, json=body, headers=head2)
    #print('&&&&&&',res.text)
    userId = (res.json()['data']['userId'])
    customer = (res.json()['data']['id'])
    #print(userId,customer)
    return userId,customer

def creat_customer(head,test_data):
    '''创建租户 '''
    url = operation_url+'/crm/admin/api/customer'
    body = {
            "phone":test_data['phone'],
            "fullName":test_data['fullName'],
            "certPicUrl1":test_data['certPicUrl1'],
            "certPicUrl2":"",
            "shortName":test_data['shortName'],
            "name":test_data['name'],
            "password":"Aa1579",
            "type":1,
            "email":test_data['email'],
            "list":[
                {
                    "callerIdNumber":"15200000001",
                    "id":198,
                    "shareType":0,
                    "type":3
                }
            ],
            "agentSize":test_data['agentSize'],
            "industryId":2405,
            "concurrent":test_data['concurrent'],
            "domainName":test_data['domainName'],
            "expiryDate":test_data['expiryDate'],
            "outboundLimit":test_data['outboundLimit'],
            "accountType":test_data['accountType'],
            "earlyMediaSwitch":0
        }
    #print('body',body)
    res = requests.post(url, json=body, headers=head)
    #print('&&&&&&',res.text)
    #userId = (res.json()['data']['userId'])
    #customer = (res.json()['data']['id'])
    #print(userId,customer)
    return res.text

def examine_success():
    '''租户审核成功 '''
    param = creat_right_customer()
    userId = str(param[0])
    customer1 = str(param[1])
    url = operation_url+'/crm/admin/api/customer/'+ customer1 +'/audit'
    #url = operation_url + '/crm/admin/api/customer/111123/audit'
    body ={"auditStatus":2,"auditReason":""}
    res = requests.put(url, json=body, headers=head2)
    print(res.text)
    return userId

#examine_success()

def examine_fail():
    '''租户审核失败'''
    #param = creat_customer()  #如果不想执行失败，则不需要调创建租户接口
    customer1 = param[1]
    url = operation_url + '/crm/admin/api/customer/'+customer1+'/audit'
    body ={"auditStatus":3,"auditReason":"自动化测试"}
    res = requests.put(url, json=body, headers=head2)
    #print(res.text)

def mange_authority():
    '''租户权限分配--如果业务需要创建租户，则直接调用该接口执行'''
    userid = examine_success()
    print(userid)
    url = operation_url+'/crm/admin/api/user/'+userid+'/role/tenant/allot'
    body = {"roleId":452}
    res = requests.post(url, json=body, headers=head1)
    print(res.text)












