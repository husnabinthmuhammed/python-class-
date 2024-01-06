def upper_decor(fun):
    def wrapper(name):
        result = fun(name)
        return result.upper()
    return wrapper

@upper_decor
def hello_name(name):
    return "hello "+name


print(hello_name("husna"))