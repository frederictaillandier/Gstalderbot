import modules.cardboardModule as cardboardModule
import modules.foodmasterModule as foodmasterModule
import modules.rentModule as rentModule
import modules.werecycleModule as werecycleModule
import modules.telegramAPIModule as telegramAPIModule

def main() -> int:
    telegramAPIModule.send_message("Hello everyone !")
    telegramAPIModule.send_message(foodmasterModule.getFoodMasterMessage())
    telegramAPIModule.send_message(werecycleModule.getWeRecycleMessage())
    telegramAPIModule.send_message(cardboardModule.getCardBoardMessage())
    telegramAPIModule.send_message(rentModule.getRentReminderMessage())

if __name__ == '__main__':
    main()