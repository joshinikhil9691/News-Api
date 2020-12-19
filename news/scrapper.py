import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep
from.models import Story

def print_headlines():
    url = 'https://inshorts.com/en/read'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    stories = soup.find_all(attrs={'itemtype': 'http://schema.org/NewsArticle'})
    for story in stories:
        headline = story.find('span', {'itemprop': "headline"}).get_text()
        date = story.find('span', {'class': "date"}).get_text()
        author = story.find('span', {'class': 'author'}).get_text()
        content = story.find('div', {'class': 'news-card-content news-right-box'}).get_text()
        # link = story.find('a', {'class': 'source'}).text

        print({'headline': headline, 'date': date,
               'author': author, 'content': content})

        Story.objects.create(
            headline=headline,
            date=date,
            author=author,
            content=content
        )

        sleep(5)

print_headlines()