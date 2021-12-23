import datetime
import calendar

def rent_reminder() -> str:
    today = datetime.datetime.today()
    next_week = today + datetime.timedelta(days=7)
    rent_limit = datetime.datetime(today.year, today.month, 27)
    rent_reminder_date = rent_limit + datetime.timedelta(days=-2)
    message = ""

    if (today < rent_reminder_date and rent_reminder_date < next_week):
        message += "Don't forget to pay your rent for " + calendar.day_name[rent_limit.weekday()] + "."
        return message
    return None

