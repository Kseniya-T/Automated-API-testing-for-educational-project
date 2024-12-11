import configuration
import data
import requests

#Функция для осуществления запроса на создание корзины заказа
def post_new_basket():
    return requests.post(configuration.URL + configuration.BASKET,
                         headers=data.header,
                         json=data.new_basket)
response_basket = post_new_basket()

#print(response_basket.status_code, response_basket.json())
#Снять комментирование со строки выше для получения результата функции
