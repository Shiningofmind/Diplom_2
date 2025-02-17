import pytest
import allure
from data import EXISTED_PAYLOAD, EXIST_USER_ERROR_RESPONSE, MISSING_FIELDS_ERROR_RESPONS

@allure.epic("Управление пользователями")
@allure.description("Тесты для создания пользователя, включая валидацию и обработку ошибок.")
class TestCreateUser:

    @allure.title("Тест создания уникального пользователя")
    def test_create_unique_user(self, user_methods):
        response = user_methods.create_user()
        assert response.status_code == 200
        assert response.json() is not None

    @allure.title("Тест создания уже зарегистрированного пользователя")
    def test_create_already_registered_user(self, user_methods):
        response = user_methods.create_user(EXISTED_PAYLOAD)
        assert response.status_code == 403
        assert response.json() == EXIST_USER_ERROR_RESPONSE

    @pytest.mark.parametrize("field", ["email", "password", "name"])
    @allure.title("Тест создания пользователя с отсутствующим полем {field}")
    def test_create_user_missing_field(self, user_fixture, user_methods, field):
        payload, _ = user_fixture  # Берем только payload
        payload = payload.copy()
        del payload[field]
        response = user_methods.create_user(payload)
        assert response.status_code == 403
        assert response.json() == MISSING_FIELDS_ERROR_RESPONS