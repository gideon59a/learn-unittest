#Purpose: More on mocked method using patch.object and return_value
# patch.object(MyClient2, "containers", return_value=MockMyContainers):

import unittest
from unittest.mock import patch
from my_class2 import MyClient2

some_global = 100

print('****Regular NON-MOCKED run***')
# = MyClient2("a", "b")
print(f'MyClient2 type: {type(MyClient2)}')
print(f'MyClient2() type: {type(MyClient2("",""))}')
cl1 = MyClient2("a", "b")
cont1 = cl1.containers()
e1 = cont1.exists('myname')
print(f"Runinig exists('myname'):  {e1}")

print('\n****MOCKING run***')
class MockMyClient2:
    def __init__(self, url, config):
        self.url = url
        self.config = config

    def containers(self):
        return MockMyContainers("real one")

class MockMyContainers:
    global some_global
    def __init__(self, str1) -> None:
        self.str1 = str1

    @staticmethod
    def exists(name):
        print(f'At MOCKED containers.exists with name: {name}')
        if name:
            return True
        else:
            return False

    @staticmethod
    def run():
        print('At MOCKED run')
        return True

    @staticmethod
    def run2(**kwargs):
        print(f'At run2, printing some_global: {some_global}')
        if some_global == 100:
            return True
        else:
            return False


class TestLcmApi(unittest.TestCase):
    def test_MyClient2(self, *newargs, **newkeywargs):
        global some_global
        print(f'Mocking a class method that returns some class object')
        with patch.object(MyClient2, "containers", return_value=MockMyContainers):
            a = MyClient2("a", "b")
            print(f'MyClient2 type (left un mocked): {type(MyClient2)}')
            print(f'MyClient2() type (left un mocked): {type(MyClient2("", ""))}')
            not_mocked = MyClient2("a", "b")  # Not mocked as just its container method is mocked
            print(f'not_mocked: {not_mocked}')
            cont_mocked = not_mocked.containers()  # the mocked method
            print(f'cont_mocked: {cont_mocked}')
            exists1 = cont_mocked.exists('myname')  # runs the mocking method
            run1 = cont_mocked.run()
            print(f"MOCKED exists1: {exists1}")
            print(f"MOCKED* run1: {run1}")
            self.assertEqual(exists1, True)
            self.assertEqual(run1, True)

            print('\nVerify that the method can be called more than once dynamically changed')
            run2 = cont_mocked.run2()
            print(f'run2: {run2}')
            print(f'some_global: {some_global}')
            assert run1
            some_global = 200
            run2 = cont_mocked.run2()
            print(f'run2: {run2}')
            print(f'some_global: {some_global}')
            assert not run2

if __name__ == '__main__':
    unittest.main()
