import requests
import configuration
import data


# Функция "Создать новый заказ"
def create_new_order(param_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         headers=data.headers,
                         json=param_body
                         )

# Функция create_new_order получает ответ сервера. В нём есть код ответа 201 со словом Created
# и тело, состоящее только из ключа-значения трека (track)

# следующие строки были для проверки, что всё работает в самой функции; при тесте они не нужны
# create_new_order_response = create_new_order(data.new_order_body)
# print(create_new_order_response.status_code)
# print(create_new_order_response.json())
# print(create_new_order_response.json()["track"])


# Старая редакция функции получения трека нового заказа.
# Обращается к функции создания заказа с параметром, взятым из файла data.
# Тело полученного от сервера ответа (об успешном создании заказа) функция записывает в свою внутреннюю переменную.
# Из этой переменной функция берёт значение ключа track и записывает его в ещё одну внутреннюю переменную.
# Значение этой второй внутренней переменной функция возвращает наружу.
# def get_new_order_track():
#    new_order_response = create_new_order(data.new_order_body)
#    new_track = new_order_response.json()["track"]
#    return new_track
# Старая функция закончилась


# Второй вариант функция получения трека нового заказа.
# Раньше она работала без параметра и вызывала сама функцию create_new_order, то есть в рамках обновлённого теста
# функция create_new_order срабатывала повторно.
# Теперь get_new_order_track будет работать на параметре, который тест возьмёт у функции создания и передаст функции
# получения трека.
# Функция берёт тело полученного от сервера ответа (об успешном создании заказа) и записывает в свою внутреннюю
# переменную (new_track) значение ключа track из тела.
# Значение этой внутренней переменной (new_track) функция возвращает наружу — в тест.

def get_new_order_track(param_new_order_response):
    new_track = param_new_order_response.json()["track"]
    return new_track


# Функция получения данных заказа по треку имеющегося заказа.
# У неё есть параметр, в него она будет получать номер трека свежесозданного заказа. Тест возьмёт этот номер из
# результата работы функции get_new_order_track
def get_order_data_by_track(param_ordertrack):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_DATA_BY_TRACK + str(param_ordertrack))

# Функция get_order_data_by_track получает ответ сервера: данные заказа.
# В нём есть заголовок (200 при успехе), а также тело, в котором все поля таблицы Orders
