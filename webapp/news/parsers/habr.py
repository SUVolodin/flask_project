from datetime import datetime, timedelta
import locale
import platform

from bs4 import BeautifulSoup

from webapp.news.parsers.utils import get_html, save_news

if platform.system() == "Windows":
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_ALL, "ru_RU")


def parser_habr_date(date_str):
    if "сегодня" in date_str:
        today = datetime.now()
        date_str = date_str.replace("сегодня", today.strftime("%d %B %Y"))
    elif "вчера" in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace("вчера", yesterday.strftime("%d %B %Y"))
    try:
        return datetime.strptime(date_str, "%d  %B %Y в %H:%M")
    except ValueError:
        return datetime.now()


def get_habr_snippets():
    html = get_html("https://www.habr.com/ru/search/?target_type=posts&q=python&order_by=date")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.find("div", class_="tm-articles-list").findAll("div", class_="tm-article-snippet")
        result_news = []
        for news in all_news:
            title = news.find("h2", class_="tm-article-snippet__title tm-article-snippet__title_h2").text
            url = news.find("a", class_="tm-article-snippet__title-link")["href"]
            published = news.find("span", class_="tm-article-snippet__datetime-published").text
            published = parser_habr_date(published)
            print(title, url, published)
            """
            try:
                published = datetime.strptime(published, "%Y-%m-%d")
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)
            """