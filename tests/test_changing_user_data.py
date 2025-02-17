import allure
from data import EXISTED_PAYLOAD, AUTH_ERROR_RESPONSE, EMAIL_ERROR_RESPONSE

@allure.epic("Управление профилем пользователя")
@allure.description("Тесты для управления профилями пользователей, включая создание, получение и обновление.")
class TestUserProfile:

    @allure.title("Тест получения информации о пользователе с авторизацией")
    def test_get_user_info_with_authorization(self, user_fixture, login_user, profile_methods):
        payload, token = user_fixture
        response = profile_methods.get_user_info(token)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json()["user"]["email"] == payload["email"]
        assert response.json()["user"]["name"] == payload["name"]


    @allure.title("Тест обновления информации о пользователе с авторизацией")
    def test_update_user_info_with_authorization(self, user_fixture, user_methods, profile_methods):
        payload, token = user_fixture
        new_email = f'{user_methods.generate_random_string(8)}@mail.com'
        new_name = user_methods.generate_random_string(8)
        response = profile_methods.update_user_info(token, new_email, new_name)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json()["user"]["email"] == new_email
        assert response.json()["user"]["name"] == new_name


    @allure.title("Тест обновления информации о пользователе без авторизации")
    def test_update_user_info_without_authorization(self, profile_methods):
        response = profile_methods.update_user_info("", "new_email@mail.com", "NewName")
        assert response.status_code == 401
        assert response.json() == AUTH_ERROR_RESPONSE

    @allure.title("Тест обновления информации с уже существующим email")
    def test_update_with_existing_email(self, user_fixture, profile_methods):
        _, token = user_fixture
        existing_email = EXISTED_PAYLOAD["email"]
        response = profile_methods.update_user_info(token, existing_email)
        assert response.status_code == 403
        assert response.json() == EMAIL_ERROR_RESPONSE