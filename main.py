import requests

# bot configuration
telegram_URL = "https://api.telegram.org/"
bot_Token = "bot5013822196:AAEPswPRePxU4WT6ZIaxu1bBu4y_tM_TKdE"
chat_id = "930376906"

# API
sendMessageCommand = "/sendMessage"

def send_message(dest_id, message):
    req = telegram_URL + bot_Token + sendMessageCommand
    content = {'chat_id': dest_id, 'text': message}
    r = requests.get(url = req, params = content)

def main() -> int:
    # Example
    send_message(chat_id, "hello world")
    print("done")

if __name__ == '__main__':
    main()