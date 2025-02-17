import allure
from data import ingredient1, ingredient2, INGR_ID_ERROR_RESPONSE, INTERNAL_SERVER_ERROR_RESPONSE

@allure.epic("Управление заказами")
@allure.description("Тесты для создания заказов, с авторизацией и без, а также валидации ингредиентов.")
class TestCreateOrder:

    @allure.title("Тест создания заказа с авторизацией")
    def test_create_order_with_authorization(self, existing_user_fixture, order_methods):
        ingredients = [ingredient1, ingredient2]
        response = order_methods.create_order(existing_user_fixture, ingredients)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    @allure.title("Тест создания заказа без авторизации")
    def test_create_order_without_authorization(self, order_methods):
        ingredients = [ingredient1, ingredient2]
        response = order_methods.create_order(None, ingredients)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    @allure.title("Тест создания заказа без ингредиентов")
    def test_create_order_without_ingredients(self, existing_user_fixture, order_methods):
        response = order_methods.create_order(existing_user_fixture, [])
        assert response.status_code == 400
        assert response.json() == INGR_ID_ERROR_RESPONSE

    @allure.title("Тест создания заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient(self, existing_user_fixture, order_methods):
        ingredients = ["invalid_hash_ingredient"]
        response = order_methods.create_order(existing_user_fixture, ingredients)
        assert response.status_code == 500
        assert response.text.strip() == INTERNAL_SERVER_ERROR_RESPONSE.strip()
