# nepali_toolkit/calendar.py
from nepali_datetime import date as bs_date
import datetime

def convert(from_calendar: str, input_date: str) -> str:
    if from_calendar.upper() == "AD":
        year, month, day = map(int, input_date.split('-'))
        ad_date = datetime.date(year, month, day)
        bs = bs_date.from_datetime_date(ad_date)
        return f"{bs.year}-{bs.month:02d}-{bs.day:02d}"
    elif from_calendar.upper() == "BS":
        year, month, day = map(int, input_date.split('-'))
        bs = bs_date(year, month, day)
        ad = bs.to_datetime_date()
        return f"{ad.year}-{ad.month:02d}-{ad.day:02d}"
    else:
        return "Invalid calendar type. Use AD or BS."
