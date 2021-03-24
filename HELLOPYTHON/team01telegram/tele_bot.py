import telegram
telgm_token = '1596083568:AAFroiRjK4odJN5jVkYmmSDwYTtrTQ2nEvk'
bot = telegram.Bot(token = telgm_token)
updates = bot.getUpdates()
bot.sendMessage(chat_id ='1609390701', text="모두들2 벼락부자되세요")
print(updates)
for i in updates:
    print(i)
print('start telegram chat bot')
    
    