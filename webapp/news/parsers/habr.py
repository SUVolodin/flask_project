from datetime import datetime, timedelta
import locale
import platform

from bs4 import BeautifulSoup
from webapp.news.parsers.utils import get_html, save_news

if platform.system() == "Windows":
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, "ru_RU")

def parse_habr_date(date_str):
    if "сегодня" in date_str:
        today = datetime.now()
        date_str = date_str.replase("сегодня", today.strftime("%d %B %Y"))
    elif "вчера" in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replase("вчера", yesterday.strftime("%d %B %Y"))
    try:
        return datetime.strptime(date_str, "%d %B %Y в %H:%M")
    except ValueError:
        return datetime.now()

def get_habr_snippets():
    html = get_html("https://habr.com/ru/search/?target_type=posts&q=python&order_by=date")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.find("div", class_="tm-sub-page__main").findAll("article", class_="tm-articles-list__item")
        for news in all_news:
            title = news.find("h2", class_="tm-article-snippet__title tm-article-snippet__title_h2").text
            url = news.find("a", class_="tm-article-snippet__title-link")["href"]
            published = news.find("span", class_="tm-article-snippet__datetime-published").text
            published = parse_habr_date(published)
            save_news(title, "https://habr.com" + url, published)