import unittest
from unittest.mock import patch
from podman import PodmanClient
from unittest.mock import MagicMock
#import podman.client
import podman

print(f'Original PodmanClient class: {podman.client.PodmanClient}')
class MockPodmanClient:  #(MagicMock):
    def containers(self):
        print('AT MockPodmanClient containers')
        return MockMyContainers("real one")

class MockMyContainers:
    global some_global
    def __init__(self, str1) -> None:
        self.str1 = str1
        print(f'MockMyContainers __init__ with str: {str1}')

    @staticmethod
    def exists(name):
        print(f'At MOCKED containers.exists with name: {name}')
        if name:
            return False
        else:
            return 'NAME SHOULD HAVE BEEN DEFINED'

    @staticmethod
    def run():
        print('At MOCKED run')
        return True

#class TestMyProg(unittest.TestCase):
#    def setUp(self):
#        podman.client.PodmanClient = MockPodmanClient
#    def test_my_program(self):
#        res1 =

def my_real_program():
    client = PodmanClient(base_url=f"unix://abc")
    print(f'111aa {client.containers}')  # without the mocking we'd get <podman.domain.containers_manager.ContainersManager object>
    print(f'111bb {client.containers.exists}')
    exists = client.containers.exists("container_name")
    print(f'exists type: {type(exists)} and value: {exists}')
    if exists != False:
        print("***** Error !!!!! Verify exists is not an object id, implying is has no mocked value")
    if not client.containers.exists("container_name"):
        client.containers.run(image="img")
        print('(in my_real_program) not client.containers.exists (False)')
    else:
        print('(in my_real_program) client.containers.exists (True)')
    print("(in my_real_program) here after run")
'''
@patch("podman.client.PodmanClient")
def mock_class1(podman_mock):
    print('11111111111')
    podman_mock.return_value.containers.return_value = MockPodmanClient.containers("aaa")
    client = PodmanClient(base_url=f"unix://abc")
    print(f'(mock_class1) client: {client}')
    print(f'(mock_class1) client.containers: {client.containers}')
    #my_real_program()
#mock_class1()

@patch("podman.client.PodmanClient.containers")
def mock_class2(podman_mock):
    print('2222222222')
    podman_mock.return_value.containers = MockPodmanClient.containers("aaa")
    client = PodmanClient(base_url=f"unix://abc")
    #print(f'*****2 client: {client}')  # NOT MOCKED
    print(f'(debug2) client.containers: {client.containers}')  # MOCKED!
    my_real_program()
#mock_class2()

@patch.object(podman.client.PodmanClient, "containers", MockPodmanClient.containers)
def mock_class3():
    print('33333333333')
    #client = PodmanClient(base_url=f"unix://abc")
    #print(f'*****2 client: {client}')  # NOT MOCKED
    #print(f'(debug3) client.containers: {client.containers}')  # MOCKED!
    my_real_program()
mock_class3()
'''

def exists(obj, stam1):
    return False

def run(obj, img="img1", **kwargs):
    return True

#Patching Python39\Lib\site-packages\podman\domain\containers_manager.py
@patch.object(podman.domain.containers_manager.ContainersManager, "exists", exists)
@patch.object(podman.domain.containers_manager.ContainersManager, "run", run)
def mock_class4():
    print('444444444')
    my_real_program()
mock_class4()



if __name__ == '__main__':
    unittest.main()
