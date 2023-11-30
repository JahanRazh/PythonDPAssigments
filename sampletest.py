
#These functions should cover Task 2

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: Cannot divide by zero.")
        return None
    return x / y

def power(x, y):
    return x ** y

def remainder(x, y):
    if y == 0:
        print("Error: Cannot calculate remainder with zero.")
        return None
    return x % y

#-------------------------------------

#This function should cover Task 1 (Section 2) and Task 3

def select_op(choice):
    if choice == '+':
        return add
    elif choice == '-':
        return subtract
    elif choice == '*':
        return multiply
    elif choice == '/':
        return divide
    elif choice == '^':
        return power
    elif choice == '%':
        return remainder
    elif choice == '#':
        return -1  # Special code to indicate program termination
    elif choice == '$':
        print("Resetting...")
        return None  # Special code to indicate program reset
    else:
        print("Invalid input. Please enter a valid operation.")
        return None

#End the select_op(choice) function here
#-------------------------------------

# This is the main loop. It covers Task 1 (Section 1)
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    operation = select_op(choice)
    if operation == -1:
        # program ends here
        print("Done. Terminating")
        exit()
    elif operation is not None:
        # valid operation, proceed with calculation
        if operation == add or operation == subtract or operation == multiply or operation == divide or operation == power or operation == remainder:
            x = float(input("Enter first operand: "))
            y = float(input("Enter second operand: "))
            result = operation(x, y)
            if result is not None:
                print(f"Result: {result}")
    elif operation is None:
        # Reset the program
        continue
