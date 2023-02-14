# Ref: https://kimsereylam.com/python/2021/03/19/how-to-use-patch-in-python-unittest.html
# in my_class.py

# Part 1:
class MyClass:
    my_attribute = 1

    def __init__(self):
        self.value = 2

    def do_something(self):
        return "hello {}".format(self.value)

    def get_client(self):
        return Client()

    def change_class_attribute(self):
        MyClass.my_attribute = "MyClass.my_attribute has been changed"

    def change_class_instance_attribute(self):
        self.my_attribute = "self.my_attribute has been changed afterwards"


def get_value():
    o = MyClass()
    return o.value

# PART 2:
class Client:
    def send(self):
        return "Sent from original client"

def send():
    return MyClass().get_client().send()

if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    a.my_attribute = 7
    print(MyClass.my_attribute, a.my_attribute, b.my_attribute)
    MyClass.my_attribute = 'MyClass--my_attribute'
    print(MyClass.my_attribute, a.my_attribute, b.my_attribute)
