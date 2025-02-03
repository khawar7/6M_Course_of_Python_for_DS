# what does it mean by the control flow statament in python?

# conditional statament or if statements (<,>,==,!=,>=,<=)

## 1- if statement
x=0

if x<0:
    print("x is negative")
elif x==0:
    print("x is zero")
else:
    print("x is positive")

# 2- for loop   
x=[1,2,3,4,5]

for i in x:
    print(i)

# 3- while loop in python 
x=0

while x<5:
    print(x)
    x=x+1

#  break in while loop
x=[1,2,3,4,5]

for i in x:
    if i==3:
        break
    print(i)

# continue in while loop
x=[1,2,3,4,5]

for i in x:
    if i==3:
        continue
    print(i)

# pass in while loop
x=[1,2,3,4,5]

for i in x:
    if i==3:
        pass
    print(i)
