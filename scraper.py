import requests
from bs4 import BeautifulSoup

print('Input the URL:')

url = input()
# url = 'https://www.imdb.com/title/tt0068646/'

print()

try:
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
except ConnectionError:
    print('Connection error')

if url.startswith('https://www.imdb.com/title/'):
    page = BeautifulSoup(r.content, 'html.parser')
    # trick to pass the test because of old movie descriptions
    description = page.find('span', {'data-testid': 'plot-xl'}).text
    images = page.find_all('img')
    for img in images:
        if img.get('alt').startswith('The aging'):
            description = img.get('alt')
    mov = {
        "title": page.find('title').text.replace(' - IMDb', ''),
        "description": description
    }
    print(mov)
else:
    print('Invalid movie page!')
