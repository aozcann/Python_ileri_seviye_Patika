# def print_func():
#     print("hey")

# def decorator_func(func):
#     def wrapper_func():
#         return func()

#     return wrapper_func

# decorator_print = decorator_func(print_func)
# decorator_print()

# def decorator_func(func):
#     def wrapper_func():
#         print(f"the name of the function is {func.__name__} ") 
#         return func()

#     return wrapper_func

# decorator_print = decorator_func(print_func)
# decorator_print()

# @decorator_func
# def print_func():
#     print("heyy")

# print_func()

def func(name ,number):
    print(f"Name : {name} , number : {number} ")

func("jack",102)

def decorator_func(func):
    def wrapper_func(*args):
        print(f"the name of the function is {func.__name__} ") 
        return func(*args)

    return wrapper_func

@decorator_func
def func(name ,number,phone):
    print(f"Name : {name} , number : {number} , phone :{phone} ")

func("jake",103,12314515)

