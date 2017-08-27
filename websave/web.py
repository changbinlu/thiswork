doc = 'http://docs.python-guide.org/en/latest/scenarios/scrape/'
from lxml import html
import requests
page = requests.get('https://digital-photography-school.com/11-surefire-tips-for-improving-your-landscape-photography/')
print(page.content)

