# what is the nested loop in the python?

# nested loop
x=0
y=0

while x<5:
    y=0
    while y<5:
        print(x,y)
        y=y+1
    x=x+1

# nusted for loop
x=0
y=0

for x in range(5):
    for y in range(5):
        print(x,y)

# for loop inside the while loop
x=0
y=0

while x<5:
    for y in range(5):
        print(x,y)
    x=x+1

# while loop insdie for loop   
x=0
y=0

for x in range(5):
    while y<5:
        print(x,y)
        y=y+1
