import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = True
WEATHER_DEFAULT_CITY = "Moscow,Russia"
WEATHER_API_KEY = "047aff68951c4c438db191152220304"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, "..", "webapp.db")
SEND_FILE_MAX_AGE_DEFAULT = 0

SECRET_KEY = "wegwfo3403ug838_pg0i90"
