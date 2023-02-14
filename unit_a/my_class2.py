class MyClient2:
    def __init__(self, url, config):
        self.url = url
        self.config = config

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
        return 'yyy'
