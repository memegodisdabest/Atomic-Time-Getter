import requests

url = 'https://time.is/atomic'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    # parse the response data to get the atomic time
    atomic_time = ...
    print(f'Atomic time: {atomic_time}')
