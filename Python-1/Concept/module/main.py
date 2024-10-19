"""import function

user_input=""
while user_input != "exit":
    user_input = input("Enter no. of days and unit with :\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dict = { "days": days_and_unit[0], "unit": days_and_unit[1]}
    function.check_user_input(days_and_unit_dict)"""


"""from function import check_user_input

user_input=""
while user_input != "exit":
    user_input = input("Enter no. of days and unit with :\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dict = { "days": days_and_unit[0], "unit": days_and_unit[1]}
    check_user_input(days_and_unit_dict)"""


from function import check_user_input, user_input_main

user_input=""
while user_input != "exit":
    user_input = input(user_input_main)
    days_and_unit = user_input.split(":")
    days_and_unit_dict = { "days": days_and_unit[0], "unit": days_and_unit[1]}
    check_user_input(days_and_unit_dict)

# from function import *
# import function as f