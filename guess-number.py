import random
# random is a module

a = 1
b= 100


random_num = random.randint(a,b)


attempt = 0

while True:
 
    user_guess = int(input(f"Guess a number between {a} and {b}: "))

    # Check if the user's guess is higher or lower than the random number
    if user_guess > random_num:
        print("Too high! Try again.")
    elif user_guess < random_num:
        print("Too low! Try again.")
    else:
        print(" Congratulations! You guessed the correct number!")
        break

  
    attempt += 1

print(f"It took you {attempt} attempts to guess the correct number.")