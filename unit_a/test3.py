import unittest
from unittest.mock import patch
from podman.api import cached_property

from my_class3 import MyClient3
import my_class3

print('\n**** run 3a, with patch return value. No "with" statement ***')
@patch('my_class3.MyContainers.exists', return_value='RETURN-From-patch-3a')
@patch('my_class3.MyContainers.run', return_value='True-From-path-3a')
def test_patch1(*args):
    m_client = my_class3.MyClient3("xx", "yy")
    #print(f"mocked exists: {m_client.containers.exists()}")
    exists = m_client.containers.exists()
    print(f"mocked exists: {exists}")
    run = m_client.containers.run()
    print(f'mocked run   : {run}')
test_patch1()

print('\n**** run 3b, with patch return value. Using WITH statement ***')
class Test4(unittest.TestCase):
    @patch('my_class3.MyContainers.exists', return_value='RETURN-From-patch-3b-WITH')
    @patch('my_class3.MyContainers.run', return_value='True-From-path-3b-WITH')
    def test_using_with(self, *newargs, **newkeywargs):
        with my_class3.MyClient3("xx", "yy") as m_client:
            print(f'mock .exists: {m_client.containers.exists()}')
            exists = m_client.containers.exists()
            print(f'mocked exists: {exists}')
            run = m_client.containers.run()
            print(f'mocked run   : {run}')



if __name__ == '__main__':
    unittest.main()
