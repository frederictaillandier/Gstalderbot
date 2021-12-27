import datetime 
import calendar

werecycle_dates = {
    datetime.datetime(2022, 1, 18),
    datetime.datetime(2022, 1, 27),
    datetime.datetime(2022, 2, 8),
    datetime.datetime(2022, 2, 23),
    datetime.datetime(2022, 3, 11),
    datetime.datetime(2022, 3, 28),
}

def getNextWeRecycle():
    today = datetime.datetime.today()
    best = datetime.datetime(2050,1,1)
    for date in werecycle_dates:
        if date > today and date < best:
            best = date
    if best == datetime.datetime(2050,1,1):
        return None
    return best

def getWeRecycleMessage():
    next_week = datetime.datetime.today() + datetime.timedelta(days=7)
    next_pick = getNextWeRecycle()
    if next_pick == None:
        return "I don't know when is the next We-Recycle pick-up. :("
    if next_pick > next_week:
        return "No We-Recycle pick-up this week.\nIt will be on the {0} of {1}.".format(str(next_pick.day), calendar.month_name[next_pick.month])
    return "Next We-Recycle pick-up is: {0} morning.".format(calendar.day_name[next_pick.weekday()])