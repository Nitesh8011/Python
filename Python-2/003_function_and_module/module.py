import calculator

option = input("Enter add, sub, multi or div: ")
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

if option == 'add':
    print("Result: ",calculator.addition(x,y))

elif option == 'sub':
    print("Result: ", calculator.subtraction(x,y))

elif option == 'multi':
    print("Result: ", calculator.multiplication(x,y))

elif option == 'div':
    print("Result: ", calculator.division(x,y))