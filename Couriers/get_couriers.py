import requests
import configuration

#Функция для осуществления запроса на получение списка всех возможных доставок сервиса
def get_couriers():
    return requests.get(configuration.URL+configuration.GET_COURIERS)
response_couriers = get_couriers()

#print(response_couriers.status_code, response_couriers.json())
#Снять комментирование со строки выше для получения результата функции