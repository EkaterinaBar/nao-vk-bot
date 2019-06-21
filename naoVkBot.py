# -*- coding: utf-8 -*-
import bs4 as bs4
import requests
import apiai, json

class Bot:

    def __init__(self, user_id):
        
        self.ID = user_id
        
        self.Name = self.get_name(user_id)

        self.Commands= ["ПРИВЕТ", "ПОГОДА", "ВРЕМЯ", "ПОКА"]

    def get_name(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self.clean(bs.findAll("title")[0])

        return user_name.split()[0]

    def textMessage(self, message):
        request = apiai.ApiAI('e044062e07af4406aba6f1cd5e1dceba').text_request() # ключ API к Dialogflow
        request.lang = 'ru' # язык запроса
        request.session_id = 'NaoBot' # ID Сессии диалога
        request.query = message # Посылаем запрос с сообщением
        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и получаем ответ
        # Если есть ответ от бота - возвращаем его
        if response:
            return response
        else:
            return "Что?"

    def new_message(self, mess):

        if mess.upper() == self.Commands[0]:
            return f"Приветствую, {self.Name}!"

        elif mess.upper() == self.Commands[1]:
            return self.weather()

        elif mess.upper() == self.Commands[2]:
            return self.time()

        elif mess.upper() == self.Commands[3]:
            return f"До свидания, {self.Name}!"

        else:
            return self.textMessage(mess)

    def time(self):
        request = requests.get("https://my-calend.ru/date-and-time-today")
        b = bs4.BeautifulSoup(request.text, "html.parser")
        return self.clean(str(b.select(".page")[0].findAll("h2")[1])).split()[1]

    @staticmethod
    def clean(string_line):

        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result

    @staticmethod
    def weather(city: str = "москва") -> list:

        request = requests.get("https://sinoptik.com.ru/погода-" + city)
        b = bs4.BeautifulSoup(request.text, "html.parser")

        p3 = b.select('.temperature .p3')
        weather1 = p3[0].getText()
        p4 = b.select('.temperature .p4')
        weather2 = p4[0].getText()
        p5 = b.select('.temperature .p5')
        weather3 = p5[0].getText()
        p6 = b.select('.temperature .p6')
        weather4 = p6[0].getText()

        result = ''
        result = result + ('Утром :' + weather1 + ' ' + weather2) + '\n'
        result = result + ('Днём :' + weather3 + ' ' + weather4) + '\n'
        temp = b.select('.rSide .description')
        weather = temp[0].getText()
        result = result + weather.strip()

        return result
