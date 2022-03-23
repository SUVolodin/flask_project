from flask import Flask, render_template
from app.weather import weather_by_city
from app.python_news_org import get_python_news

def creatw_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        title = "Новости Python"
        weather = weather_by_city("Moscow,Russia")
        news_list = get_python_news()
        return render_template("index.html", page_title=title, weather=weather, news_list=news_list)
    return app
app = creatw_app()