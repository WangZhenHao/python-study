# keyword arguments = arguments preceded by an identifier when we pass them to a function.
#                     The order of the arguments doesn't matter, unlike positional arguments.
#                     Python knows the names of the arguments that are being passed.


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


# hello(title='Mr.', last='Smith', first='John', greeting='hello')

# arbitrary arguments 
# *args = arbitrary arguments  
# allows us to pass a variable number of arguments into a function.


def add(*nums):
    total = 0
    for args in nums:
        total += args
    return total

# print(add(1,2,3))


# **kwargs = arbitrary keyword arguments
# allows us to pass a variable number of keyword arguments into a function.

def address(**kwargs):
    # print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# address(street="123 Main St", city="New York", state="NY", zipcode=10001)

# arr = [{"age": 1},{"age": 21},{"age": 31},{"age": 41},{"age": 51}]

# for index in range(len(arr)):
#     print(index)

def shiping_able(*args, **kwargs):
      for args in args:
          print(args, end=" ")
      print(" ")
      for key, value in kwargs.items():
          print(f"{key}: {value}")

shiping_able("John", "Smith", street="123 Main St", city="New York", state="NY", zipcode=10001)