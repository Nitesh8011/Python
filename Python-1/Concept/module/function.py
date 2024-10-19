def no_of_hours(no_of_days, units):
    if units == "hours":
        return f"{no_of_days} days has {no_of_days * 24} hours"
    elif units == "minutes":
        return f"{no_of_days} days has {no_of_days * 24 * 60} minutes"
    else:
        return "Unsupported unit"


def check_user_input(days_and_unit_dict):
    try:
        user_input_check = int(days_and_unit_dict["days"])
        if user_input_check > 0:
            calculated_value = no_of_hours(user_input_check,days_and_unit_dict["unit"])
            print(calculated_value)
        elif user_input_check == 0:
            print("Enter value except 0")
        else:
            print("Enter any positive input")
    except ValueError:
        print("Enter valid input")


user_input_main = "Enter no. of days and unit with :\n"