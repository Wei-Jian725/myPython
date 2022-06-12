# -*- coding:utf-8 -*-
_author_ = 'weijian'


import pytest#导入pytest库，进行测试用例数据驱动等操作
from Common.getToken import getToken  #导入token封装类

#将token设置为全局变量
@pytest.fixture(scope='session', autouse=True)
def token():
    token = getToken().token()  # 导入封装好的token
    return token

@pytest.fixture(scope='session', autouse=True)
def manageToken():
    token = getToken().manageToken()  # 导入封装好的token
    return token


@pytest.fixture(scope='session', autouse=True)
def superToken():
    token = getToken().superToken()  # 导入封装好的token
    return token

@pytest.fixture(scope='session', autouse=True)
def zjToken():
    token = getToken().zjToken()  # 导入封装好的token
    return token