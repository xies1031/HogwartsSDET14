import pytest


@pytest.fixture(scope='function', autouse=True)
def calc():
    print("\n开始计算")
    yield
    print("\n计算结束")
