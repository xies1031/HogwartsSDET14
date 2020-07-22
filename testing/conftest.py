import pytest
import yaml


@pytest.fixture(scope='function', autouse=True)
def calc():
    print("\n开始计算")
    yield
    print("\n计算结束")


# 自定义参数
def pytest_addoption(parser):
    mygroup = parser.getgroup('Captain')
    mygroup.addoption('--env', default='test', dest='env', help='set your run env')


# 根据自定义参数获取当前环境数据
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        datapath = 'data/test/test.yaml'

    if myenv == 'dev':
        datapath = 'datas/dev/data.yaml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
