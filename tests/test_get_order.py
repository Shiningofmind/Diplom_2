import allure
from data import AUTH_ERROR_RESPONSE

@allure.epic("Управление заказами")
@allure.description("Тесты для получения заказов конкретного пользователя: авторизованный и неавторизованный пользователь.")
class TestGetOrders:

    @allure.title("Тест получения заказов авторизованным пользователем")
    def test_get_orders_authorized_user(self, existing_user_fixture, get_order_methods):
        response = get_order_methods.get_orders(existing_user_fixture)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert isinstance(response.json().get("orders"), list)

    @allure.title("Тест получения заказов неавторизованным пользователем")
    def test_get_orders_unauthorized_user(self, get_order_methods):
        response = get_order_methods.get_orders("")
        assert response.status_code == 401
        assert response.json() == AUTH_ERROR_RESPONSE
