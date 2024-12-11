import requests
import configuration
import data


#Функция для осуществления запроса на изменение цены продукта в системе сервиса
def put_cost():
    return requests.put(configuration.URL + configuration.PUT_COST + configuration.PUT_COST_ID,
                        headers=data.header,
                        json=data.new_cost)
response_put_cost = put_cost()

#print(response_put_cost.status_code, response_put_cost.json())
#Снять комментирование со строки выше для получения результата функции