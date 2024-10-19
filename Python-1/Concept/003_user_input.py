calculation_of_units = 24
value_of_units = "hours"

def no_of_hours(no_of_days):
    return f"{no_of_days} has {no_of_days * calculation_of_units} number of {value_of_units} "

user_input = input("Enter the number of days\n")
int_value = int(user_input)

calculated_value = no_of_hours(int_value)

print(calculated_value)