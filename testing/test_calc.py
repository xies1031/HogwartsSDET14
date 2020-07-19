import sys
import pytest
import yaml

print(sys.path.append(".."))
from pythoncode.calc import Calculator

class TestCalc():
    cal = Calculator()

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('data1.yaml')), ids=['int','zero',"negative",'float','str'])
    def test_add(self,a,b,result):
        try:
            result = a + b
        except Exception as msg:
            print(f'\n异常用例："{msg}"')
        else:
            assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('data2.yaml')), ids=['int', 'zero', "negative", 'float', 'str'])
    def test_minus(self, a, b,result):
        try:
            result = a - b
        except Exception as msg:
            print(f'\n异常用例："{msg}"')
        else:
            assert result == self.cal.minus(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('data3.yaml')), ids=['int', 'zero', "negative", 'float', 'str'])
    def test_mult(self, a, b,result):
        try:
            result = a * b
        except Exception as msg:
            print(f'\n异常用例："{msg}"')
        else:
            assert result == self.cal.mult(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('data4.yaml')), ids=['int', 'zero', "negative", 'float', 'str','wrongzero'])
    def test_div(self, a, b,result):
        try:
            result = a / b
        except Exception as msg:
            print(f'\n异常用例："{msg}"')
        else:
            assert result == self.cal.div(a, b)
