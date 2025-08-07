
# kwargs - key word arguments
# Dictinary{key:value}


def greet(name,nationality):
    print("Name is",name)
    print("From ", nationality)

# kwargs also fix mixup

#greet("John","Kenya")
greet(nationality="Kenya", name="John")

#KWARGS PROFILE
def employee(**kwargs):
    print (kwargs)
    print("Name is", kwargs["name"])

#{key values}
employee(name="John", age=30, nationalit="Kenya")
employee(name="Jane", age=25, nationality="USA")

def mixed(*args, **kwargs):
    print(args)
    print(kwargs)
    print("Name is", kwargs["name"])