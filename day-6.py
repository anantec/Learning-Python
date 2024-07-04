# day 6 of learning python

#  today we learned about tuples and dictionary

# dictionary is mutable data structures that allow you to store key-value pairs
# these are denoted by {}

# where as tuples are donated by []

tup= ['anant singh', 19, 13*4]

print(tup)

course = "MCA"

# {
# tup1=tup + (course,)
# print(tup1)}

# the above code will throw an error because a tuple has immutable proprty that's why we can't add any value

tup.pop()
print(tup) 

# now we'll see some thing about dictionary

dic = {
    "Mango Juice": 120,
    "chocolate shake": 150,
    "Coffee":200
}

print(dic)
print(dic["Mango Juice"])
print(len(dic))