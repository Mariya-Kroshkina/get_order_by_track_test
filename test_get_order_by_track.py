import pytest
import request_sender

# позитивный тест на проверку получения данных о заказе по трек номеру.
def test_possible_get_track_by_name():
    response = request_sender.get_orderData_by_track()

    assert response.status_code == 200
