# for loop with contiue and break
for i in range(10):
    if i == 5:
        continue
    elif i == 8:
        break
    print(i)

# for loop with list
list = ["Apple","Orange","Mango"]
for a in list:
    print(a)


# while loop
i = 0
while i < 15:
    print(i)
    i += 1

# for loop with dictionary
person = {"name": "Nitesh", "Age": '18', "Job":"DevOps"}
for key,value in person.items():
    print(f'{key}: {value}')

# for loop with else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("loop completed")