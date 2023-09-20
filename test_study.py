import pytest


class TestStudye(object):
    a =[]
    @pytest.fixture()
    def up_class(self):
        self.a = [1,2,3]
        print('i am class fixture',self.a)
        return self.a

    # @pytest.mark.parametrize('x',a)
    def test_main(self,up_class):
        print('test beginning now',up_class[:])

if __name__ == '__main__':
    pytest.main(['-s', 'test_study.py'])