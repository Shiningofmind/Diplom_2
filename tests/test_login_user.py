import allure
from data import LOGIN_ERROR_RESPONSE

@allure.epic("Управление пользователями")
@allure.description("Тесты для авторизации пользователей")
class TestLoginUser:

    @allure.title("Тест авторизации существующего пользователя")
    def test_login_existing_user(self, login_user):
        response = login_user.login_user()
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json().get("accessToken") is not None

    @allure.title("Тест авторизации с некорректными учетными данными")
    def test_login_with_incorrect_credentials(self, login_user):
        payload = {
            "email": "wrong.email@mail.com",
            "password": "wrongpassword"
        }
        response = login_user.login_user(payload)
        assert response.status_code == 401
        assert response.json() == LOGIN_ERROR_RESPONSE

    @allure.title("Тест авторизации с отсутствующим полем")
    def test_login_missing_field(self, login_user):
        payload = {
            "email": "",
            "password": "password"
        }
        response = login_user.login_user(payload)
        assert response.status_code == 401
        assert response.json() == LOGIN_ERROR_RESPONSE
