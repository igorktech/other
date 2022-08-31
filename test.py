import config
import telebot
import time
import random
# Create bot
bot = telebot.TeleBot(token=config.TOKEN)
# Address
CHANNEL_NAME = "@lovelycupidboy_bot"
# Load file
f = open('lovemassage.txt', 'r', encoding='UTF-8')
massages = f.read().split('\n')
f.close()
print(time.strftime("%D", time.localtime()))
# Command handler /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Your personal cupid')
    while ((time.strftime("%d", time.localtime())) == "01") or ((time.strftime("%d", time.localtime())) == "02"):
        if time.strftime("%H:%M", time.localtime()) =="09:00":
            bot.send_message(m.chat.id, "It's time to start your trip sweetheart")
        if time.strftime("%H:%M", time.localtime()) =="11:00":
            bot.send_message(m.chat.id, "Next station is on a plate")
        if time.strftime("%H:%M", time.localtime()) =="12:40":
            bot.send_message(m.chat.id, "May we try to swim?")
        if time.strftime("%H:%M", time.localtime()) == "13:45":
            bot.send_message(m.chat.id, "What is the best idea to get powers after the sea trip?")
        if time.strftime("%H:%M", time.localtime()) == "17:00":
            bot.send_message(m.chat.id, "I really recommend you relax")
        if (int(time.strftime("%H", time.localtime()))%2 == 0)and(int(time.strftime("%M", time.localtime())) == 0):
            bot.send_message(m.chat.id, random.choice(massages))
        time.sleep(60)

    for massage in massages:
        bot.send_message(m.chat.id, random.choice(massages))
        time.sleep(18000)
bot.polling(none_stop=True, interval=0)
