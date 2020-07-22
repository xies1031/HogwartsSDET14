import sys

import pytest
import yaml

sys.path.append('..')
from pythoncode.calc import Calculator

with open('data/test/data.yaml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)

    adddatas = datas['add'].values()
    addids = datas['add'].keys()

    minusdatas = datas['minus'].values()
    minusids = datas['minus'].keys()

    multdatas = datas['mult'].values()
    multids = datas['mult'].keys()

    divdatas = datas['div'].values()
    divids = datas['div'].keys()


class TestCalc:
    cal = Calculator()

    @pytest.mark.parametrize('a,b,result', divdatas, ids=divids)
    @pytest.mark.run(order=3)
    @pytest.mark.dependency(depends=['test_mult'])
    def test_div(self, a, b, result):
        if b == 0:
            print("除数不能为0")
            return 0
        else:
            assert result == self.cal.div(a, b)

    @pytest.mark.parametrize('a,b,result', adddatas, ids=addids)
    @pytest.mark.run(order=0)
    @pytest.mark.dependency(name='test_add')
    def test_add(self, a, b, result):
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,result', minusdatas, ids=minusids)
    @pytest.mark.run(order=1)
    @pytest.mark.dependency(depends=['test_add'])
    def test_minus(self, a, b, result):
        assert result == self.cal.minus(a, b)

    @pytest.mark.parametrize('a,b,result', multdatas, ids=multids)
    @pytest.mark.run(order=2)
    @pytest.mark.dependency(name='test_mult')
    def test_mult(self, a, b, result):
        assert result == self.cal.mult(a, b)
