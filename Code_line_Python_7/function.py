# functions in python is a block of code that only run when it is called. you can pass data in
# a function that is paremeter into a function. fucntion can return data as  result. In python
# a the fucntion is defined using def keyword

# 1- functions
# lets create a function

def hello():
    print("hello")
    print("how are you?")

hello()

def hello(name):
    print("hello",name)
    print("how are you?")

hello("khawar")

# 2- retun values
def sqaure(num):
    return num*num

print(sqaure(5))

#3- recursion function

def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))

# lamda function 

x= lambda a: a + 10
print(x(10))

y=lambda a,b: a*b
print(y(5,6))