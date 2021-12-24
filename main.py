import requests
import werecycle
import rent
import cardboard
import sys


# bot configuration
telegram_URL = "https://api.telegram.org/"
bot_Token = "bot5013822196:AAEPswPRePxU4WT6ZIaxu1bBu4y_tM_TKdE"
test_chat_id = "930376906"
prod_chat_id = "-602519148"
chat_id = test_chat_id


# API
sendMessageCommand = "/sendMessage"

def send_message(message):
    if message == None:
        return
    req = telegram_URL + bot_Token + sendMessageCommand
    content = {'chat_id': chat_id, 'text': message}
    r = requests.get(url = req, params = content)

def intro():
    send_message("Hello everyone !")

def we_recycle_message():
    message = werecycle.getNextFormatedWeRecycleDayOfWeek()
    send_message(message)

def rent_message():
    message = rent.rent_reminder()
    send_message(message)

def cardboard_pickup():
    message = cardboard.getNextFormatedCarboardDayOfWeek()
    send_message(message)

def main() -> int:
    intro()
    we_recycle_message()
    rent_message()
    cardboard_pickup()

if __name__ == '__main__':
    args = sys.argv[1:]
    print (args[0])
    if len(args) == 1 and args[0] == "-prod":
        chat_id = prod_chat_id
    main()