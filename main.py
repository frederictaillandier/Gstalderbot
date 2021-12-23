import requests
import werecycle
import rent

# bot configuration
telegram_URL = "https://api.telegram.org/"
bot_Token = "bot5013822196:AAEPswPRePxU4WT6ZIaxu1bBu4y_tM_TKdE"
chat_id = "930376906"

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

def main() -> int:
    # We recycle
    intro()
    we_recycle_message()
    rent_message()




if __name__ == '__main__':
    main()