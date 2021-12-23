import requests
import werecycle

# bot configuration
telegram_URL = "https://api.telegram.org/"
bot_Token = "bot5013822196:AAEPswPRePxU4WT6ZIaxu1bBu4y_tM_TKdE"
chat_id = "930376906"

# API
sendMessageCommand = "/sendMessage"

def send_message(message):
    req = telegram_URL + bot_Token + sendMessageCommand
    content = {'chat_id': chat_id, 'text': message}
    r = requests.get(url = req, params = content)

def intro():
    send_message("Hello everyone !")

def recycle_message():
    message = werecycle.getNextFormatedWeRecycleDayOfWeek()
    send_message(message)

def main() -> int:
    # We recycle
    intro()
    recycle_message()

if __name__ == '__main__':
    main()