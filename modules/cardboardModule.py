import datetime
import calendar

cardboard_dates = {
    datetime.datetime(2022, 1, 7),
    datetime.datetime(2022, 2, 4),
    datetime.datetime(2022, 3, 4),
    datetime.datetime(2022, 4, 1),
    datetime.datetime(2022, 5, 6),
    datetime.datetime(2022, 6, 3),
    datetime.datetime(2022, 7, 1),
    datetime.datetime(2022, 8, 5),
    datetime.datetime(2022, 9, 2),
    datetime.datetime(2022, 10, 7),
    datetime.datetime(2022, 11, 4),
    datetime.datetime(2022, 12, 2)
}

def getNextCarboardPickup():
    today = datetime.datetime.today()
    best = today + datetime.timedelta(days=365)
    for date in cardboard_dates:
        if date > today and date < best:
            best = date
    if best == (today + datetime.timedelta(days=365)):
        return None
    return best

def getCardBoardMessage():
    next_week = datetime.datetime.today() + datetime.timedelta(days=7)
    next_pick = getNextCarboardPickup()
    if next_pick == None:
        return "I don't know when is the next Cardboard pick-up. :("
    if next_pick < next_week:
        return  "Next Cardboard pick-up is: {0} morning.".format(calendar.day_name[next_pick.weekday()])
    return None