# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
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

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            
            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Привет, друг!")
            elif request == "пока":
                write_msg(event.user_id, "Увидимся!")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")
