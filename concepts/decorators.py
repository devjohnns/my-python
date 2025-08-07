# Decorators
# Extend or modify the


def my_deco(fun):
    def wrapper():
        print("Before function run")
        fun()
        print("Function completed running")
    return wrapper

@my_deco
def hello():
    print("Hello world")


my_deco
def greet():
    print("Enda uoge")

greet()
hello()


    