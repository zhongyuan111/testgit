#!/usr/bin/env python
# coding=gbk
import os
import pytest

root_dir = os.path.dirname(os.path.abspath('.'))  # 获取项目根目录的相对路径
file_path = root_dir + '\\UiTest\\Report'
print('root_dir:::',root_dir)

if __name__ == "__main__":
    #pytest.main(['-s'])
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    #pytest.main(['--alluredir', file_path])
    pytest.main(['-s', '-v', '--alluredir', file_path, root_dir + '\\UiTest\\Testcase\\test_callmange'])
    #分布式执行
    #pytest.main(['-s', '-v','-n','auto','--dist','loadfile','--alluredir', file_path, root_dir+'\\UiTest\\Testcase\\test_callrobot'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    #os.system("allure generate report -o report/html")
    os.popen('allure generate D:\\demo\\UiTest\\Report  -o D:\\demo\\UiTest\\allure-report   --clean')
    #os.popen('allure generate ./Report  -o ./allure-report   --clean')
