import json

employee = '{"id":"09", "name": "Aman", "department":"Finance"}'

try:

    # json.load(filename)
    with open('horoscope_data.json','r') as file:
        data = json.load(file)


    # unformatted data
    date = data['data']['date']
    horoscope = data['data']['horoscope_data']
    print(f'Data is {date}: {horoscope}')


    # format data output
    formatted_data = json.dumps(data, indent=2)
    print(formatted_data)


    # with json.loads(string)
    employee_dict = json.loads(employee)
    for key in employee_dict: # Iterate through the dictionary and print key-value pairs
        print(key, ":", employee_dict[key])


except Exception as e:
    print("Error:", e)
