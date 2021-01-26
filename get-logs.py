import re
import requests
from bs4 import BeautifulSoup

city_url = 'https://www.cityofithaca.org'
log_url = f'{city_url}/654/Incident-Log'
pattern = re.compile('.*[0-1] to [0-9].*')

# get the index page to all incident logs
html_text = requests.get(log_url).text
soup = BeautifulSoup(html_text, 'html.parser')

# look for links that roughly match the '<date> to <date>' pattern
for link in soup.find_all('a'):
    if pattern.match(link.text):
        # download and write to disk
        r = requests.get(f'{city_url}{link.get("href")}')
        file_name = link.text + '.pdf'

        print(f'Saving {link.get("href")} to {file_name}')
        with open(file_name, 'wb') as f:
            f.write(r.content)
