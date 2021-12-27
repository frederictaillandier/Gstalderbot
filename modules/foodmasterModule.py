import datetime
import config.flatmatesConfig as flatmatesConfig

weeks_calendar_delta = 4

def getFoodMasterMessage():
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    week_number = tomorrow.isocalendar()[1] + weeks_calendar_delta
    food_master = flatmatesConfig.flatmates[week_number % len(flatmatesConfig.flatmates)]['name']
    return "From tomorrow, {0} is the food master".format(food_master)