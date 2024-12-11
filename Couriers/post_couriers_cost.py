import data
import configuration
import requests

#Функция для осуществления запроса для поиска служб доставок, способных выполнить данный заказ
def post_couriers_cost():
    return requests.post(configuration.URL + configuration.POST_COURIERS_COST,
                         headers=data.header,
                         json=data.products)
response_cost = post_couriers_cost()

#print(response_cost.status_code, response_cost.json())
#Снять комментирование со строки выше для получения результата функции