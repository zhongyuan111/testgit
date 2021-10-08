import configparser
import os
import random
#配置文件目录
root_dir = os.path.dirname(os.path.abspath('.'))  # 获取项目根目录的相对路径
file_path = os.path.dirname(os.path.abspath('.')) + '\\auto_4.0\Config\profile_conf.txt'
upload_path = os.path.dirname(os.path.abspath('.')) + '\\up_files\\'
print('file_path:',file_path)
cf = configparser.ConfigParser()
cf.read(file_path,encoding='utf-8')


class Get_Config():
    def get_mail_smtpserver(self):
        smtpserver = cf.get("mail","smtpserver")
        return smtpserver

    def get_mail_user(self):
        user = cf.get("mail","user")
        return user

    def get_mail_password(self):
        password = cf.get("mail","password")
        return password

    def get_mail_sender(self):
        sender = cf.get("mail","sender")
        return sender
    def get_mail_receiver(self):
        receiver = cf.get("mail","receiver")
        return receiver

    def get_operation_user(self):
        user = cf.get("operation_login","user")
        return user

    def get_operation_password(self):
        password = cf.get("operation_login","password")
        return password

    def get_operation_authorization(self):
        authorization = cf.get("operation_login","authorization")
        return authorization

    def get_operation_testfile(self):
        test_file = cf.get("operation_login","test_file")
        return test_file

    def get_tenant_id(self):
        tenant_id = cf.get("tenant_login","tenant_id")
        return tenant_id

    def get_tenant_user(self):
        user = cf.get("tenant_login","user")
        return user

    def get_tenant_password(self):
        password = cf.get("tenant_login","password")
        return password

    def get_tenant_authorization(self):
        authorization = cf.get("tenant_login","authorization")
        return authorization

    def get_agent_user(self):
        user = cf.get("agent_login","user")
        return user

    def get_agent_domain(self):
        domain = cf.get("agent_login","domain")
        return domain

    def get_agent_password(self):
        password =cf.get("agent_login","password")
        return password

    def get_agent_authorization(self):
        authorization = cf.get("agent_login","authorization")
        return authorization

    def get_address_operation(self):
        operation_url =cf.get("system_address","operation_url")
        return operation_url

    def get_address_tenant(self):
        tenant_url =cf.get("system_address","tenant_url")
        return tenant_url

    def get_address_ws(self):
        ws_url =cf.get("system_address","ws_url")
        return ws_url
    def get_address_agent(self):
        agent_url =cf.get("system_address","agent_url")
        return agent_url

    def get_robot_callno(self):
        call_no =cf.get("robot_attr","call_no")
        return call_no
    def get_robot_calledno(self):
        called_no =cf.get("robot_attr","called_no")
        return called_no
    def get_robot_instid(self):
        inst_id =cf.get("robot_attr","inst_id")
        return inst_id

    def get_robot_flowid(self):
        flow_id =cf.get("robot_attr","flow_id")
        return flow_id

    def get_robot_testfile(self):
        test_file =cf.get("robot_attr","test_file")
        return test_file


    def get_mixrobot_callno(self):
        call_no =cf.get("mixrobot_attr","call_no")
        return call_no
    def get_mixrobot_calledno(self):
        called_no =cf.get("mixrobot_attr","called_no")
        return called_no
    def get_mixrobot_instid(self):
        inst_id =cf.get("mixrobot_attr","inst_id")
        return inst_id

    def get_mixrobot_flowid(self):
        flow_id =cf.get("mixrobot_attr","flow_id")
        return flow_id

    def get_mixrobot_testfile(self):
        test_file =cf.get("mixrobot_attr","test_file")
        return test_file

    def get_mixrobot_ccid(self):
        ccid = cf.get("mixrobot_attr","cc_id")
        return ccid

    def get_mixrobot_groupid(self):
        group_id = cf.get("mixrobot_attr","group_id")
        return group_id

    def get_mixrobot_groupdn(self):
        group_dn = cf.get("mixrobot_attr", "group_dn")
        return group_dn
    def get_mixrobot_groupname(self):
        group_dn = cf.get("mixrobot_attr", "group_name")
        return group_dn

    def get_mysql_conn(self):
        conn = cf.get("db_conn", "mysql_config")
        return conn
    def get_pg_conn(self):
        conn = cf.get("db_conn", "pg_config")
        return conn


class Random_Number():
    def random_phone(self):
        '''随机生成手机号'''
        str_start = random.choice(['188', '189', '190'])
        str_end = ''.join(random.sample('0123456789', 8))
        str_phone = str_start + str_end
        #print(str_phone)
        return str_phone

    def random_name(self):
        '''随机生成姓名'''
        first_name = random.choice(['自动化张', '自动化王', '自动化赵', '自动化刘', '自动化李'])
        second_name = chr(random.randint(0x4e00, 0x9fbf))
        name = first_name + second_name
        #print(name)
        return name
    def random_domainName(self):
        '''随机生成域名'''
        first = chr(random.randint(97,122))
        second= chr(random.randint(97,122))
        domain = random.choice([first, second])
        domainName = first +second + domain +'.com'
        #print('*****ceshi ***',domainName)
        return  domainName

    def random_email(self):
        '''随机生成邮箱'''
        email = self.random_phone() + '@qq.com'
        #print(email)
        return email








