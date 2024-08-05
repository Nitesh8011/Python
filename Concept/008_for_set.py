calculation_of_units = 24
value_of_units = "hours"

def no_of_hours(no_of_days):
    return f"{no_of_days} has {no_of_days * calculation_of_units} {value_of_units}"


def check_user_input():
    try:
        user_input_check = int(no_of_units)
        if user_input_check > 0:
            calculated_value = no_of_hours(user_input_check)
            print(calculated_value)
        elif user_input_check == 0:
            print("Enter value except 0")
        else:
            print("Enter positive value only")
    except:
        print("Entered valid input")
    

user_input=""
while user_input != "exit":
    user_input = input("Enter any number\n")
    list_of_days = user_input.split(", ")
    for no_of_units in set(list_of_days):
        check_user_input()