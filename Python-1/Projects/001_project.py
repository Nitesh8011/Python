# Ask user goal and date, and answer back the day or hours remaining

from datetime import datetime

user_input = input("Enter goal and deadline of goal with . separated\n")

input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

# print (goal, deadline)

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
current_date = datetime.now()
time_remaining = deadline_date - current_date

hours_remaining = int(time_remaining.total_seconds() / 60 / 60)

print(f"Hey User, time remaining for your goal: {goal} is {time_remaining.days} days")
print(f"Hey User, time remaining for your goal: {goal} is {hours_remaining} hours")


# learn python:2.12.2024