import json
import requests

url = 'https://api.bitso.com/v3/available_books/'
response = requests.get(url)

if response.status_code == 200:
    json = json.loads(response.content.decode('utf-8'))
    data = [float(x['maximum_value']) for x in json['payload']]
    print(max(data))

else:
    print('NON')
