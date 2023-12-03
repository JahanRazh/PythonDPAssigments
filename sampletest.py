
#These functions should cover Task 2

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        print("float division by zero")
        return None
    return x / y

def power(x, y):
    return x ** y

def remind(x, y):
    if y == 0:
        print("Error: Cannot calculate remainder with zero.")
        return None
    return x % y

#-------------------------------------

#This function should cover Task 1 (Section 2) and Task 3

def select_op(choice):
    if (choice == '#'):
        return -1  # Special code to indicate program termination
    elif choice == '$':
        print("Resetting...")
        return 0  # Special code to indicate program reset
    elif (choice in('+','-','*','/','^','%')):
        while True:
            num1 = str(input("Enter first number: "))
            print(num1)
            if num1.endswith('$'):
                return 0
            if num1.endswith('#'):
                return -1
            try:
                x1 = float(num1)
                break
            except:
                print("Not a valid number,please enter again")
                continue
        
        while True:
            num2 = str(input("Enter second number: "))
            print(num2)
            if num2.endswith('$'):
                return 0
            if num2.endswith('#'):
                return -1
            try:
                x2 = float(num2)
                break
            except:
                print("Not a valid number,please enter again")
                continue
    
        if (choice == '+'):
            print(x1, "+", x2, "=", add(x1,x2))
        elif (choice == '-'):
            print(x1, "-", x2, "=", sub(x1,x2))
        elif (choice == '*'):
            print(x1, "*", x2, "=", mul(x1,x2))
        elif (choice == '/'):
            print(x1, "/", x2, "=", div(x1,x2))
        elif (choice == '^'):
            print(x1, "^", x2, "=", power(x1,x2))
        elif (choice == '%'):
            print(x1, "%", x2, "=", remind(x1,x2))
        else:
            print("Invalid input. Please enter a valid operation.")
            return None
    else:
        print("Unrecognized operation")
        
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
    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")
        exit()
  
