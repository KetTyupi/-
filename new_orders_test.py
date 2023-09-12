import order_request

#Тюпина Екатерина, 8 когорта, дипломный проект - Инженер по тестированию плюс

#Тест на возврат ответа 200
def test_receive_order_track():
    response = order_request.get_receive_order_track(order_request.track_json)
    print(response.status_code)
    assert response.status_code == 200



