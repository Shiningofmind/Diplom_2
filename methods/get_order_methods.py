import allure
import requests

from data import API_ENDPOINTS


class Order:
    @allure.step("Получение списка заказов пользователя")
    def get_orders(self, token):
        headers = {"Authorization": token} if token else {}
        return requests.get(API_ENDPOINTS["receiving_orders"], headers=headers)

