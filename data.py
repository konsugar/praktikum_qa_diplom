# Заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# Тело создания нового заказа
new_order_body = {
    "firstName": "firstname_test",
    "lastName": "lastname_test",
    "address": "address_test",
    "metroStation": 107,
    "phone": "+99999999999",
    "rentTime": 1,
    "deliveryDate": "2024-12-31",
    "comment": "comment_test",
    "color": [
        "BLACK"
    ]
}
