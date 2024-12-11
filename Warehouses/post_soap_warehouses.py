import requests
import configuration
import data


#Функция для получения списка количества товаров на складах сервиса с помощью SOAP запроса
def post_soap_warehouses():
    return requests.post(configuration.URL + configuration.POST_WAREHOUSES,
                         data=data.ids_warehouses)
response_soap=post_soap_warehouses()

#print(response_soap.status_code, response_soap.text)
#Снять комментирование со строки выше для получения результата функции