import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = True
WEATHER_DEFAULT_CITY = "Moscow,Russia"
WEATHER_API_KEY = "5c9e49c87a064f128db203756220403"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, "..", "webapp.db")