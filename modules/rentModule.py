import datetime
import calendar

rent_day_of_the_month = 27


def getRentReminderMessage() -> str:
    today = datetime.datetime.today()
    next_week = today + datetime.timedelta(days=7)
    rent_limit = datetime.datetime(today.year, today.month, rent_day_of_the_month)
    # We add 2 days to prevent to be warned on the exact day
    rent_reminder_date = rent_limit + datetime.timedelta(days=-2)
    if (today < rent_reminder_date and rent_reminder_date < next_week):
        return "Don't forget to pay your rent for {0}.".format(calendar.day_name[rent_limit.weekday()])
    return None

