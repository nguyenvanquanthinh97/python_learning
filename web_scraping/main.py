import requests
import pprint
from bs4 import BeautifulSoup


def hacker_news_scraping(start=1, end=1):
    news = []
    for pageIdx in range(start, end + 1):
        news = news + scraping(pageIdx)
    return sort_hackernews(news)


def scraping(page):
    res = requests.get(f"https://news.ycombinator.com/news?p={page}")
    soup = BeautifulSoup(res.text, 'html.parser')

    links = soup.select("span.titleline > a:first-child")
    subtexts = soup.select(".subtext")
    return create_custom_hackernews(links, subtexts)


def create_custom_hackernews(links, subtexts):
    hacker_news = []
    for i, _ in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        votes = subtexts[i].select(".score")
        if len(votes):
            point = int(votes[0].getText().replace(" points", ""))
            if point >= 100:
                hacker_news.append({"title": title, "link": href, "votes": point})
    return sorted(hacker_news, key=lambda news: news["votes"], reverse=True)


def sort_hackernews(news):
    return sorted(news, key=lambda news: news["votes"], reverse=True)


pprint.pprint(hacker_news_scraping(1, 2))
