import unittest
import random
import string
import requests
import re
from Config.public_config import Get_Config

get_config = Get_Config() #实例化

class Login_Token(unittest.TestCase):

    def get_token(sefl,sys_name):
        '''获取token，入参operation：管理端  tenant：租户端  agent：坐席端'''
        if sys_name=='operation':
            url = get_config.get_address_operation() + 'uaa/oauth/token'
            authorization = get_config.get_operation_authorization()
            header = {'content-type': 'application/x-www-form-urlencoded',
                      'Authorization': authorization}
            data = 'grant_type=password&password=' + get_config.get_operation_password() + '&username=' + get_config.get_operation_user() + '&auth_type=username'
            res = requests.post(url, data, headers=header)
            print(res.status_code)
            token = res.json()['access_token']

            return token
        if sys_name=='tenant':
            url = get_config.get_address_tenant() + 'uaa/oauth/token'
            authorization = get_config.get_tenant_authorization()
            header = {'content-type': 'application/x-www-form-urlencoded',
                      'Authorization':authorization}
            data = 'grant_type=password&password=' + get_config.get_tenant_password() + '&username=' + get_config.get_tenant_user() + '&auth_type=username'
            res = requests.post(url, data, headers=header)
            # print(url)
            # print(data)
            # print(header)
            # print(res.status_code)
            # print(res.text)
            token = res.json()['access_token']
            return token
        if sys_name=='agent':
            url = get_config.get_address_agent() + 'uaa/oauth/token'
            authorization = get_config.get_agent_authorization()
            header = {'content-type': 'application/x-www-form-urlencoded',
                      'Authorization':authorization}
            data = 'grant_type=password&password=' + get_config.get_agent_password() + '&username='+get_config.get_agent_user()+'&auth_type=username'
            res = requests.post(url, data, headers=header)
            # print(url)
            # print(data)
            # print(header)
            # print(res.status_code)
            # print(res.text)
            # print(res.status_code)
            token = res.json()['access_token']
            return token



    def json_header(self,sys_name):
        '''json格式的头'''
        token =self.get_token(sys_name)
        A = '%s %s' % ('Bearer', token)

        header ={'content-type': 'application/json',
                  'Authorization': A
                  }

        return header

    def str_header(self,sys_name):
        '''字符串格式的头'''
        token = self.get_token(sys_name)
        A = '%s %s' % ('Bearer', token)

        header = { 'content-type': 'application/x-www-form-urlencoded',
                  'Authorization': A
                  }

        return header
    def upload_header(self,sys_name):
        '''上传文件的头'''
        token = self.get_token(sys_name)
        A = '%s %s' % ('Bearer', token)

        header = {#'content-type': 'multipart/form-data',
                  'Authorization': A
                  }

        return header


    def get_ws_url(self):
        '''生成登录时websocket连接url'''
        token = self.get_token('tenant')
        '''随机生成8位字符串作为socketid'''
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        '''生成随机三位数字'''
        num = ''.join(random.sample(string.digits, 3))
        str1 = get_config.get_address_ws()+"socket/api/socket/%s" % num
        str2 = "/%s" % ran_str
        str3 = "/websocket?access_token=%s" % token
        socket_url = str1 + str2 + str3
        '''返回url'''
        return socket_url

    def get_socketid(self,socket_url):
        '''从ws连接截取socketid'''
        socketID = re.findall('api/socket/(.+?)websocket?', socket_url)[0]
        socketid = re.findall('/(.+?)/', socketID)[0]
        return socketid






suite = unittest.TestSuite()

suite.addTest(Login_Token("get_token"))
suite.addTest(Login_Token("json_header"))
suite.addTest(Login_Token("str_header"))
suite.addTest(Login_Token("get_ws_url"))
suite.addTest(Login_Token("get_socketid"))



