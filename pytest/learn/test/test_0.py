# fixture参数(夹具）
'''
这个例子演示了如何使用 pytest 进行参数化测试，通过定义一个夹具来提供测试数据。
在测试函数中，可以通过夹具参数访问测试数据，
从而执行多次相同的测试用例，每次使用不同的输入数据。
'''
import pytest

#定义一个fixture参数,作用域为每个函数
@pytest.fixture()
def createUser(request):
    user={
        'username': request.param[0],
        'password': request.param[1]
    }
    yield user

class Test_Users:
    @pytest.mark.parametrize("createUser",[
        ('zhangsan','0001'),
        ('lisi','0002'),
        ('wanger','0003'),
        ('mazi','0004')
    ],indirect=True)    #indirect=True 表示要将参数传递给夹具而不是测试函数本身
    def test_users(self,createUser):
        print(f"\nusername={createUser['username']},id={createUser['password']}")