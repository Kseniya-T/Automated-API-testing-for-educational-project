import configuration
from Products import put_cost_product


#Тесты для запроса на изменения цены продукта
def test_put_cost():
    testing_response = put_cost_product.response_put_cost
    assert testing_response.status_code == 200
    assert testing_response.json()['ok'] == True

def test_negative_put_cost():
    configuration.PUT_COST_ID = '/123456'
    response = put_cost_product.put_cost()
    assert response.status_code == 404
    assert response.json()['message'] == 'Not Found'

def test_negative_put_cost_no_id():
    configuration.PUT_COST_ID = ''
    response = put_cost_product.put_cost()
    assert response.status_code == 400 or 405


