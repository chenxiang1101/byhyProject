#.\cases\登录\test_login.py

from pytest.learn.lib.webui import loginAndCheck

class Test_login:
    def test_UI_0000(self):
        print("用户名正确，密码正确")
        returnText = loginAndCheck('byhy', '88888888')
        assert returnText == 'success'

    def test_UI_0001(self):
        print("用户名为空，密码正确")
        returnText = loginAndCheck(None,'88888888')
        assert returnText == '请输入用户名'

    def test_UI_0002(self):
        print("用户名正确，密码为空")
        returnText = loginAndCheck('byhy',None)
        assert returnText == '请输入密码'

    def test_UI_0003(self):
        print("用户名错误")
        returnText = loginAndCheck('wrongName','88888888')
        assert returnText == '登录失败 : 用户名或者密码错误'