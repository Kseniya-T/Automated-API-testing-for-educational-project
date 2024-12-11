import requests
import configuration


#Таблица из базы данных со списком корзин заказов
def get_order_model():
    return requests.get(configuration.URL+configuration.GET_ORDER_MODEL)

response_order_table = get_order_model()

#Таблица из базы данных со списком наборов
def get_kit_model():
    return requests.get(configuration.URL+configuration.GET_KIT_MODEL)

response_kit_table = get_kit_model()

#Таблица из базы данных со списком продуктов
def get_product_model():
    return requests.get(configuration.URL+configuration.GET_PRODUCT_MODEL)

response_product_table = get_product_model()
