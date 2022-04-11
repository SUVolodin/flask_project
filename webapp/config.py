from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False
WEATHER_DEFAULT_CITY = "Moscow,Russia"
WEATHER_API_KEY = "047aff68951c4c438db191152220304"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, "..", "webapp.db")

SECRET_KEY = "lofhosekfi38tr7rgrgrb"

REMEMBER_COOKIE_DURATION = timedelta(days=7)