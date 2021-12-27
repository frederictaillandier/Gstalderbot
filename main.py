import modules.cardboardModule as cardboardModule
import modules.foodmasterModule as foodmasterModule
import modules.rentModule as rentModule
import modules.werecycleModule as werecycleModule
import modules.telegramAPIModule as telegramAPIModule
import modules.flatteryModule as flatteryModule

calls = [
    foodmasterModule.getFoodMasterMessage,
    werecycleModule.getWeRecycleMessage,
    cardboardModule.getCardBoardMessage,
    rentModule.getRentReminderMessage,
    flatteryModule.getFlatteryMessage
    ]

def main() -> int:
    message = "Hello everyone!\n"    
    for call in calls:
        phrase = call()
        if phrase != None:
            message += phrase + '\n'
    message += "Have a great week!"
    telegramAPIModule.send_message(message)

if __name__ == '__main__':
    main()