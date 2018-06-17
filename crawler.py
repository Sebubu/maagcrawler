import requests
from bs4 import BeautifulSoup


class OpenIdeoItem:
    def __init__(self, item):
        self.item_soup = item

    @property
    def title(self):
        return self.item_soup.h1.a.string

    @property
    def href(self):
        return self.item_soup.h1.a['href']
    

website = 'https://challenges.openideo.com/challenge/gratitude-in-the-workplace/feedback?page={page}&order=newest'

nb_pages = 2

ideo_items = []
for page_number in range(1, nb_pages):
    page_url = website.format(page=page_number)
    result = requests.get(page_url)
    soup = BeautifulSoup(result.content, 'html.parser')
    items = soup.find_all('div', {'class': 'main-item-info'})

    for item in items:
        ideo_item = OpenIdeoItem(item)
        ideo_items.append(ideo_item)


for ideo_item in ideo_items:
    print(ideo_item.title)
    print(ideo_item.href)
    print()
