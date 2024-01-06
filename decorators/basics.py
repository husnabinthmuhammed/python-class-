"""
decorators are allows you to modify the behaviour of a function or class without directly its sourcre code.

@symbol
"""


def deco_func(func):
    def wrapper():
        print("Before func execution")
        func()
        print("After function execution")

    return wrapper


@deco_func
def my_func():
    print("Inside the my_func")


my_func()


# _________________________________________________

def decor_func(func):
    def inner():
        print("I got decorator")
        func()

    return inner


@decor_func
def test_fun():
    print("a test func")


test_fun()
# decorated_function = decor_func(test_fun)
# decorated_function()
