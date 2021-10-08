#!/usr/bin/env python
# coding=gbk
import os
import pytest

root_dir = os.path.dirname(os.path.abspath('.'))  # ��ȡ��Ŀ��Ŀ¼�����·��
file_path = root_dir + '\\UiTest\\Report'
print('root_dir:::',root_dir)

if __name__ == "__main__":
    #pytest.main(['-s'])
    # ִ��pytest��Ԫ���ԣ����� Allure ������Ҫ�����ݴ��� /temp Ŀ¼
    #pytest.main(['--alluredir', file_path])
    pytest.main(['-s', '-v', '--alluredir', file_path, root_dir + '\\UiTest\\Testcase\\test_callmange'])
    #�ֲ�ʽִ��
    #pytest.main(['-s', '-v','-n','auto','--dist','loadfile','--alluredir', file_path, root_dir+'\\UiTest\\Testcase\\test_callrobot'])
    # ִ������ allure generate ./temp -o ./report --clean �����ɲ��Ա���
    #os.system("allure generate report -o report/html")
    os.popen('allure generate D:\\demo\\UiTest\\Report  -o D:\\demo\\UiTest\\allure-report   --clean')
    #os.popen('allure generate ./Report  -o ./allure-report   --clean')
