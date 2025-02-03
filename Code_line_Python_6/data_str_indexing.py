# 1- we create the list first 

food=["pizza","pasta","burger","noodles","rice"]
print(food)

# we use the indexing to access the data from the list
print(food[0])

# we use the negative indexing to access the data from the list
print(food[-1])

# now we simply relocate the new value to the valudes in the dataset     
food[1]="briyani"

print(food[1])
print(food)

# 2- we create the tuple

cordinates=(2.59,3.59,4.59)
print(cordinates)
print(cordinates[1])

# 3- we create the dictionary

person={"name":"khawar","age":25,"country":"pakistan"}
print(person)
print(person["name"])
print(person["country"])

# 4- we create the set

s={1,2,3,4}
print(s)

s.add(5)        # add the value 5 in the set s 
print(s)