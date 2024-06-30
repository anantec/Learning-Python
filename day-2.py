# Day 2 of learning python from scratch

#  function is nothing but some lines of code which help to perform some specific task or some particular task

# we are going to create a simple function to add two numbers
 
def add (a,b): 
 print("sum of two numbers is: "  + str(a+b));

add(100,118)

#  now we are going to create a function for the multiplication

def multiply (x,y):
 res = x*y
 print("The multiplication of two given numbers is: " + str(res))

multiply(5,10)

# lets create a simple program where the user will get the remainder as output

def Resp(a,b):
 cons = a%b
 print("The remainder of the given number is : " + str(cons))

Resp(10,2)

# same as above lets create a simple program where the user will get the quotient as output

def Divs(a,b):
 cons = a/b
 print("The quotient of the given number is : " + str(cons))

Divs(10,2)