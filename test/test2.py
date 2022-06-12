# -*- coding:utf-8 -*-
_author_ = 'weijian'

import pytest,allure,subprocess,time,datetime   #导入pytest库，进行测试用例数据驱动等操作
from Common.API_key import ApiKey   #将封装的get、post请求导入。将取接口返回值的封装函数导入
from conf.readini import read_ini   #将读取环境URL的模块导入
from Common.readCase import readCase  #将读取测试用例封装的函数导入
from Common.read_log import Mylog  #导入日志封装类
from conf.Global3 import * #导入全局变量类


ak = ApiKey()  # 导入封装好的接口请求方式
Url = read_ini('../conf/config.ini', 'test_server', 'url')  # 导入接口请求端口号为9000的URL







# url = ' https://rmp-newtest.fs-salon.cn/prod-api/ic/study/manageSearch'
# print(url)
# data={
#     'advanced': False,
# 'aiStatus': "",
# 'checkEndDateTime': "",
# 'checkStartDateTime': "",
# 'condition': "",
# 'deptId': "",
# 'endDateTime': "",
# 'hospId': "",
# 'modalityModel': "",
# 'modalityType': "",
# 'orderEndDateTime': "",
# 'orderStartDateTime': "",
# 'pageIndex': 1,
# 'pageSize': 15,
# 'printerName': "",
# 'reporterName': "",
# 'reviewerName': "",
# 'selfHospId': "936570992694800384",
# 'sex': "",
# 'startDateTime': "",
# 'status': [],
# 'studyPartName': "",
# 'type': "",
#         }
#
#
# header={'Content-type':'application/json','Authorization':getToken().token()}#请求头
# reps=ak.do_post(url,json = data ,headers=header)#发起请求
# pprint.pprint(reps.json())




# url = Url + name['path'] + f'?partId={partId()}'  # 请求地址
#data = name['data']
#if data['name'] == '正确值':  # 判断yaml文件中是否填写了'正确值'，如果填写了就给他赋值正确的值
#Post_CaseT(token, name, data, url)


@allure.feature('会诊管理模块')
class Test_diagnosisRead:
    modalityworkLoadDT = readCase('../data/普通用户系统/检查统计模块/设备工作量统计.yaml')

    @allure.description('检查统计模块-设备工作量统计接口')
    @allure.title('设备工作量统计接口')
    @allure.testcase(Url + '/ic/studyStatistics/modalityWorkLoad')
    @pytest.mark.parametrize('name', modalityworkLoadDT)  # 将测试结果参数化作为用例执行
    def test_modalityWorkLoad(self, token, name):
        url = Url + name['path']  # 请求地址
        data = name['data']
        data['hospId'] = selfHospId()
        # print(data)
        header = name['header']  # 接口请求头
        header['Authorization'] = token  # 接口请求头中传入token
        res = ak.do_post(url=url, json=data, headers=header)  # post请求返回结果
        Mylog().debug(f'设备工作量统计接口请求参数{data}')
        Mylog().debug(f'设备工作量统计接口返回值{res.json()}')
        exceptSuccess = name['expect']['success']
        success = ak.get_text(res.text, 'success')  # 接口返回结果中的字段
        exceptMsg = name['expect']['msg']  # 在测试用例中提取预期返回结果
        msg = ak.get_text(res.text, 'msg')  # 接口实际返回结果
        exceptState = name['expect']['state']  # 在测试用例中提取预期返回结果
        state = ak.get_text(res.text, 'state')
        assert exceptMsg == msg and success == exceptSuccess and state == exceptState  # 断言接口返回字段如果为预期结果，则说明接口请求成功




if __name__ == '__main__':
    pytest.main(['test2.py', '-s'])

