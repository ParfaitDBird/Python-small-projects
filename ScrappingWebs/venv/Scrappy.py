import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes (hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hackers_news(links,subtext):
    hn=[]
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title' : title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

for a in range(2):
    url = 'https://news.ycombinator.com/news?p=' + f'{str(a+1)}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    link = soup.select('.storylink')
    subtext = soup.select('.subtext')
    print(f'RESULTADOS PAGINA {a+1}')
    pprint.pprint(create_custom_hackers_news(link,subtext))
