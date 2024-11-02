def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if y != 0:
        return x/y
    else:
        return "Cannot divide by zero"


# option = input("Enter what you wanna do out of add, sub, multi or div: ")
# x = float(input("Enter the value for x: "))
# y = float(input("Enter the value of y: "))

# if option == 'add':
#     print("Addition: ",addition(x,y))

# elif option == 'sub':
#     print("Subration: ",subtraction(x,y))

# elif option == 'multi':
#     print("Multiplication: ",multiplication(x,y))

# elif option == 'div':
#     print("Division: ",division(x,y))

# else:
#     print("Enter correct option ;)")