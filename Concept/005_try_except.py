calculation_of_units = 24
value_of_units = "hours"


def no_of_hours(no_of_days):
    return f"{no_of_days} has {no_of_days * calculation_of_units} hours."


def check_user_input():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = no_of_hours(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("Your entered 0, plus enter any positive value!")
        else:
            print("Enter any positive value")
    except ValueError:
        print("Kindly enter any valid input")


user_input = input("Enter no. of days\n")
check_user_input()