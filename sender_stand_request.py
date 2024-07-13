import requests
import configuration
import data


# Функция "Создать новый заказ"
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         headers=data.headers,
                         json=body
                         )

# Функция create_new_order получает ответ сервера. В нём есть код ответа 201 со словом Created
# и тело, состоящее только из ключа-значения трека (track)


# следующие строки были для проверки, что всё работает в самой функции; при тесте они не нужны

# create_new_order_response = create_new_order(data.new_order_body)
# print(create_new_order_response.status_code)
# print(create_new_order_response.json())
# print(create_new_order_response.json()["track"])

# Функцию можно было разместить в одном файле вместе со всеми остальными функциями, но я решил оставить файлы примерно
# так же, как в проекте 10-го спринта, который я взял за основу.
