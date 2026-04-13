# Iterable = An object/collection that can be looped over

def fn():

    name = "Jose"

    for char in name:
        print(char)

def fn2():
    my_dict  = {
        "name": "Jose",
        "age": 30,
        "city": "New York"
    }
    
    print(my_dict.items())
    for key in my_dict:
        print(key)

fn2()
