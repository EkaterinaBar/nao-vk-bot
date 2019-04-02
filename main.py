# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# --
#-- from commander.commander import Commander
from vk_bot import VkBot
import random
# --

def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id":get_random_id()})


# API-ключ созданный ранее
token = "cf60b2f0c288836085d81f31b403c57798c5f8ed8302b1247c662611a4c3e048a01424f5022664ec01890"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# commander = Commander()
print("Server started")

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
           # if event.text[0] == "/":
           #     write_msg(event.user_id, commander.do(event.text[1::]))
           # else:
            write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)
