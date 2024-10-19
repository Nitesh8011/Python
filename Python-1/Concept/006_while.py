calculation_of_units = 24
value_of_units = "hours"


def no_of_hours(no_of_days):
    return f"{no_of_days} has {no_of_days * calculation_of_units} {value_of_units}"


def check_user_input():
    try:
        user_input_check = int(user_input)
        if user_input_check > 0:
            calculated_value = no_of_hours(user_input_check)
            print(calculated_value)
        elif user_input_check == 0:
            print("Your entered 0, plus enter any positive value!")
        else:
            print("Enter any positive input")
    except ValueError:
        print("Enter any valid input")


user_input=""
while user_input != "exit":
    user_input = input("Enter number of days\n")
    check_user_input()