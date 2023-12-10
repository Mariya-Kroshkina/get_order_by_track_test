import data
import requests
import configuration

#создаем заказ
def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.ORDER_BODY)

#сохраняем трек номер из заказа
def get_track():
    track_body = create_order().json()
    return track_body['track']

#получаем данные о заказе по его треку
def get_orderData_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + str(get_track()))