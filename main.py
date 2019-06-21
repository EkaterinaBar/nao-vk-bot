# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from naoVkBot import Bot
import random
import apiai, json


def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id":get_random_id()})


# API-key
token = "cf60b2f0c288836085d81f31b403c57798c5f8ed8302b1247c662611a4c3e048a01424f5022664ec01890"

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)


print("Начали")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('Текст сообщения:', event.text)
            print(f'От: {event.user_id}', end='')
            bot = Bot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))
