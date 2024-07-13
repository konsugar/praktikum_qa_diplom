# Константин Сахаров, 18-я когорта — Финальный проект. Инженер по тестированию плюс

# import requests
# import configuration
import data
import sender_stand_request


# Тест получения кода 200 при запросе данных заказа по треку.
# Без параметра, потому что на вход он будет получать одни и те же данные и использовать генерирующийся при создании
# нового заказа трек.
# Тестировщик не передаёт функции какие-то определённые тестовые данные.
def test1_response_200_while_getting_order_data_by_track_after_creating_new_order():
    # Выполнить запрос на создание заказа
    creating_response = sender_stand_request.create_new_order(data.new_order_body)
    # Сохранить номер трека заказа
    global_track = sender_stand_request.get_new_order_track(creating_response)
    # Выполнить запрос на получения заказа по треку заказа
    check_response = sender_stand_request.get_order_data_by_track(global_track).status_code
    # Проверить, что код ответа равен 200
    assert check_response == 200
