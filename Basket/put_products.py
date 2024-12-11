import requests
import configuration
import data

#Функция для осуществления запроса на изменение состава корзины заказа
def create_products():
    return requests.put(configuration.URL + configuration.PUT_PRODUCTS_BASKET + configuration.PUT_BASKET_ID,
                        headers=data.header,
                        json=data.product_in_basket)
response_put_basket = create_products()

#print(response_put_basket.status_code, response_put_basket.json())
#Снять комментирование со строки выше для получения результата функции