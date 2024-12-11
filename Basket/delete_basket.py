import requests
import configuration

#Функция для осуществления запроса на удаление корзины заказа
def delete_basket():
    return requests.delete(configuration.URL+configuration.BASKET+configuration.DELETE_BASKET_ID)
response_del_basket = delete_basket()

#print(response_del_basket.status_code, response_del_basket.json())
#Снять комментирование со строки выше для получения результата функции
