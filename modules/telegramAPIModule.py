import requests
import sys
import config.telegramApiConfig as telegramApiConfig

def send_message(message):
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == "-prod":
        chat_id = telegramApiConfig.config['prod_chat_id']
    else:
        chat_id = telegramApiConfig.config['test_chat_id']
    if message == None:
        return
    req = telegramApiConfig.config['telegram_URL'] + telegramApiConfig.config['bot_Token'] + telegramApiConfig.config['sendMessageCommand'] 
    content = {'chat_id': chat_id, 'text': message}
    r = requests.get(url = req, params = content)