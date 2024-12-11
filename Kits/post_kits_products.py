import configuration
import data
import requests

#Функция для осуществления запроса на поиск наборов, содержащих данный продукт/ы
def post_kits_products():
    return requests.post(configuration.URL + configuration.POST_MAIN_PRODUCTS,
                         headers=data.header,
                         json=data.ids_products)
response = post_kits_products()

#print(response.status_code, response.json())
#Снять комментирование со строки выше для получения результата функции