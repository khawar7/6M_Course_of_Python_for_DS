# syntax error
print("Hello, " + name + "!") # syntax error

# logical error or name error
name = "Alice"
print("Hello, " + name + "!")

# module not found error
import maths
print(maths.sqrt(4)) # module not found error

# index error
my_list = [1, 2, 3]
print(my_list[4]) # index error

# key error
my_dict = {"name": "Alice"}
print(my_dict["age"]) # key error

# type error
x = "hello"
y = 10
print(x + y) # type error

# value error
print(int("hello")) # value error

# zero division error
print(1 / 0) # zero division error

# name error
try:
    print(unknown_variable)
except NameError:
    print("Variable is not defined") # name error

# attribute error
class MyClass:
    def __init__(self):
        self.attribute = "value"
obj = MyClass()
print(obj.attribute) # attribute error

# file not found error
file = open("file.txt") # file not found error

# import error
import unknown_module # import error

# print error
try:
    print(1 / 0)
except ZeroDivisionError:
    print(1 / 0) # print error

# unbound local error
try:
    x = x + 1
    except UnboundLocalError:
        print("Variable is not defined") # unbound local error

# memory error
try:
    x = "hello" * 10 ** 6
    except MemoryError:
        print("Memory is full") # memory error

# recursion error
try:
    def factorial(n):
        return n * factorial(n - 1)
    print(factorial(1000)) # recursion error

# time out error
try:
    import time
    time.sleep(10) # time out error 
