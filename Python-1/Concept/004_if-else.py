calculation_of_units = 24
value_of_units = "hours"


def no_of_hours(no_of_days):
    return f"{no_of_days} has {no_of_days * calculation_of_units} {value_of_units}."


def check_user_input():
    if user_input.isdigit():
        int_user_input = int(user_input)
        if int_user_input > 0:
            calculated_value = no_of_hours(int_user_input)
            print(calculated_value)
        elif int_user_input == 0:
            print("Entered value is 0, which isn't valid")
    else:
        print("Kindly enter any integer, string isn't valid")


user_input = input("Enter number of days\n")
check_user_input()
