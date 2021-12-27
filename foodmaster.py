import datetime
import flatmates

weeks_calendar_delta = 4

def get_food_master():
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    week_number = tomorrow.isocalendar()[1] + weeks_calendar_delta
    food_master = flatmates.flatmates[week_number % 8]['name']
    return "From tomorrow, {0} is the food master".format(food_master)