calculation_of_units = 24 * 60
value_of_units = "hours"


def no_of_hours(no_of_days):
    print (f"{no_of_days} has {no_of_days * calculation_of_units} {value_of_units}")

no_of_hours(20)


def scope(num_days):
    my_var = "variable inside function"
    print(num_days)
    print(value_of_units)
    print(my_var)

scope(12)