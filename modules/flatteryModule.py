import config.flatteryConfig as flatteryConfig
import datetime

def getFlatteryMessage():
    today = datetime.datetime.today()
    week = today.isocalendar()[1]
    message =  "Special message for " +  flatteryConfig.flatmates[week % len(flatteryConfig.flatmates)] + ": " + flatteryConfig.flatteries[week % len(flatteryConfig.flatteries)] + " ;)"
    return message