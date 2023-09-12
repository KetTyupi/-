import data
import main
import requests

# Создание нового заказа
def post_new_order(order_body):
    return requests.post(data.URL_SERVICE + data.CREATE_ORDER, json=order_body, headers=main.headers)

track_json = post_new_order(main.order_body).json();

#Получение заказа по треку заказа
def get_receive_order_track(track_body):
    return requests.get(data.URL_SERVICE + data.ORDER_TRACK, params={"t": track_body["track"]})

