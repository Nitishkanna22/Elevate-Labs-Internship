def addition():
    try:
        print("\nYou have selected ADDITIION !!!!!!!!")
        number_1 = float(input("\nEnter the digit: "))
        number_2 = float(input("Enter the digit: "))
        result = number_1 + number_2
        print(f"\nThe final solution is {result}")

    except ValueError:
        print("Only enter numerical values")

def subtraction():
    try:
        print("\nYou have selected SUBTRACTION !!!!!!")
        number_1 = float(input("\nEnter the digit: "))
        number_2 = float(input("Enter the digit: "))
        result = number_1 - number_2
        print(f"\nThe final solution is {result}")

    except ValueError:
        print("Only enter numerical values")

def multiplication():
    try:
        print("\nYou have selected MULTIPLICATION !!!!!!!")
        number_1 = float(input("\nEnter the digit: "))
        number_2 = float(input("Enter the digit: "))
        result = number_1 * number_2
        print(f"\nThe final result is {result}")

    except ValueError:
        print("Only enter numerical values")

def division():
    try:
        print("\nYou have selected DIVISION !!!!!!")
        number_1 = float(input("\nEnter the digit: "))
        number_2 = float(input("Enter the digit: "))
        result = number_1 / number_2
        print(f"\nThe result is {result}")

    except ValueError:
        print("Only enter numerical values")

is_running = True

while is_running:
    print("\n***********************************")
    print("Enter 1 for addition")
    print("Enter 2 for subraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 5 to exit the application")
    print("*************************************")


    try:
        options = int(input("Enter the options from (1-5): "))

        if options == 1:
            addition()

        elif options == 2:
            subtraction()

        elif options == 3:
            multiplication()

        elif options == 4:
            division()

        elif options == 5:
            is_running = False
            print("Thank you for using the application")

    except ValueError:
        print("\nKindly do study the mannual clearly")
        print("Only numerical values allowed")

    
    
            