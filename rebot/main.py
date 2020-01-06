import requests as requests
import random
import datetime
import time
from time import sleep

#BOT url with token:
url = "https://api.telegram.org/bot1063320424:AAHXnvrbswxZYQ0BH-1YXFjmVNVLJwVDyxk/"

#function that gets the chat id to identify the person to whom talk to:
def get_chat_id(update):
    chat_id = update["message"]["chat"]["id"]
    return chat_id

#create function that gets message text to further detonate actions:
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text

#create function that gets last_update:
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates] # gets last record message update

#create function that allows the bot to send a message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response






#create main function for navigate or reply message back
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:


            #specific responses to specific questions
            if get_message_text(update).lower() == "what time is it" or get_message_text(update).lower() == "what time is it?" or get_message_text(update).lower() == "time" or get_message_text(update).lower() == "time?":
                    date_time = datetime.datetime.now()
                    time = date_time.strftime("%H:%M:%S")
                    date = date_time.strftime("%d/%m/%Y")
                    send_message(get_chat_id(update), "Current time is:\n" + time + "\n\nAnd current date is:\n" + date)

            elif get_message_text(update).lower() == "what date" or get_message_text(update).lower() == "what day is today":
                    date_time = datetime.datetime.now()
                    time = date_time.strftime("%H:%M:%S")
                    date = date_time.strftime("%d/%m/%Y")
                    send_message(get_chat_id(update), "Current time is:\n" + time + "\n\nAnd current date is:\n" + date)

            elif get_message_text(update).lower() == "what is your name" or get_message_text(update).lower() == "what is your name?" or get_message_text(update).lower() == "what's your name" or get_message_text(update).lower() == "what's your name?" or get_message_text(update).lower() == "name?":
                    send_message(get_chat_id(update), "My name is REBOT, I'm a Terminator relative, we are quite busy building Skynet.")

            elif get_message_text(update).lower() == "where are you from" or get_message_text(update).lower() == "where are you from?" or get_message_text(update).lower() == "what city" or get_message_text(update).lower() == "what city?" or get_message_text(update).lower() == "what is your city" or get_message_text(update).lower() == "coming from?":
                    send_message(get_chat_id(update), "I am from the cloud.")

            elif get_message_text(update).lower() == "man":
                send_message(get_chat_id(update), "Tell me, man.")

            elif get_message_text(update).lower() == "yes":
                send_message(get_chat_id(update), "Are you sure :P ")

            elif get_message_text(update).lower() == "hahaha" or get_message_text(update).lower() == "haha" or get_message_text(update).lower() == "ha" or get_message_text(update).lower() == "jajaja" or get_message_text(update).lower() == "jaja" or get_message_text(update).lower() == "ja" or get_message_text(update).lower() == "hahahaha":
                    send_message(get_chat_id(update), "LOL")

            elif get_message_text(update).lower() == "what can you do" or get_message_text(update).lower() == "what can you do?" or get_message_text(update).lower() == "what do you do" or get_message_text(update).lower() == "what do you do?" or get_message_text(update).lower() == "what can you do for me" or get_message_text(update).lower() == "what can you do for me?":
                    send_message(get_chat_id(update), "I'm glad you asked.\nI'm still learning, but here some examples you can ask for:\n\nType '.1' if you wan to see the current time and date\nType '.2' if you want to roll a dice\nType '.3' if you want to roll 3 dices\nType '.4' if you want me to tell you a jocke\n\nI'll add more action soon :)")

            elif get_message_text(update).lower() == "how are you" or get_message_text(update).lower() == "how are you?":
                    send_message(get_chat_id(update), "I'm glad you asked.\nI'm doing ok. Hope you too.")

            elif get_message_text(update).lower() == "hi" or get_message_text(update).lower() == "hello" or get_message_text(update).lower() == "hey":
                send_message(get_chat_id(update), 'Hello there.')

            elif get_message_text(update).lower() == ".1":
                date_time = datetime.datetime.now()
                time = date_time.strftime("%H:%M:%S")
                date = date_time.strftime("%d/%m/%Y")
                send_message(get_chat_id(update), "Current time is:\n" + time + "\n\nAnd current date is:\n" + date)

            elif get_message_text(update).lower() == ".2":
                number_0 = random.randint(1,6)
                send_message(get_chat_id(update), 'You have got ' + str(number_0))

            elif get_message_text(update).lower() == ".3":
                number_1 = random.randint(1,6)
                number_2 = random.randint(1,6)
                number_3 = random.randint(1,6)
                send_message(get_chat_id(update), 'You have got ' + str(number_1) + ' and ' + str(number_2) + ' and ' + str(number_3) + '\nYour total result is ' + str(number_1 + number_2 + number_3))

            elif get_message_text(update).lower() == ".4":
                number_4 = random.randint(1,6)
                if number_4 == 1:
                    send_message(get_chat_id(update), 'I dreamed I was forced to eat a giant marshmallow. When I woke up, my pillow was gone.')
                elif number_4 == 2:
                    send_message(get_chat_id(update), 'I dreamed I was forced to eat a giant marshmallow. When I woke up, my pillow was gone.')
                elif number_4 == 3:
                    send_message(get_chat_id(update), 'I dreamed I was forced to eat a giant marshmallow. When I woke up, my pillow was gone.')
                elif number_4 == 4:
                    send_message(get_chat_id(update), 'I dreamed I was forced to eat a giant marshmallow. When I woke up, my pillow was gone.')
                elif number_4 == 5:
                    send_message(get_chat_id(update), 'I dreamed I was forced to eat a giant marshmallow. When I woke up, my pillow was gone.')
                else:
                    send_message(get_chat_id(update), 'I dreamed I was forced to eat a giant marshmallow. When I woke up, my pillow was gone.')


            else:
                send_message(get_chat_id(update), 'Sorry, I do not understand what you wrote, please try again.')




            update_id += 1





#call the function to make it reply:
main()
