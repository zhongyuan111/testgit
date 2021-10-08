from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
import time
from case.public_config import Get_Config
import os


to_mail = Get_Config()

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


## ==============定义发送附件邮件==========
def send_file(file_new):
    smtpserver = to_mail.get_mail_smtpserver()
    user = to_mail.get_mail_user()
    password = to_mail.get_mail_password()
    sender = to_mail.get_mail_sender()
    #在读取后转换成字符串数组
    raw_value = to_mail.get_mail_receiver()
    receiver = [i.strip() for i in raw_value.split(',')]

    # subject='**接口自动化测试报告'
    # file=open(file_new,'rb').read()# 读文件
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    # 邮件正文是MIMEText
    # body = MIMEText(mail_body, 'html', 'utf-8')
    body =MIMEText(_text=mail_body,_subtype='html',_charset='utf-8')
    html =MIMEText(_text=mail_body,_subtype='html',_charset='utf-8')
    # 邮件对象
    massage = MIMEMultipart()
    massage['Subject'] = Header("！！请查阅——4.0接口自动化测试报告！！", 'utf-8').encode()  # 主题
    massage['From'] = Header(u'接口自动化程序 <%s>' % sender)  # 发件人
    #massage['To'] = Header(u'相关人员 <%s>' % receiver)  # 收件人
    massage['To'] = ';'.join(receiver)
    massage['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    body.add_header("Content-Disposition", "attachment", filename=("gbk", "", "接口自动化测试报告.html"))
    massage.attach(body)
    massage.attach(html)


    smtp=smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,massage.as_string())
    smtp.quit()


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    test_report =os.path.join(os.getcwd(), "report")
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序 win
    # lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn)) #linux
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的报告保存到file_new
    print(file_new)
    return file_new
#
# if __name__ == "__main__":
#     send_file( r'C:\Users\Administrator\PycharmProjects\OpenAPI_new\Report\2017-10-26 20_08_07result.html')