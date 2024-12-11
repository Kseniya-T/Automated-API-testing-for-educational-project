import configuration
import data
import requests

#Функция для осуществления запроса на создание нового пользователя
def create_user():
    return requests.post(configuration.URL + configuration.CREATE_USER,
                         headers=data.header,
                         json=data.user_body)
response_user = create_user()
token = {'Authorization': 'Bearer '+ response_user.json()['authToken']}

#print(response_user.status_code, response_user.json())
#Снять комментирование со строки выше для получения результата функции