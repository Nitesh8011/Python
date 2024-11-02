import json
import requests

try:
    responce = requests.get('https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today')
    data = responce.json()

    # json.dump(dict, file_pointer)
    with open('horoscope_data.json','w') as file:
        json.dump(data, file)
    
    # json.dumps(dict)
    res = json.dumps(data)
    print(data)

    print("Successfully dumped data")

except Exception as e:
    print(f"Failed to dump ", {e})