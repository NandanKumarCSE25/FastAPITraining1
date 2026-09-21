#concept: decorator is a python function 
#decorators are the functions that modify the functionality of another function.
def my_decorator(func):
    def wrapper():
        print("before");
        func()
        print("after");
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello() 