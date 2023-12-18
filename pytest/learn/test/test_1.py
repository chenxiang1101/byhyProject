import pytest


# 当这里的scope分别为function、class、module等时，具体表现会不一样
@pytest.fixture(scope='function',autouse=True)
def createUser():
    print("\n*****开始创建*****")
    user = {
        'username' : 'zhangsan',
        'id' : '0001'
    }

    yield user

    print("\n*****清除*****")

class Test_A:
    def test_000A1(self,createUser):
        print(f"case 000A1:{createUser}")

    def test_000A2(self,createUser):
        print(f"\ncase 000A2:{createUser}")


class Test_B:
    def test_0003(self,createUser):
        print(f"case 000B1:{createUser}")
