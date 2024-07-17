stunt= {}

work = False

while not work:
    name = input (str("Enter the name you want to add: "))
    grade = input("Enter the grade: ")

    stunt[name] = grade

    print(stunt)
    cnf = input("Do you want to add more data (Y/N)? ").lower()

    if cnf == 'y':
        work = False

    else:
        work = True