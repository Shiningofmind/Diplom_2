import allure
import requests
from data import API_ENDPOINTS


class UserProfile:
    @allure.step("Получение информации о пользователе")
    def get_user_info(self, token):
        headers = {"Authorization": token}
        return requests.get(API_ENDPOINTS["changing_user_data"], headers=headers)

    @allure.step("Обновление информации о пользователе")
    def update_user_info(self, token, email=None, name=None):
        headers = {"Authorization": token}
        payload = {}
        if email:
            payload["email"] = email
        if name:
            payload["name"] = name
        return requests.patch(API_ENDPOINTS["changing_user_data"], json=payload, headers=headers)
    