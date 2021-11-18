import requests

print('Input the URL:')
url = input()  # 'https://api.quotable.io/quotes/-CzNrWMGIg8V'
print()

try:
    r = requests.get(url)
    data = r.json()
    data_keys = data.keys()
except ConnectionError:
    print('Connection error')

if 'content' in data_keys:
    print(data['content'])
else:
    print('Invalid quote resource!')
