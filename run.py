#!/usr/bin/env python
# coding=gbk
import pytest
import os

root_dir = os.path.dirname(os.path.abspath('.'))  # 获取项目根目录的相对路径
file_path = root_dir + '\\auto_4.0\\Report'
print('root_dir:::',root_dir)

if __name__ == "__main__":
    #pytest.main(['-s'])
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    #pytest.main(['--alluredir', file_path])
    pytest.main(['-s', '-q', '--alluredir', file_path, root_dir+'\\auto_4.0\\Testcase\\Tenant\\1Super_agent'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    #os.popen('allure generate --clean ./Report')
    os.popen('allure generate ./Report  -o ./allure-report   --clean')



