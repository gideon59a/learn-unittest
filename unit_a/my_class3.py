from podman.api import cached_property

class MyClient3:
    def __init__(self, url, config):
        self.url = url
        self.config = config

    def __enter__(self):
        print('At MyClient3 __enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('At MyClient3 __exit__')
        return

    @cached_property
    def containers(self):
        return MyContainers("real one")


class MyContainers:
    def __init__(self, str1) -> None:
        self.str1 = str1

    def exists(self, name):
        print(f'At REAL containers.exists with name: {name}')
        if name:
            return 'REAL True'
        else:
            return 'REAL False'

    def run(self):
        print('At real run')
        return 'REAL yyy'
