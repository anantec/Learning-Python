# this is day 4 of learning python 

#  today I learned some concept about conditional loops like: if if-else if-else if -else


#  the code below i wrote is the code of just if condition
def agecal (a):
    if(a>18):
        print("you are above 18 ")

agecal(20)

# the code below is if-else block

def verify(a):
    if(a>18):
        print("you are eligible to visit this site")

    else:
        print("you are too young to visit this site")

verify(8)


# now here comes the if else_if else block

def fun1(a):
    if(a<18):
        print("you are too young to visit this park")
    elif(a<50):
        print("You are too old to visit this park")
    else:
        print("you are able to visit this park")

fun1(12)
# this above will give the output of first condition
fun1(56)
# the second condition will run
fun1(45)
# third condtion will run
    