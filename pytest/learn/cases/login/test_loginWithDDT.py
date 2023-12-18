#.\cases\登录\test_loginWithDDT.py

import pytest
from pytest.learn.lib.webui import loginAndCheck
class Test_loginWithDDT:
    @pytest.mark.parametrize('usename,password,returnText',[
        ('byhy','88888888','success'),
        (None,'88888888','请输入用户名'),
        ('byhy',None,'请输入密码'),
        ('by','8888','登录失败 : 用户名或者密码错误'),
    ])
    def test_UI(self,usename,password,returnText):
        assert loginAndCheck(usename,password) == returnText