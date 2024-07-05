# this day 7 of learning python from scratch

# today I saw some basic concept of looping

# first we are going to give a look on for loop

list=["1","2","3","4","5"]

for i in list :
    print(i)
    i=+1

# the above code will print all the items in list until the list ends


print("\n")
print("for loop with an increment of 1")



for i in range(10,21):
    print(i)

# it will automatically increment the variable or value by 1 and the above code says that the  value will start from  10 and ends at 20


# now i am going ro write a code for increment of 2
print("\n")
print("for loop with an increment of 2")

for i in range(0,20,2):
    print(i)


# there is another loop named (While) loop it will work till the condtion is true

print("\n")
print("while loop with an increment of 2")
while(i>20):
    print(i)
    i+=2

# there is only two loops in python