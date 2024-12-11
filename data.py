header = {
    "Content-Type": "application/json"
}

#Тело запроса для post_kits_products
ids_products = {
    'ids':[2]
}

#Тело запроса для post_soap_warehouses
ids_warehouses = '<?xml version="1.0" encoding="utf-8"?>\
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.MainWsdl">\
    <soap:Body>\
        <Request xmlns="WebServices.MainWsdl">\
            <ids>1</ids>\
            <ids>4</ids>\
            <ids>44</ids>\
        </Request>\
    </soap:Body>\
</soap:Envelope>'

#Тело запроса для post_couriers_cost
products = {
    "products": [
        {
            "id": 1,
            "quantity": 3
        },
        {
            "id": 4,
            "quantity": 1
        },
        {
            "id": 9,
            "quantity": 3
        }
    ],
    "deliveryTime": 7
}

#Тело запроса для put_cost_product
new_cost = {
    "price": '175'
}

#Тело запроса для post_basket
new_basket = {
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        }
    ]
}

#Тело запроса для post_create_user
user_body = {
    "firstName": "Ева",
    "phone": "+79998889988",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

#Тело запроса для put_products
product_in_basket = {
    "productsList": [
        {
            "id": 20,
            "quantity": 4
        }
    ]
}


#Тело запроса для post_create_kit
kit_body = {
    'name': 'Вкусняшки'
}