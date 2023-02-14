# Purpose: basics of mocking a class/method/variables using patch and patch.object
# Ref: https://kimsereylam.com/python/2021/03/19/how-to-use-patch-in-python-unittest.html
import unittest
from unittest.mock import patch

import my_class1
from my_class1 import MyClass, get_value
from my_class1 import Client, send


def test_get_value(xstr):
    return f'{xstr} {len(xstr)}'
m_str = "hellooo"

print('Testing mocking a class variable mocking the WHOLE CLASS and using return_value.\n'
      'Patching the class itself, and then using return_value to mock/replace the \n'
      'original class variable with a mocking function that returns the mocking value.')
print(f'The original (non mocked) get_value(): {get_value()}')
with patch("my_class1.MyClass") as mock:
    print('Printing my_class1.get_value() BEFORE(!) setting the value in the mocking class:')
    print(f'The before setting the value mocked:  get_value() provide:\n '
          f'  {get_value()}   (or {my_class1.get_value()} )')

    print('Now set the value for the mocked class (and assert):')
    mock.return_value.value = test_get_value(m_str)
    print(f'The mocked get_value():   {get_value()}   (or {my_class1.get_value()} )')
    mocked_value = my_class1.get_value()
    assert mocked_value == f'{m_str} {len(m_str)}'

    print('\nNote that as my_class1.MyClass is mocked, you have to define any method that is used!\n'
          'or you will get an ID instead of a value. For example, \n'
          'that class attribute or do_something function will return just the mocking id:')
    print(f'Printing my_class1.MyClass.my_attribute:      {my_class1.MyClass.my_attribute}')
    print(f'Printing my_class1.MyClass().do_something():  {my_class1.MyClass().do_something()}')


print('\nAnother way to write it, rather than using the with statement (!), getting same result is:')
#     (per https://stackoverflow.com/questions/63276033/python-unittest-mock-vs-patch)
@patch("my_class1.MyClass")
def mock_class_var(my_mock):
    m_str2 = "hello222"
    my_mock.return_value.value = test_get_value(m_str2)
    print(f'The mocked get_value():   {get_value()}   (or {my_class1.get_value()} )')
    assert get_value() == f'{m_str2} {len(m_str2)}'
mock_class_var()


print(f'\nTesting mocking a class variable, directly mocking JUST THE CLASS VARIABLE.\n'
      f'Note that patch.object is used rather than just patch')
print(f'The original my_attribute: {MyClass.my_attribute}')
with patch.object(MyClass, "my_attribute", "my_hello"):
    o = MyClass()
    print(f'MyClass.my_attribute: {MyClass.my_attribute}')
    print(f'o.my_attribute:       {o.my_attribute}')
    assert o.my_attribute == 'my_hello'

    print('\n! Note that yet the mocked class attribute can be changed by a non-mocked function'
          'that changed the class variable!')
    o.change_class_attribute()
    print(f'MyClass.my_attribute: {MyClass.my_attribute}')
    print(f'o.my_attribute:       {o.my_attribute}')
    print('\nAnd of course changing the instance variable does not affect the class one:')
    o.change_class_instance_attribute()
    print(f'MyClass.my_attribute: {MyClass.my_attribute}')
    print(f'o.my_attribute:       {o.my_attribute}')
    
    print('\nAnd of course changing the class variable to "my_hellooo" affects just the class:')
    MyClass.my_attribute = "my_hellooo"
    print(f'MyClass.my_attribute: {MyClass.my_attribute}')
    print(f'o.my_attribute:       {o.my_attribute}')

    print(f'\nNote that only my_attribute has been mocked, so the rest remain original:\n'
          f'The get_value():   {get_value()}\n'
          f'The do_something:  {my_class1.MyClass().do_something()}')
    assert get_value() == 2

    print("Changing the class variable after the patch operatio. Adding to it the string '***added':")
    o.my_attribute += "**added"
    print(f'{o.my_attribute}')


print(f'\nTesting mocking a class method\n'
      f'Note that patch.object is used rather than just patch')
print(f'The original do_something returns: {MyClass().do_something()}')
with patch.object(MyClass, "do_something", return_value="hello something"):
    o = MyClass()
    print(f'The mocked do_something():  {o.do_something()}')
    assert o.do_something() == "hello something"


print(f'\nTesting mocking a CHAINED method')
print(f'The original send gives: {send()}')
with patch.object(Client, "send", return_value="hello from chained method"):
    print(send())

print(f'\nTesting mocking a WHOLE CHAIN and then call another function that uses it. ')
with patch.object(MyClass, "get_client") as mock:
    mock.return_value.send.return_value = "hello from whole chain mock"
    print(f'The mocked my_class1.send():  {my_class1.send()}')
    assert my_class1.send() == "hello from whole chain mock"


if __name__ == '__main__':
    unittest.main()
