
# Decorator  = A function that takes a function as an argument and returns a function
#              A function that extends the behavior of another function

def add_sprikles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprikles")
        print(func)
        print(args, kwargs)
        func(*args, **kwargs)

    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge")
        func(*args, **kwargs)

    return wrapper

@add_sprikles
@add_fudge
def get_ice_create(flavor):
    print(f"Making ice cream, {flavor}")


get_ice_create('chocolate')