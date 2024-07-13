#  this is a fizz fuzz program in this we will display fizz if the number given by user is divisible by 3 if the number is divisible by 5 then we print fuzz

# if the number is divisible by both the number we will print fizzfuzz


while True:
    try:
        a = int(input("Enter the number to check whether your number gets fizz or fuzz: "))

        if(int(a)%5==0 ):  # First, check if divisible by 5
            if(int(a)%3==0):  # Then, check if it's also divisible by 3
                print("Great! Your number got FizzFuzz")
            else:
                print("Your number got fuzz")
            res = input("do you want to continue? (y/n)")
            if(res.lower()== 'n' ):
                break

        elif(int(a)%3==0 ):  # Second, check if divisible by 3
            print("Your number get fizz")
            res = input("do you want to continue? (y/n)")
            if(res.lower()== 'n' ):
                break

        else:
            print("Sorry your number didn't get anything")
            res = input("do you want to continue? (y/n)")
            if(res.lower()== 'n' ):
                break

    except ValueError:
        print("Oops! That's not an integer.")