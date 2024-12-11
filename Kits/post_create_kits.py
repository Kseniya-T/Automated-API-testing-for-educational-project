import requests
import configuration
import data
from Users import post_create_user


#Функция для осуществления запроса на создание нового набора для созданного пользователя
def post_create_kit():
    return (requests.post(configuration.URL + configuration.POST_CREATE_KIT,
                         json = data.kit_body,
                         headers = post_create_user.token))
response_new_kit = post_create_kit()

print(response_new_kit.status_code, response_new_kit.json())