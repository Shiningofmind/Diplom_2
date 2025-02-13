import requests
import allure
from data import API_ENDPOINTS


class CreatingOrder:
    @allure.step("Создание заказа")
    def create_order(self, token, ingredients):
        headers = {"Authorization": token} if token else {}
        payload = {"ingredients": ingredients}
        return requests.post(API_ENDPOINTS["create_order"], json=payload, headers=headers)


