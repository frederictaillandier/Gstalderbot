import datetime 
import calendar

werecycle_dates = {
    datetime.datetime(2022, 4, 26),
    datetime.datetime(2022, 5, 10),
    datetime.datetime(2022, 5, 25),
    datetime.datetime(2022, 6, 19),
    datetime.datetime(2022, 6, 27),
}

def getNextWeRecycle():
    today = datetime.datetime.today()
    best = today + datetime.timedelta(days=365)
    for date in werecycle_dates:
        if date > today and date < best:
            best = date
    if best == (today + datetime.timedelta(days=365)):
        return None
    return best

def getWeRecycleMessage():
    next_week = datetime.datetime.today() + datetime.timedelta(days=7)
    next_pick = getNextWeRecycle()
    if next_pick == None:
        return "I don't know when is the next We-Recycle pick-up. :("
    if next_pick > next_week:
        return "No We-Recycle pick-up this week, it will be on the {0} of {1}.".format(str(next_pick.day), calendar.month_name[next_pick.month])
    return "Next We-Recycle pick-up is: {0} morning.".format(calendar.day_name[next_pick.weekday()])