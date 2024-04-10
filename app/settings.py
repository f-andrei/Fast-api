import os
from datetime import datetime, timedelta
from pytz import timezone
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#DATABASE_URL = os.getenv('DATABASE_URL').replace("://", "ql://", 1)

def time_range():
    tz = "America/Sao_Paulo"
    new_tz = timezone(tz)
    datetime_tz = datetime.now(new_tz)

    time_range = timedelta(seconds=30)
    start_time_range = (datetime_tz - time_range).time()
    end_time_range = (datetime_tz + time_range).time()
    return start_time_range, end_time_range