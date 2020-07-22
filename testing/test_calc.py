import sys
import pytest
import yaml

print(sys.path.append(".."))
from pythoncode.calc import Calculator


class TestCalc():
    cal = Calculator()

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('data/data1.yaml')),
                             ids=['int', 'zero', "negative", 'float', 'str'])
    def test_add(self, a, b, result):
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('data/data2.yaml')),
                             ids=['int', 'zero', "negative", 'float', 'str'])
    def test_minus(self, a, b, result):
        assert result == self.cal.minus(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('data/data3.yaml')),
                             ids=['int', 'zero', "negative", 'float', 'str'])
    def test_mult(self, a, b, result):
        assert result == self.cal.mult(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('data/data4.yaml')),
                             ids=['int', 'zero', "negative", 'float', 'str', 'wrongzero'])
    def test_div(self, a, b, result):
        assert result == self.cal.div(a, b)
