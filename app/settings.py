import os
from datetime import datetime, timedelta
from pytz import timezone

DATABASE_URL = os.getenv('DATABASE_URL').replace("://", "ql://", 1)

def time_range():
    tz = "America/Sao_Paulo"
    new_tz = timezone(tz)
    datetime_tz = datetime.now(new_tz)

    time_range = timedelta(seconds=30)
    start_time_range = (datetime_tz - time_range).time()
    end_time_range = (datetime_tz + time_range).time()
    return start_time_range, end_time_range